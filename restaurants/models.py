import uuid
from django.db import models

class Restaurant(models.Model):
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False)
    logo = models.ImageField(upload_to='restaurants')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    