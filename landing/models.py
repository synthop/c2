from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()

    def __str__(self):
        return '%s (%s)' % (self.name, self.email)
