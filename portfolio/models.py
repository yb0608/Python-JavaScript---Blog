from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Category (models.Model):
    category = models.CharField(max_length=255, unique = True)

    def __str__(self):
        return f'{self.category}'
    
    def get_absolute_url (self):
        return reverse('share')


class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null = True, upload_to = "images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    content = RichTextField(blank = True, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255,default = 'Landscape Architecture')
    likes = models.ManyToManyField(User, related_name="likers")
    summary = models.CharField(max_length=255,blank = True, null = True)

    def __str__(self):
        return f'{self.title} - {self.author}'

    def get_absolute_url (self):
        return reverse('detail', args=(str(self.id)))
       
        
class Comment (models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project} - {self.commenter}'