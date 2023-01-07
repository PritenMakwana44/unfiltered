from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

categories_choices = (
    ('Sports'),
    ('News'),
    ('Social'),
    ('World'),
    ('History'),
    ('Spiritual'),
    ('Other'),
)

class Post (models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE, related_name="newsfeed_posts")
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    upvotes = models.ManyToManyField(User, related_name='post_upvotes', blank=True)
    downvotes = models.ManyToManyField(User(), related_name='post_downvotes', blank=True)
    Category_group = models.ForeignKey(categories_choices, related_name='category_group')

class Meta:
    ordering = ['-created_on']

def __str__(self):
    return self.title

def number_of_upvotes(self):
    return self.upvotes.count()

def number_of_downvotes(self):
    return self.downvotes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    Categories = models.CharField(max_length=7, choices=catagories_choices)



