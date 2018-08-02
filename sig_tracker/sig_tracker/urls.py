from django.contrib import admin
from django.conf.urls import include,url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('main.urls')),
<<<<<<< HEAD
]

=======
    ]
>>>>>>> 531244f4fc50a5f7af58a82ab52f9b5d7eb22c68

