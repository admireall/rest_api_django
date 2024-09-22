from django.db import models

# Create your models here.
class movie_data(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    duration=models.FloatField()
    rating=models.FloatField()
    typ=models.CharField(max_length=200,default='action')
    img=models.ImageField(upload_to='Images/',default='Images/None/Noimg.jpg')