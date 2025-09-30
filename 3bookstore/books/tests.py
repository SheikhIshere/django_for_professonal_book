# books/tests.py

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Book, Review
from django.contrib.auth.models import Permission

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='reviewer',
            email='reviewer@email.com',
            password='password123',
        )
        cls.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )
        # create the review with the exact text the test expects
        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review='An excellent review',
        )

        cls.special_permission = Permission.objects.get(
            codename = 'special_status'
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.price}", "25.00")

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "An excellent review")
        # make sure this matches the actual filename of your template:
        self.assertTemplateUsed(response, "books/book_details.html")
    
    def test_book_list_view_for_logged_in_user(self):
        self.client.login(
            email='reviewer@email.com', 
            password='password123'
        )

        response = self.client.get(
            reverse('book_list')
        )
        self.assertEqual(
            response.status_code, 
            200
        )
        self.assertContains(
            response, 
            'Harry Potter'
        )
        self.assertTemplateUsed(
            response, 
            'books/book_list.html'
        )
    
    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "%s?next=/books/" % (
                reverse("account_login")
            )
        )
        response = self.client.get(
            '%s?next=/books/' % (
                reverse('accounts_login')
            )
        )
        self.assertContains(response, 'Log In')

    def test_book_details_view_with_permission(self):
        self.client.login(
            email = 'reviewer@email.com',
            password = 'password123',
        )
        self.user = self.__class__.user
        self.user.user_permissions.add(self.special_permission)

        response = self.client.get(
            self.book.get_absolute_url()
        )
        no_response = self.client.get(
            '/books/123/'
        )
        self.assertEqual(
            response.status_code, 200
        )
        self.assertEqual(
            no_response.status_code, 
            404
        )
        self.assertContains(
            response, "Harry Potter"
        )
        self.assertContains(
            response, "An excellent review"
        )
        self.assertTemplateUsed(
            response, "books/book_details.html"
        )
    
# cz of all auth and abstruct_usre_model for this book it's getting error but in future it will be ok cz i will be using one authen tication system