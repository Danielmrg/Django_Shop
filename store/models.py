from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db.models import Sum
from django.db import models
from django.utils import timezone



class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)
    first_name = models.CharField(max_length=85, blank=True, null=True)
    last_name = models.CharField(max_length=85, blank=True, null=True)
    address = models.TextField(max_length=540, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Categorys(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Category(models.Model):
    image = models.ImageField(upload_to='image-category',default='image/default.jpg')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(to=Categorys,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def get_details(self):
        return reverse('store:detail_category',kwargs={"id":self.id,'title':self.title})


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=3,blank=False,default=0)
    discount_price = models.DecimalField(max_digits=20, decimal_places=3,blank=True,null=True,default=0)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    description = models.TextField()
    date_created =models.DateTimeField(auto_now_add=True,blank=True, null=True)
    image = models.ImageField(upload_to='image-items',default='image/default.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:product", kwargs={
            'slug': self.slug,'id': self.id
        })

    def get_offer_percentage(self):
        offer=round(self.discount_price * 100 / self.price)
        return offer
    def get_time_product(self):
        return timezone.now() - self.date_created

    def get_add_to_cart_url(self):
        return reverse("store:add-to-cart", kwargs={
            'slug': self.slug,'id':self.id
        })

    def get_remove_from_cart_url(self):
        return reverse("store:remove-from-cart", kwargs={
            'slug': self.slug,'id':self.id
        })

class itemimage(models.Model):
    image = models.ImageField(upload_to='image-item',default='image/default.jpg')
    item = models.ForeignKey(to=Item,on_delete=models.CASCADE)

class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()



class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    address = models.TextField(max_length=320, blank=False,null=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class CouponManager(models.Manager):
    def get_queryset(self):
        return super(CouponManager, self).get_queryset().order_by('-timemake')

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    timemake=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    objects=models.Manager()
    couponmanager=CouponManager()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"
