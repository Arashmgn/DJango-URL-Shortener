from datetime import datetime, timedelta
import string
from django.utils import timezone
from django.db import models

# Create your models here.
def return_date_time():
    now = timezone.now()
    return now + timedelta(days=2)

class url(models.Model):
    short_url= models.CharField(max_length = 4)
    long_url = models.CharField(max_length = 500)
    created = models.DateField(default=datetime.now)
    expiration = models.DateField(default=return_date_time)
    
    

    


    