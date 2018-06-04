from django.db import models

# Create your models here.

class Activity(models.Model):
    pub_date = models.DateTimeField('date published')
    title= models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Group(models.Model):
    name= models.CharField(max_length=50)
    description = models.TextField()
    activity = models.ManyToManyField(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
