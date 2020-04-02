from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, phone_no, password,
                     is_staff, is_superuser, is_user, is_shop,
                     **extra_fields):
        now = timezone.now()

        if not phone_no:
            raise ValueError('Error!!..Please enter your contact!')

        if not email:
            raise ValueError('Error!!..Please enter your Email!')

        email = self.normalize_email(email)
        user = self.model(email=email,phone_no = phone_no,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          is_user = is_user, is_shop= is_shop,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, phone_no ,password=None, is_user= True, is_shop = False,
                     **extra_fields):
        return self._create_user(email, phone_no, password, False, False, is_user , is_shop,
                                 **extra_fields)

    def create_superuser(self, email, phone_no,password, **extra_fields):
        return self._create_user(email, phone_no, password, True, True, is_user = False, is_shop = False,
                                 **extra_fields)