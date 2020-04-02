from django.utils.translation import ugettext_lazy as _
from django.db import models
# Create your models here.
from authapp.models import CustomUser

class Profile(CustomUser):
    location = models.CharField(_('location'), max_length = 100,
        help_text = _('Location of User.'), blank = True)
    address = models.CharField(_('address'), max_length = 150,
        help_text = _('Address of User.'), blank = True)
    profile_pic = models.ImageField(_('profile image'), upload_to = 'profile pics', blank = True,
        help_text = _('Profile pictures of Users'))