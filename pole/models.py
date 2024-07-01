from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20)


class PoleTable(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qeustion = models.TextField()

class PoleHaveOptions(models.Model):
    user_option = models.ForeignKey(PoleTable,on_delete=models.CASCADE,null=True)
    option = models.CharField(max_length=50)
    

class Vote(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_question = models.ForeignKey(PoleTable, on_delete=models.CASCADE, null=True)
    user_option = models.ForeignKey(PoleHaveOptions, on_delete=models.CASCADE)