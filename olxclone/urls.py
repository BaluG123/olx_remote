"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from testapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.item_list_view),
    path('detail/(?p<year>\d{4})/(?p<month>\d{2})/(?p<day>\d{2})/(?p<item>\[-\w]+)/$',views.item_detail_view,name="item_detail"),
    path('below5/',views.item_ormview),
    path('above5/',views.item_ormview1),
    path('create/',views.Item_addview),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',views.Signup_view),
    path('logout/',views.logout_view)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
