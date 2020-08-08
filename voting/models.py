from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Voters(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name = 'voter', on_delete = models.CASCADE)
  voted = models.BooleanField(default=False)
  posit = models.CharField(max_length = 100, blank = True)
  
  def __str__(self):
    return self.user.username
  
class Position(models.Model):
  name = models.CharField(max_length = 200)
  votes = models.IntegerField(default = 0)
  percentage = models.IntegerField(default = 0)
  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('vote',  args=[self.id])