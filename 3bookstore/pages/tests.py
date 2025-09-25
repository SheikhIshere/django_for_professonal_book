# pages/test.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import Homepageview, AboutPageView

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_url_name(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_template(self):
        response= self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        # self.assertContains(response, 'Thi\s is our home page.')
        self.assertContains(response, 'This is our home page.')
    
    def test_homepage_dose_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'hi there! i should not be on the page')
    
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, Homepageview.as_view().__name__)

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('pages:about')
        self.response = self.client.get(url)
    
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
    
    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'hi there! i sould not be here'
        )
    
    def test_about_page_urls_resolve_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )