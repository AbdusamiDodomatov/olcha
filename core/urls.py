from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),  
    path('api/auth/', include('user.urls')),
    path('api/order', include('orders.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
