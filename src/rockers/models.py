from django.db import models
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
            verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Text of an article")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", 
            verbose_name="Photo")
    time_create = models.DateTimeField(auto_now_add=True,
            verbose_name="Time of creation")
    time_update = models.DateTimeField(auto_now=True,
            verbose_name="Time of modification")
    is_published = models.BooleanField(default=True, 
            verbose_name="Is publicated")
    role = models.ForeignKey('Role', on_delete=models.PROTECT,
            verbose_name="Role")

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # unique route to element
        # name of urlpattern, {name_of_param: what I want to get}
        return reverse('post', kwargs={'post_id': self.pk}) 

    class Meta:
        verbose_name = 'Rocker'
        verbose_name_plural = 'Rockers'
        ordering = ['-time_create', 'name']


class Role(models.Model):
    activity = models.CharField(max_length=100, db_index=True,
            verbose_name="Role")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
            verbose_name="URL")

    def __str__(self):
        return self.activity

    def get_absolute_url(self):
        return reverse('role', kwargs={'role_id': self.pk})

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
        ordering = ['id']
