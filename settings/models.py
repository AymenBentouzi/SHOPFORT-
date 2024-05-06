from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Brand(models.Model):
    BRDName = models.CharField(max_length=40, unique=True)
    BRDDescription = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.BRDName


class Variant(models.Model):
    VRTName = models.CharField(max_length=40, unique=True)
    VRTDescription = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = _('Variant')
        verbose_name_plural = _('Variants')
    
    def __str__(self):
        return self.VRTName
