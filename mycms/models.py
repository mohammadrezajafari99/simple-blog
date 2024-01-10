from django.db import models
import uuid
from profiles.models import UserProfile


class Post(models.Model):
    writer=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200)
    body=models.TextField()
    post_id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    slug=models.SlugField()
    image=models.ImageField(upload_to='image/')
    category=models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True)
    
    
    def __str__(self) :
        return self.title



class Category(models.Model):
    title=models.CharField(max_length=100)
    category_id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    slug=models.SlugField()

    def __str__(self) :
        return self.title