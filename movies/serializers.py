from rest_framework import serializers
from .models import movie_data

class movie_serializer(serializers.ModelSerializer):
    img=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=movie_data
        fields=['id','name','duration','rating','typ','img']