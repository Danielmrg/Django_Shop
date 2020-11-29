from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.

'''
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
'''

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    '''Admin View for UserProfile'''

    list_display = ('first_name','last_name')
    list_filter = ('address',)
    search_fields = ('first_name', 'last_name','address')
    ordering = ('first_name',)

class CategoryInline(admin.TabularInline):
    '''Tabular Inline View for Category'''

    model = Category
    min_num = 1
    max_num = 20
    extra = 1

@admin.register(Categorys)
class CategorysAdmin(admin.ModelAdmin):
    '''Admin View for Category's'''

    list_display = ('title',)
    list_filter = ('title',)
    inlines = [
        CategoryInline,
    ]
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    search_fields = ('title',)
    ordering = ('title',)



class itemimageInline(admin.TabularInline):
    '''Tabular Inline View for itemimage'''

    model = itemimage
    min_num = 1
    max_num = 20
    extra = 1


@admin.register(Item)
class ItemAdmin(SummernoteModelAdmin):
    '''Admin View for Item'''

    list_display = ['title','price','discount_price','slug']
    list_filter = ['price','discount_price','slug']
    inlines = [
        itemimageInline,
    ]
    summernote_fields = ('description')
    search_fields = ('title','slug','description')
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''Admin View for OrderItem'''

    list_display = ['user','ordered','quantity','user',]
    list_filter = ['ordered','quantity']
    search_fields = ('ordered','quantity')
    list_display_links = [
        'user',
        'ordered'
    ]

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    '''Admin View for Coupon'''

    list_display = ('code','amount','timemake')
    list_filter = ('timemake','amount')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'state',
        'zip',
        'default',
    ]
    list_filter = ['default', 'state']
    search_fields = ['user','state' , 'street_address', 'apartment_address', 'zip']

@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ('reason','accepted','email')

