from django.db import models
from datetime import datetime
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/photos/{1}'.format(instance.title, filename)

class Event(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to=user_directory_path,blank=False)
    photo_1 = models.ImageField(upload_to=user_directory_path,blank=True)
    photo_2 = models.ImageField(upload_to=user_directory_path,blank=True)
    photo_3 = models.ImageField(upload_to=user_directory_path,blank=True)
    is_published = models.BooleanField(default=True)
    event_date = models.DateField(default=datetime.today,blank=False)
    start_time = models.TimeField(default=datetime.now,blank=False)
    end_time = models.TimeField(default=datetime.now,blank=False)

    def __str__(self):
        return self.title