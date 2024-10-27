from django.db import models
from django.contrib.auth import get_user_model
import uuid #generates unique id for each post
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
#profile model
#in build user model gives us username,pass1,pass2,email,etc
#we wanted to add more fields so we create profile model , and link User model with a foreign key

User = get_user_model()





class Profile(models.Model):
    DEPARTMENT_CHOICES = [
        ('IT', 'IT'),
        ('CSE', 'CSE'),
        ('CSD', 'CSD'),
        ('AIML', 'AIML'),
        ('MECH', 'MECH'),
        ('CIVIL', 'CIVIL'),
        ('EEE', 'EEE'),
        ('ECE', 'ECE'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)  # linked User model using foreginKey
    id_user = models.IntegerField()
    profile_img =models.ImageField(upload_to='profile_images' , default= 'profile_images/default_profileimg.jpg')  #here the profile_imgs will be added in profile_images folder inside Media
    points  = 0
    branch = models.CharField(max_length=50,choices=DEPARTMENT_CHOICES,default='CSE')
    overall_ranking = 0
    dept_ranking = 0

    def __str__(self):
        return self.user.username
    #in signup we r using name . insted of creating seperate column for name we using username , ab=nf we specify every diff acc with email

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
  
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} likes {self.post.id}'
