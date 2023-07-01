from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _

class CompanyTypes(models.Choices):
    MARKET = 'Market'
    RESTAURANT = 'Restaurant'
    PHARMACY = 'Pharmacy'
    FLOWERS = 'Flowers'
    OTHER = 'Other'


# Create your models here.
class Company(models.Model):

    class Meta:
        db_table = 'company'
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=CompanyTypes.choices)
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=30)
    logo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.address} {self.tel}"