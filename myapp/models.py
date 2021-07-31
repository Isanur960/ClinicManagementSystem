from django.db import models

# Create your models here.
class PatientDB(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    disease = models.TextField(max_length=1000)
    doctorName = models.CharField(max_length=50)
    doctorFees = models.IntegerField(default=500)
    startMedsDate = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
