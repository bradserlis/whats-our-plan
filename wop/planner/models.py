from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Activity(models.Model):
#     pub_date = models.DateTimeField('date published')
#     title= models.CharField(max_length=50)
#     description = models.TextField()
#     group = models.ManyToManyField(Group, on_delete=models.CASCADE, through="")


# want most recent activity on top

    # def __str__(self):
    #     return self.title

    # class Meta:
    #     ordering = ('title',)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField('Group', blank=False)

class Group(models.Model):
    name= models.CharField(max_length=50)
    description = models.TextField()
    # activity = models.ManyToManyField(Activity, on_delete=models.CASCADE)
    users = models.ManyToManyField('Profile', blank=False)

    def __str__(self):
        return self.name


# another claass

# class User_Group(models.Model):
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     group = models.ManyToManyField(Group)

# class Activity_Group(models.Model):
#     group = models.ManyToManyField(Group, on_delete=models.CASCADE)
#     activity = models.ManyToManyField(Activity, on_delete=models.CASCADE)
