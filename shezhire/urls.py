from django.contrib import admin
from django.urls import path, include  # <-- добавили include

urlpatterns = [
    path('admin/', admin.site.urls),
    # теперь все запросы, не попавшие в admin/, пойдут в family.urls
    path('', include('family.urls')),  
]
