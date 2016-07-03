from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    donor=models.CharField(max_length=200, blank=True)
    photo=models.ImageField(upload_to='static/items', default='static/items/book_generic.png')
    
    def take(self,newDonor):
        self.donor=newDonor
        self.save()
        
    def __str__(self):
        return self.title
        