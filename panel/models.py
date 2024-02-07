from django.db import models
# from django.forms import ModelForm
# from webapp.models import enter,petacatgory

# Create your models here.
# class cart(models.Model):
#     user = models.ForeignKey(enter,on_delete=models.CASCADE,default="")
#     product = models.ForeignKey(petacatgory,on_delete=models.CASCADE,default="")
#     qty = models.IntegerField(default=0,max_length=200)
#     price = models.IntegerField(max_length=500)
#     amount = models.IntegerField(max_length=500)
# class cartForm(ModelForm):
#     class Meta:
#         model = cart
#         fields = ["user","product","qty","price","amount"]