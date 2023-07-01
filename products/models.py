from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Product(models.Model):

    class Meta:

        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.URLField(max_length=255)
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, related_name='products')
    description = models.TextField()