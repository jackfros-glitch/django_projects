from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

# Create your models here.
class Ads(models.Model):
    title = models.CharField(max_length=200, validators =[MinLengthValidator(
        2, "Title must be greater than 2 characters")])
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(null=True, max_length=256, help_text="The MIMEType of the file")
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title