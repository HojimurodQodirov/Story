from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def get_detailed_info_url(self):
        first_detailed_info = self.detailedinfo_set.first()
        if first_detailed_info:
            return reverse('detailed_info_detail', kwargs={'pk': first_detailed_info.pk})
        return None

    def __str__(self):
        return self.title


class DetailedInfo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField()
    additional_details = models.TextField()

    def __str__(self):
        return self.description[:50]
