# pages/tests.py

from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

# Create your tests here.


class HomePageTest(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get(reverse('home'))

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'This text should not be on the page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__,
                         HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get(reverse('about'))

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'This text should not be on the page')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
