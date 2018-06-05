from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField('Group', blank=False)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

class Group(models.Model):
    name= models.CharField(max_length=50)
    description = models.TextField()
    users = models.ManyToManyField('Profile', blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class User_Group(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ManyToManyField(Group)

# class Activity_Group(models.Model):
#     group = models.ManyToManyField(Group, on_delete=models.CASCADE)
#     activity = models.ManyToManyField(Activity, on_delete=models.CASCADE)

class Activity(models.Model):
    # pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=50)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, default=1)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('title',)