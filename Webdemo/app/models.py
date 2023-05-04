from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your models here.
# Change forms register django
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


# class Customer(models.Model):
#     user = models.OneToOneField(
#         User, on_delete=models.SET_NULL, null=True, blank=False)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return str(self.id)

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.transaction_id)

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quatity for item in orderitems])  # tong so luong mua
        return total

    @property  # tong tien
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        # tong so luong mua
        total = sum([item.get_total for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quatity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property  # tong tien 1 ssp
    def get_total(self):
        total = self.product.price * self.quatity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=11, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
