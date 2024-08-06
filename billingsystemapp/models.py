from django.db import models,IntegrityError
import uuid
from datetime import date,timedelta
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    quantity = models.IntegerField()
    manufacturingdate = models.DateField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name
    from datetime import date

    def update_discount(self):
        if self.manufacturingdate:
        # Calculate the number of months since the manufacturing date
            months_old = (date.today().year - self.manufacturingdate.year) * 12 + date.today().month - self.manufacturingdate.month

        # If the product is within the first 6 months, set discount to 0
            if months_old < 6:
                self.discount = 0.00
            else:
            # Calculate six-month periods
                six_month_periods = (months_old - 6) // 6

            # Define starting discounts based on category
                starting_discounts = {
                    12: 5.00,  # Example category ID mappings
                    13: 10.00,
                    14: 15.00,
                    15: 8.00,
                    16: 12.00,
                    17: 7.00,
                }
                starting_discount = starting_discounts.get(self.category_id, 0.00)

            # Calculate total discount with increment
                total_discount = starting_discount + (six_month_periods * 5.00)
            
            # Ensure total discount does not exceed 90%
                if total_discount > 90.00:
                    total_discount = 90.00

                self.discount = total_discount
        
            self.save()


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    purchase_date = models.DateField()

    def __str__(self):
        return str(self.customer_name)

class Sales(models.Model):
    sales_id = models.AutoField(primary_key=True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.sales_id)
    
class Billing(models.Model):
    id = models.AutoField(primary_key=True)
    sale_number = models.UUIDField(default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchasetime = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('sale_number', 'product_id')
    def __str__(self):
        return str(self.sale_number)

class stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock =models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return str(self.stock_id)

