from django.db import models

class Form(models.Model):
    Name = models.CharField(max_length=64) 
    FatherName = models.CharField(max_length=64, blank=True, null=True)  
    GuardianName = models.CharField(max_length=64, blank=True, null=True)  
    MotherName = models.CharField(max_length=64)  
    DateofBirth = models.DateField()
    class1 = models.CharField(max_length=64)  
    SubjectName = models.CharField(max_length=256) 
    School = models.CharField(max_length=256)  
    Board = models.CharField(max_length=64) 
    Address = models.TextField()  
    ContactNo = models.CharField(max_length=15)  
    Email = models.EmailField()
    DateofJoining = models.DateField()
    AgreeToDeclaration = models.BooleanField(default=False)

    def __str__(self):
        return self.Name