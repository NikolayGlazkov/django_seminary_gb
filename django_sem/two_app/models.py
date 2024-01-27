from django.db import models


class Counter(models.Model):
    result = models.CharField(max_length=10)
    flip_time = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    ferst_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    biograpt = models.TextField()
    birthday = models.DateField()
    fullname = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.ferst_name} {self.last_name}"
    def __str__(self) -> str:
        return f"{self.fullname}, {self.birthday}"
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    reliz_date = models.TimeField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_counter = models.IntegerField(default=0)
    status = models.CharField(max_length=100)
