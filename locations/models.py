import secrets
import string

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from users.models import CustomUser
from .utils.enum_category import EnumCategoryLayer1, EnumCategoryLayer2


class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")

    def __str__(self):
        return self.name


class Location(models.Model):
    title = models.CharField(max_length=200)
    category_layer1 = models.CharField(
        max_length=200, choices=EnumCategoryLayer1.choices()
    )
    category_layer2 = models.CharField(
        max_length=200, choices=EnumCategoryLayer2.choices()
    )
    address = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
    rent = models.IntegerField(blank=True, null=True)

    uid = models.CharField(max_length=7, unique=True, editable=False)

    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    state = models.ForeignKey(to=State, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


@receiver(pre_save, sender=Location)
def generate_unique_id(sender, instance, **kwargs):
    characters = string.ascii_letters + string.digits
    unique_id = "".join(secrets.choice(characters) for _ in range(7))
    instance.uid = unique_id
