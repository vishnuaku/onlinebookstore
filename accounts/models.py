from django.db import models

# Create your models here.
class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    #book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name