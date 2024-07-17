from django.db import models

# Create your models here.

class team(models.Model):
    team_name = models.CharField(max_length=30)

    def __str__(self):
        return self.team_name

class person(models.Model):
    team = models.ForeignKey(team,on_delete=models.CASCADE,null=True,blank=True,related_name='members',default=None)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    place = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
