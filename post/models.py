from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = RichTextField()
    is_published = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)

# only logged in users can like posts
# once a post is liked, it is saved to the users liked posts list 

