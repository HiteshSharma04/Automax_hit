import uuid
from django.db import models
from .cars import BRANDS, TRANSMISSION
from users.models import profile, Location
from .utils import usr_listing_path
# Create your models here.
class Listing(models.Model):
    models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False 
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now =True)
    seller = models.ForeignKey(profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=24, choices=BRANDS, default=None)
    model = models.CharField(max_length=64,)
    vin = models.CharField(max_length=24,)
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=24, )
    description = models.TextField()
    engine = models.CharField(max_length=24,)
    transmission = models.CharField(max_length=24, choices = TRANSMISSION, default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=usr_listing_path)

    def __str__(self):
        return f'{self.seller.user.username}\"s Listing -{self.model}'

class LikedListing(models.Model):
    profile = models.ForeignKey(profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.listing.model} listing liked by {self.profile.user.username}'
