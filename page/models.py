from random import randint
from django.db import models

def dobl(*lis):
    ret=[]
    for i in lis:
        ret.append((i,i))
    return tuple(ret)

class KafshModel(models.Model):
    model=models.CharField(max_length=200)
    price=models.IntegerField()
    size=models.FloatField()
    color=models.CharField(max_length=30,choices=dobl('blabk','white','red','blue','yellow','green','pink','purple','gray','orange'))
    takhfif=models.CharField(max_length=16,choices=dobl('No takhfif','5%','10%','15%','20%','25%','30%','40%','50%','60%','70%'))
    n=models.IntegerField()
    img=models.ImageField()

    def __str__(self):
        return f"Kafsh {self.model} {self.size}"

class VIP(models.Model):
    title=models.CharField(max_length=200)
    kafsh1=models.ForeignKey(KafshModel, on_delete=models.CASCADE, related_name="k1")
    kafsh2=models.ForeignKey(KafshModel, on_delete=models.CASCADE, related_name="k2")
    kafsh3=models.ForeignKey(KafshModel, on_delete=models.CASCADE, related_name="k3")
    kafsh4=models.ForeignKey(KafshModel, on_delete=models.CASCADE, related_name="k4")
    kafsh5=models.ForeignKey(KafshModel, on_delete=models.CASCADE, related_name="k5")

class UserModel(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    sabad=models.TextField(default="[]")
    macs=models.TextField(default='[]')

    def __str__(self):
        return self.username
    
class ADModel(models.Model):
    title=models.CharField(max_length=500)
    link=models.CharField(max_length=1000)
    text=models.TextField()

    def __str__(self):
        return self.title