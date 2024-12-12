from django.db import models
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(default=now)  # Ensure this line exists

    def __str__(self):
        return self.title