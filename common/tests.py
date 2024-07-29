from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, DetailedInfo


class BlogModelsTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title="Test Post", content="Test Content")
        self.detailed_info = DetailedInfo.objects.create(
            post=self.post,
            description="Test Description",
            additional_details="Additional Test Details"
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "Test Content")

    def test_detailed_info_creation(self):
        self.assertEqual(self.detailed_info.post, self.post)
        self.assertEqual(self.detailed_info.description, "Test Description")
        self.assertEqual(self.detailed_info.additional_details, "Additional Test Details")

    def test_post_detailed_info_url(self):
        detailed_info_url = self.post.get_detailed_info_url()
        self.assertIsNotNone(detailed_info_url)
        self.assertIn(f"/detailed_info/{self.detailed_info.pk}/", detailed_info_url)


class BlogAPITest(APITestCase):

    def setUp(self):
        self.post = Post.objects.create(title="Test Post", content="Test Content")
        self.detailed_info = DetailedInfo.objects.create(
            post=self.post,
            description="Test Description",
            additional_details="Additional Test Details"
        )
        self.post_url = reverse('post-list')
        self.detailed_info_url = reverse('detailedinfo-list')

    def test_post_list(self):
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Post")

    def test_detailed_info_list(self):
        response = self.client.get(self.detailed_info_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['description'], "Test Description")

    def test_detailed_info_detail(self):
        detailed_info_detail_url = reverse('detailed_info_detail', kwargs={'pk': self.detailed_info.pk})
        response = self.client.get(detailed_info_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], "Test Description")
