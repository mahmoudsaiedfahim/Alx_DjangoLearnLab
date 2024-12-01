from rest_framework import serializers
from .models import Author, Book
from datetime import date

class AuthorSerializer(serializers.ModelSerializer):
    #books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id','title','publication_year','author']
    def validate_publication_year(self, value):
        current_year = int(date.today().year)
        if value>current_year:
            raise serializers.ValidationError('The entered "Publication Year is in the future"')
        return value
    

