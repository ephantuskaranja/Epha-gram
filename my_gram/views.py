from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pictures, Profile
from django.contrib.auth.models import User
# Create your views here.
from my_gram.forms import ProfileForm, UploadPicForm


@login_required(login_url='/accounts/login/')
def index(request):
    pics = Pictures.get_pictures()

    return render(request, 'index.html',{"pics":pics})


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



def display_profile(request, user_id):
    users = User.objects.get(id=user_id)
    profile=Profile.objects.get(user=users)
    print("fchcvvhghfgghf")
    context={"profile":profile,
            "users":users
    }
    return render(request, 'display_profile.html', context)
