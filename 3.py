'''Yes, Django signals run in the same database transaction as the caller. This means that if the transaction is rolled back, 
any actions triggered by the signal will also be rolled back.'''

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import Customer

@receiver(post_save, sender=Customer)
def customer_created_handler(sender, instance, created, **kwargs):
    if created:
        print("Signal triggered. Customer created.")

def create_customer_in_transaction():
    try:
        with transaction.atomic():
            customer = Customer.objects.create(name='testcustomer')
            raise Exception("Simulating an error to rollback the transaction.")
    except Exception as e:
        print("Transaction rolled back. Signal changes discarded.")
