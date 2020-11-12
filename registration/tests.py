from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from django.urls import reverse

# Create your tests here.
class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='sabrinaK', password='testing321')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='sabrinaK', password='testing321')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='testing321')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='sabrinaK', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

class SignUpTests(TestCase):
    def setUp(self):
        self.username = 'test_user_358'
        self.password = 'testing4321'

    def test_signup_page_url(self):
        response = self.client.get(reverse('game-signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/signup.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('game-signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/signup.html')
