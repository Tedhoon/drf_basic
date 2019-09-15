from .models import Essay , Album , Files
from rest_framework import serializers


class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('id' , 'title' , 'body' , 'author_name')



class AlbumSerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url = True)
    class Meta:
        model = Album
        fields = ('id', 'image' , 'desc' , 'author_name')


class FilesSerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Files
        fields = ('id' , 'myfile' , 'desc' , 'author_name')