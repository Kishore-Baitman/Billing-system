from django.contrib import admin
from .models import Category,Customer,Billing,Product,stock,Sales
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Billing)
admin.site.register(Product)
admin.site.register(stock)
admin.site.register(Sales)
