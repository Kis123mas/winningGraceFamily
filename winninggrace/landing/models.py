from django.db import models



# model for contact form from landing page
class Contact(models.Model):
    name = models.CharField(max_length=155, null=True, blank=True)
    email = models.EmailField(max_length=155, null=True, blank=True)
    subject = models.CharField(max_length=155, null=True, blank=True)
    message = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + ' | ' + str(self.subject)