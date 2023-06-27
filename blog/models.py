from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Sarlavha')
    description = models.TextField(verbose_name="Mazmuni", unique=True)
    photo = models.ImageField(upload_to='news/', null=True, blank=True, verbose_name='Rasm')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    publish = models.BooleanField(default=True, verbose_name="Nashr etilganligi")

    def __str__(self):
        return self.title

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return '-'
