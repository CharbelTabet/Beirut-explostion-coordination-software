from django.db import models

class LatLng(models.Model):
    lat = models.DecimalField(max_digits=17, decimal_places=15, verbose_name="Location's latitude")
    lng = models.DecimalField(max_digits=17, decimal_places=15, verbose_name="Location's Longitude")
    address = models.CharField(max_length=50, verbose_name="Short Address")

class pin(LatLng):
    choices = [
        ('food', 'Food'),
        ('construction', 'Construction'),
        ('ngo', 'Ngo headquarter'),
        ('danger', 'Danger'),
        ('red cross', 'Red Cross'),
    ]
    kind = models.CharField(max_length=50, choices=choices)    
    def __str__(self):
        return self.address

class area(LatLng):
    choices = [
        (100, '100 - Small'),
        (500, '500 - Medium'),
        (1000, '1000 - Important')
    ]
    radius = models.IntegerField(choices=choices)
    def __str__(self):
        return self.address

class position(LatLng):
    choices = [
        ('food', 'Food'),
        ('construction', 'Construction'),
        ('ngo', 'Ngo headquarter'),
        ('danger', 'Danger'),
        ('red cross', 'Red Cross'),
    ]
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=50, choices=choices)
    description = models.TextField(max_length=100)
    contact = models.CharField(max_length=12)

class damage(LatLng):
    choices = [
        ('light', 'Light Damage'),
        ('moderate', 'Moderate Damage'),
        ('heavy', 'Heavy Damage')
    ]
    description = models.TextField(max_length=100)
    contact = models.CharField(max_length=12)
    level = models.CharField(max_length=50, choices=choices, verbose_name='Damage\'s level')
