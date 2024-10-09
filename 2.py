#Yes, Django signals run in the same thread as the caller by default. To verify this, 
# I'll show the thread name in both the caller function and the signal handler.

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import Customer

@receiver(post_save, sender=Customer)
def customer_created_handler(sender, instance, created, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")

def create_customer():
    print(f"Caller thread: {threading.current_thread().name}")
    customer = Customer.objects.create(name='testcustomer')

# This will print the same thread name for both the caller and the signal.

#When you run create_customer(), both the caller and the signal will print the same thread name,
#confirming that they run in the same thread.
