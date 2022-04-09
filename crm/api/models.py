from django.db import models



# Create your models here.


class Leads (models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    jobPosition = models.CharField(max_length=30)
    mobileNumber = models.CharField(max_length=30)


    def __str__(self) :
        return f"{self.firstName},  {self.lastName}"

        #{self.email}, {self.phoneNumber}, {self.company} ,{self.jobPosition},{self.mobileNumber}