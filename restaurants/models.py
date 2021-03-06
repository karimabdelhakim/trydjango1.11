from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from .utils import unique_slug_generator
from django.dispatch import receiver
from .validators import validate_category


User = settings.AUTH_USER_MODEL

class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User) #user_instance.restaurantlocation_set.all()
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(
        max_length=120, null=True, blank=True, validators=[validate_category]
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


#signal with decorator which is cleaner
@receiver(pre_save, sender=RestaurantLocation)
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.category:
        instance.category = instance.category.capitalize()

    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


#signal the normal way

# def rl_pre_save_receiver(sender, instance, *args, **kwargs):
#     print('saving...')
#     print(instance.timestamp)
#     print(sender)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)

# pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)






# def rl_post_save_receiver(sender, instance,created, *args, **kwargs):
#     print('saving...')
#     print(instance.timestamp)
#     print(sender)


# post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)
