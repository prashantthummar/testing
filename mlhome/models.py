from django.db import models

# Create your models here.

LANGUAGE_TYPE = (
    ('English','English'),
    ('Hindi','Hindi'),
    ('Gujarati','Gujarati'),
)


COMMUNICATION_TYPE = (
    ('Email','Email'),
    ('SMS','SMS'),
    ('Phone','Phone'),
)


class UserAdd(models.Model):

    avatar = models.ImageField(upload_to='pics')
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    companyName = models.CharField(max_length=50)
    contactPhone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    companySite = models.CharField(max_length=50)
    
    language = models.CharField(max_length=50)
    timeZone = models.CharField(max_length=50)
    communication = models.CharField(max_length=50)
    passwordRV = models.BooleanField(default=False) # Password Reset Verification

    address1 = models.TextField() 
    address2 = models.TextField() 
    postcode = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName + ' ' + self.lastName