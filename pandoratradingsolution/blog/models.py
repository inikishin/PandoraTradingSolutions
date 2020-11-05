from django.db import models

class Category(models.Model):
    short_name = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=150)
    description = models.TextField()
    is_show = models.BooleanField(default=True)

    def __str__(self):
        return self.short_name

class Post(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    header = models.CharField(max_length=150)
    image_url = models.TextField()
    slug = models.SlugField()
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_published = models.DateField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
