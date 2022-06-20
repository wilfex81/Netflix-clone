import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

AGE_CHOICES=(
    ('All','All'),
    ('Kids','Kids')
)

MOVIE_TYPE=(
    ('single','Single'),
    ('seasonal','Seasonal')
)

'''This user with whom the account belongs to'''
class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile')

        
'''Extra profiles created by the user(can be for family or friends'''
class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)

    def __str__(self):
        return self.name

'''This class belongs to the Movies that will be uploaded to the database
and rendered in the templates(frontend)'''

class Movie(models.Model):
    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES,blank=True,null=True)


    def __str__(self):
        return self.title
        
'''This class will hold individual movie file'''
class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')

    def __str__(self):
        return self.title
