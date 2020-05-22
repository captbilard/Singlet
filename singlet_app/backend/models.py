from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    sex = [
    ('Male', 'Male'),
    ('Female', 'Female')
]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    age = models.IntegerField()
    sex = models.CharField(max_length=7, choices=sex)
    profile_pics = models.ImageField(upload_to='profile_pics/%Y/%m/%d', max_length=255, blank=True, null=True)#you need to check more on this field
    bio = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return f'{self.user}'

class Gallery(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='galleries')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="galleries", null=True, blank=True)
    pictures = models.ImageField(upload_to="gallery/%Y/%m/%d", max_length=200, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return f'{self.user} gallery'