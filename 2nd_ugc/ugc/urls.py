"""ugc URL Configuration

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
from django.urls import path
from django.conf.urls import include
import accounts.views
import feeds.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feeds.views.index, name='index'),
    path('new/', feeds.views.new, name='new'),
    path('<int:id>/', feeds.views.category, name='category'), 
    path('article/<int:id>/', feeds.views.show, name='show'), 
    path('article/<int:id>/manage/', feeds.views.manage, name='manage'),
    path('article/<int:id>/edit/', feeds.views.edit, name='edit'),
    path('article/<int:id>/delete/', feeds.views.delete, name='delete'),
    path('article/<int:id>/comments/', feeds.views.create_comment, name='create_comment'),
    path('article/<int:id>/comments/<int:cid>/', feeds.views.delete_comment, name='delete_comment'),
    path('article/<int:id>/comments/<int:cid>/reply/', feeds.views.create_reply, name='create_reply'),
    path('article/<int:id>/comments/<int:cid>/reply/', feeds.views.create_reply, name='create_reply'),
    path('article/<int:id>/comments/<int:cid>/reply/<int:rid>/', feeds.views.delete_reply, name='delete_reply'),
    path('accounts/', include('accounts.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)