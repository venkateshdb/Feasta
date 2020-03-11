from django.db import models
import uuid


class Mess(models.Model):
    """
    Manage all mess menus, ans messes
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mess_name = models.CharField(max_length=200, null=False)
    timing = models.TimeField(auto_now_add=False, blank=False)
    address = models.CharField(max_length=300, blank=False)
    # veg or non-veg
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.mess_name


class Menu(models.Model):
    """
    Store menus from a mess
    """
    menu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=200, blank=False)

    # foreign key
    mess_id = models.ForeignKey(Mess, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Price(models.Model):
    """
    Price for each item in menu
    """
    one_time = models.IntegerField(blank=False)
    monthly = models.IntegerField(blank=False)

    # foreign key
    mess_id = models.ForeignKey(Mess, on_delete=models.CASCADE)
