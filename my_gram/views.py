from django.contrib.auth.decorators import login_required
from .models import Pictures, Profile, Comment
from django.contrib.auth.models import User
from my_gram.forms import ProfileForm, UploadPicForm, CommentForm

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from friendship.models import Follow
from friendship.models import AlreadyExistsError


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    pics = Pictures.get_pictures()
    form=CommentForm()
    comments=Comment.objects.all()
    context={"pics":pics,
            "form":form,
            "comments":comments
    }

    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your EphaGram account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form = ProfileForm()
    return render(request, 'new_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def upload_pic(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadPicForm(request.POST, request.FILES)
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = current_user
            pic.save()
    else:
        form = UploadPicForm()
    return render(request, 'UploadPicForm.html', {"form": form})


@login_required(login_url='/accounts/login/')
def display_profile(request, user_id):
    users = User.objects.get(id=user_id)
    print(users)
    profile=Profile.objects.get(user=users)
    followers = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    picts = Pictures.objects.filter(user=users)
    context={"profile":profile,
            "picts":picts,
            "users":users,
            "followers":followers,
            "following":following,
            "follow":follow
    }
    return render(request, 'display_profile.html', context)


@login_required(login_url='/accounts/login/')
def addcomment(request,picture_id):
    current_user = request.user
    if request.method == 'POST':
        picture = get_object_or_404(Pictures, pk=picture_id)
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.picture = picture
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()

    return redirect(index)


@login_required(login_url='/accounts/login/')
def follow(request,user_id):
   users = User.objects.get(id=user_id)
   try:
       follow = Follow.objects.add_follower(request.user, users)
   except AlreadyExistsError:
       return Http404
       print("fdsfghgfd")
   return redirect('/show/profile/'+user_id)
