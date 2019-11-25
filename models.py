from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=50 ,null= True)
    publication_date = models.DateField(null=True ,blank= True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES ,null = True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False ,null = True)
