from django.db import models

# Create your models here.



class Users(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    user_id = models.CharField(max_length=10,unique=True)
    language = models.CharField(max_length=10,null=True,blank=True)
    

    def __str__(self):
        return self.first_name
    


class CV(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    personal_data = models.TextField()
    education = models.TextField(null=True,blank=True)
    skills = models.TextField(null=True,blank=True)
    experience = models.TextField(null=True,blank=True)
    languages = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.user.first_name



class AdminT(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name
    

class Channel(models.Model):
    name = models.CharField(max_length=200)
    channel_id = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name



class UserPersonalInfo(models.Model):
    user_id = models.CharField(max_length=10,unique=True,null=True,blank=True)
    name = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    tel = models.CharField(max_length=20)
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    addres = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name
    



class UserEducation(models.Model):
    user_id = models.CharField(max_length=10,null=True,blank=True)
    name = models.CharField(max_length=250)
    diskreption = models.TextField()
    date = models.CharField(max_length=200)


    def __str__(self):
        return self.user.first_name



class Skill(models.Model):
    user_id = models.CharField(max_length=10,unique=True,null=True,blank=True)
    name = models.TextField()


    def __str__(self):
        return self.user.first_name
    

class WorkExperience(models.Model):
    user_id = models.CharField(max_length=10,unique=True,null=True,blank=True)
    name = models.CharField(max_length=250)
    title = models.TextField()
    body = models.TextField()
    date = models.CharField(max_length=250)

    def __str__(self):
        return self.user.first_name
    
class LanguageCv(models.Model):
    #user = models.ForeignKey(Users, on_delete=models.CASCADE ,null=True, blank=True)
    name = models.TextField()
    user_id = models.CharField(max_length=10,unique=True,null=True,blank=True)

    def __str__(self):
        return self.name

    
