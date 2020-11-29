from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from django_filters.views import FilterView
from .models import Item
from .filters import ProductFilter
from . import sitemaps
from . import views
from . import feeds

'''
sitemaps = {
    "posts": PostSitemap,
}
'''

app_name = "store"

urlpatterns = [
    path('',views.home , name="home"),
    path('store/',views.store , name="store"),
    path('store/detail/<int:id>/<str:slug>/',views.detail , name="product"),
    path('store/<category>/',views.detail , name="detail_category"),
    path('profile/cart/',views.cart , name="cart"),
    path('profile/',views.profile , name="profile"),
    path('profile/settings/',views.settings , name="settings"),
    path('profile/cart/add/<int:id>/<str:slug>/',views.add_to_cart , name="add-to-cart"),
    path('profile/cart/delete/',views.delete_of_cart , name="remove-from-cart"),
    path('profile/settings/updateinfo/',views.update_info_order , name="update_info_order"),
    # site maps 
    # path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    # feeds
    # path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path('test/store/',views.ItemListView.as_view(), name="item_list"),
    path('test/fil/', FilterView.as_view(filterset_class=ProductFilter,template_name='test/test.html'), name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)