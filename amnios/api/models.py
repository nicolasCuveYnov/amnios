from django.db import models
# Create your models here.


class Agency(models.Model):
    name = models.TextField()
    address = models.TextField()


class Seller(models.Model):
    name = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=10)
    emailAdress = models.EmailField()
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)


class Buyer(models.Model):
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=10)


class EstateAgent(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=10)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)


class Estate(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.TextField()
    price = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    date_dispo = models.DateField()
    agency=models.ForeignKey(Agency, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)


class VisitSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    enable = models.BooleanField()
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(
        EstateAgent, on_delete=models.SET_NULL, null=True)
