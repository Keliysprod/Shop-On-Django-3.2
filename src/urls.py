from django.contrib import admin
from django.urls import path, include
from mshop.views import ProductList,ProductDetail
from django.conf import settings
from django.conf.urls.static import static
from mshop.views import Register, Success, Homepage


urlpatterns = [
    path('shop/', ProductList.as_view(), name='shop'),
    path('shop/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(),name='registrations'),
    path('', include('django.contrib.auth.urls')),
    path('success/',Success, name='successreg'),
    path('', Homepage, name='home')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)