from django.core.management.base import BaseCommand
from decimal import Decimal
from billingsystemapp.models import Product, stock
import random

class Command(BaseCommand):
    help = 'Populate the stock model with data from the product model with adjustments'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()

        for product in products:
            # Adjust the stock and price values
            stock_quantity = product.quantity + random.randint(1, 10)  # Slightly higher than product quantity
            discount_percentage = Decimal(random.uniform(0.05, 0.15))  # Convert float to Decimal
            discounted_price = product.price - (product.price * discount_percentage)  # Safe operation with Decimals

            # Create a stock entry
            stock_entry, created = stock.objects.get_or_create(
                product_name=product,
                category=product.category,
                defaults={
                    'stock': stock_quantity,
                    'price': round(discounted_price, 2)  # Ensure price is rounded to two decimal places
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Stock for {product.product_name} created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Stock for {product.product_name} already exists.'))

        self.stdout.write(self.style.SUCCESS('Stock population complete.'))
