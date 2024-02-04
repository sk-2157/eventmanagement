from django.db import models
from datetime import datetime

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/participants/{1}'.format(instance.event, filename)

class Participant(models.Model):
    event = models.CharField(max_length=200)
    event_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    participated_date = models.DateField(default=datetime.now)
    user_id = models.IntegerField(blank=True)
    p_photo = models.ImageField(upload_to=user_directory_path,blank=False)

    def __str__(self):
        return self.name

