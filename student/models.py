from django.db import models

CHOICES=[
    ("python","python"),
    ("java","java"),
    ("c++","c++"),
    ("ruby","ruby"),
    (".net",".net"),
    ("java script","java script")
]

class studentmodel(models.Model):
    
    
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    phone_number=models.IntegerField(default=0)
    branch=models.CharField(max_length=30,choices= CHOICES)


    def __str__(self):

        return self.first_name+" "+self.last_name

