"""
Test admin module.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Test admin site."""

    def setUp(self):
        """Set up."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='user2@example.com',
            password='test123',

        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user1@example.com',
            password='test123',
            name='Test user full name',
        )

    def test_users_listed(self):
        """Test that users are listed on user page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test that the edit user page works."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)