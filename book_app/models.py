from django.db import models

#작가 모델
class Author(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'authors'

# 책 모델
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author_id")
    title = models.CharField(max_length=200)    
    price = models.DecimalField(max_digits=100, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'books'