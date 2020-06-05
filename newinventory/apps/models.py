from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    choice = (
        ('available','available'),
        ('comingsoon','comingsoon'),
        ('sold','sold')
    )
    condition = models.CharField(max_length=20, choices=choice, default='available')
    issues = models.CharField(max_length=20, default='good')

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name

    
    

class Desktop(Device):
    class Meta:
        verbose_name_plural = "desktop"
    pass

class Laptop(Device):
    class Meta:
        verbose_name_plural = "laptop"
    pass

class Mobile(Device):
    class Meta:
        verbose_name_plural = "mobile"
    pass