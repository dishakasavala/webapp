from django.db import models
from django.forms import ModelForm

# Create your models here.
class enter(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    contact = models.BigIntegerField()
class enterForm(ModelForm):
    class Meta:
        model = enter
        fields = ["name","email","password","contact"]

class slider(models.Model):
    Title = models.CharField(max_length=100)
    Sub_title = models.CharField(max_length=100)
    image = models.FileField(upload_to="media/",default="")
class sliderForm(ModelForm):
    class Meta:
        model = slider
        fields = ["Title","Sub_title","image"]

class maincatagory(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="media/",default="")
class maincatForm(ModelForm):
    class Meta:
        model = maincatagory
        fields = ["name","image"]

class subcatagory(models.Model):
    name = models.CharField(max_length=100)
class subcatForm(ModelForm):
    class Meta:
        model = subcatagory
        fields = ["name"]

class petacatgory(models.Model):
    title = models.CharField(max_length=300)
    catagory = models.ForeignKey(subcatagory,on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.FileField(upload_to="media/",default="")
class petacatForm(ModelForm):
    class Meta:
        model = petacatgory
        fields = ["title","catagory","price","image"]

class cart(models.Model):
    user = models.ForeignKey(enter,on_delete=models.CASCADE,default="")
    product = models.ForeignKey(petacatgory,on_delete=models.CASCADE,default="")
    qty = models.IntegerField(default=0)
    price = models.IntegerField(max_length=500)
    amount = models.IntegerField(max_length=500)
class cartForm(ModelForm):
    class Meta:
        model = cart
        fields = ["user","product","qty","price","amount"]
