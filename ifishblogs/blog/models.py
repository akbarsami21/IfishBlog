from django.db import models
from django.utils.html import format_html
# Create your models here.

#create catagroy table
class Category(models.Model):
    catId=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='catagory/')
    addDate=models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="height:60px; width:60px; border-radius:50%;">'.format(self.image))

    def __str__(self):
        return self.title
    

#create post table
class Post(models.Model):
    postId=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post/')
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    addDate=models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="height:50px;width:50px; border-radius:50%;>"'.format(self.image))
    
    def __str__(self):
        return self.title
