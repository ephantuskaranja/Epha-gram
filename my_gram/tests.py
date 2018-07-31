from django.test import TestCase
from .models import Profile, Pictures, Comment
from django.core.files import File

from django.test import override_settings
from PIL import Image
import tempfile


# Create your tests here.
# class SimpleTest(TestCase):
#     def registering(self, username, email, password, passwordCheck, phone):
#         with open('/media/profileimages/t1.jpeg') as test:
#             imgStringIO = StringIO(test.read())
#
#         return self.app.post('/registering',
#             content_type='multipart/form-data',
#             data=dict(
#                 {'file': (imgStringIO, 'test.jpg')},
#                 username=username,
#                 email=email,
#                 password=password,
#                 passwordCheck=passwordCheck,
#                 phone=phone
#             ), follow_redirects=True
#         )
#
#
#     def test_03_registering(self):
#         rv = self.registering('TestUser', 'test@test.com', 'passwordTest', 'passwordTest', '900102030')
#         assert 'Registered Successfully' in rv.data

class Test_Comment(TestCase):
    # setup method
    def setUp(self):
        self.comment_text = Comment(comment_text = 'fgghhjfood')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comment_text, Comment))

    #testing save method
    def test_save_method(self):
        self.comment_text.save_comment()
        comments = Comment.objects.filter(id=1)
        self.assertTrue(comment_text=='fgghhjfood')


class Test_Profile(TestCase):
    # setup method
    def setUp(self):
        self.bio = Profile(bio = 'fgghhjfood')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.bio, Profile))

    #testing save method
    def test_save_method(self):
        self.bio.save_bio()
        prof = Profile.objects.filter(id=1)
        self.assertTrue(prof=='fgghhjfood')
