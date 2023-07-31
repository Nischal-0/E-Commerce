from django.contrib import admin
from django.urls import path
from . import views
app_name = "Store"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index)
]
