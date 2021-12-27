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
    comment = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment', related_name="ads_comments")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Fav', related_name="favorite_ads")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(MinLengthValidator(3, "Comment must be greater than 3 characters"))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ads, on_delete=models.CASCADE, related_name="%(class)s_ads")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.text) < 15 : return self.text
        return self.text[:11] + "..."

class Fav(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ads, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'ad')

    def __str__(self):
        return '%s likes %s'%(self.user.username, self.ad.title[:10])
