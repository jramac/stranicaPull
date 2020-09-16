from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField



class Post(models.Model):

    title = models.CharField(max_length=100)

    content = RichTextField(blank=True, null=True)

    #content = models.TextField()

    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    thumbBroj = models.IntegerField(default=0)



    def __str__(self):

        return self.title



class PostImage(models.Model):

    post = models.ForeignKey(Post, default=None, on_delete = models.CASCADE,null=True)

    image = models.ImageField(upload_to='images/',blank=True,default='images/default.jpg')

    def __str__(self):

        return self.post.title