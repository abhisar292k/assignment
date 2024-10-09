"Django signals are executed synchronously by default. This means the signal handler is executed in the same process"
"and blocks the flow until it completes. Here's a code snippet to demonstrate this behavior:"

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import Customer  # Using a custom model

@receiver(post_save, sender=Customer)
def customer_created_handler(sender, instance, created, **kwargs):
    if created:
        print("Signal received. Starting sleep...")
        time.sleep(5)
        print("Signal processed after 5 seconds.")

"Since the signal handler uses time.sleep(5), the program will pause for 5 seconds before continuing,"
"showing that the signal is processed synchronously."


#I start by importing the necessary modules.
#time is used to introduce a delay, which helps demonstrate synchronous behavior.
#post_save and receiver are part of Django’s signal framework, which allows us to execute code in response to certain events—in this case, when a Customer instance is saved.
#I also import the Customer model from myapp.models, which is the model I’m working with.
#Signal Receiver:
'''The @receiver(post_save, sender=Customer) decorator sets up a signal receiver. This means that whenever a new Customer instance is saved to the database, the function customer_created_handler is automatically triggered.
Handler Function:'''

'''Inside the function, I check if a new instance was created using the created parameter. If it’s True, it means we have a new Customer.
I then print "Signal received. Starting sleep..." to indicate that the signal has been triggered.
The time.sleep(5) line simulates a processing delay of 5 seconds. This shows that the signal is being handled synchronously—meaning the execution pauses here until the sleep is finished.
Finally, I print "Signal processed after 5 seconds." This indicates that the signal handling is complete.'''