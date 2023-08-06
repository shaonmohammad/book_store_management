from django.db import models

# Create your models here.
CATAGORY = (
    ('mystry', 'Mystry'),
    ('Threler', 'Threler'),
    ('Hamour', 'Hamour'),
    ('Horror', 'Horror'),

)


class BookModels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    catagory = models.CharField(max_length=20, choices=CATAGORY)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Name:{self.name}"
