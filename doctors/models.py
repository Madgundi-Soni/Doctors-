from django.db import models
from user_details.models import User

# Create your models here.

class Categories(models.Model): 
    name = models.CharField(max_length=50 , null=True , blank=True)

    # def __str__(self):
    #     return self.name


class Blogs(models.Model):  
    title = models.CharField(max_length=50 , null=True , blank=True)
    image = models.ImageField(default='default.jpg', upload_to='blog_posts', null=True , blank=True)
    summary = models.TextField( null=True , blank=True)
    content = models.TextField(null=True , blank=True)
    categories = models.ForeignKey(Categories ,on_delete=models.CASCADE,null=True,blank=True)
    is_draft=models.BooleanField(default=False)
    user = models.ForeignKey(User ,on_delete=models.CASCADE,null=True,blank=True)


    # def __str__(self):
    #     return self.title