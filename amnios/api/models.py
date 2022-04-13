from django.db import models
# Create your models here.


class Agency(models.Model):
    name = models.TextField()
    address = models.TextField()


class Seller(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField()
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)


class Buyer(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)


class EstateAgent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)


class Estate(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.TextField()
    price = models.IntegerField()
    date_added = models.DateField()
    date_available = models.DateField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)


class VisitSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    enable = models.BooleanField()
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(
        EstateAgent, on_delete=models.SET_NULL, null=True)
