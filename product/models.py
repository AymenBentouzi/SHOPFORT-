from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Category Name'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name=_('Parent Category'), limit_choices_to={'parent': None})
    description = models.TextField(blank=True, verbose_name=_('Category Description'))
    image = models.ImageField(upload_to='category/', verbose_name=_('Category Image'), default='path/to/default_category_image.jpg')

    def __str__(self):
        return self.name

    
class Cost(models.Model):
    amount = models.DecimalField(_("Amount"), max_digits=6, decimal_places=2, default=0)

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Product Name'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Product Category'))
    brand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Brand'))
    description = models.TextField(blank=True, verbose_name=_('Product Description'))
    price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(_("Image"), upload_to='products/', null=True, blank=True, default='products/default.png')
    cost = models.ForeignKey(Cost, verbose_name=_("Cost"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __str__(self):
        return self.name

    
    
class Product_Alternatives(models.Model):
    PALNProduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='main_product')
    PALNAlternatives = models.ManyToManyField(Product , related_name='alternatives_product')
    
    
    
    
class Product_Accessories(models.Model):
    main_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='accessories', verbose_name=_('Main Product'))
    accessory_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Accessory Product'))

    def __str__(self):
        return f"{self.main_product.name} - {self.accessory_product.name}"
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"), related_name='images')
    image = models.ImageField(upload_to='product_images/', verbose_name=_("Image"))
    

    def __str__(self):
        return f"{self.product.name} - {self.id}"
