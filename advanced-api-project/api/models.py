from django.db import models

# Create your models here.
class Author(models.Model):
    ''' This Model defines Author model with on attribute'''
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    '''this model defines book'''
    title = models.CharField(max_length=100)
    publication_year = models.BigIntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title