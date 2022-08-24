from django.db import models

class Bus(models.Model):
    bus_num = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
    	return f"버스번호 : {self.bus_num}"
