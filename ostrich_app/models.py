from django.db import models


class OstrichBreeders(models.Model):
    name = models.CharField(max_length=64, unique=True)
    birth_year = models.IntegerField()
    sex = models.IntegerField(choices=((1, 'female'), (2, 'male')))
    description = models.TextField(null=True)
    is_alive = models.BooleanField(default=True)


class EggsBabies(models.Model):
    number = models.IntegerField()
    date_found = models.DateField()
    date_incubated = models.DateField()
    sex = models.IntegerField(choices=((1, 'female'), (2, 'male')), null=True)
    description = models.TextField(null=True)
    is_hatched = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    is_alive = models.BooleanField(default=True)
    father = models.ForeignKey(OstrichBreeders, null=True, related_name='father')
    mother = models.ForeignKey(OstrichBreeders, null=True, related_name='mother')


class FoodReserves(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.FloatField()
    price = models.FloatField()
    more_info = models.CharField(max_length=1024)


class SoldBirds(models.Model):
    date = models.DateField()
    quantity = models.IntegerField()
    avg_weight = models.FloatField()


class Budget(models.Model):
    name = models.CharField(max_length=200)
    amount = models.FloatField()
    revenue = models.BooleanField(default=False)


class Season(models.Model):
    name = models.CharField(max_length=128)
    date_from = models.DateField()
    date_to = models.DateField()
