from django.contrib import admin
from home.models import Product
from home.models import Contact,Review,Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(Category)
