from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def validate(self, data):
        current_year = int(date.year)
        if Book.publication_year>current_year:
            raise serializers.ValidationError('The entered "Publication Year is in the future"')
        return data
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name','books']
