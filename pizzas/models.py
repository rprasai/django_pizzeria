from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images',blank=True) # getdate
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): #Return String Representation of the Model
        return self.name


class Topping(models.Model):
    #things that goes on pizza
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE) 
    #pizza: foreign Key instance
    #delete cascade: when pizza is del all topping is deleted

    name = models.TextField()
    #textfield: doesn't need size limit
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: #holds extra info for managing a model and set special attributes
        verbose_name_plural = 'toppings'

    def __str__(self): #--str-- tells which info to show, here we specify to show only 1st 50 char
        return f"{self.name[:50]}..."
