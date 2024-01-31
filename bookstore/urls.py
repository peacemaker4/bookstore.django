from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from books.views import HomePage, AllBooks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomePage.as_view(), name="homepage"),
    path('books/', include("books.urls")),
    path('', include('booksLanding.urls')),
    path('authentication/', include('authentication.urls')),
    path('prometheus/', include("django_prometheus.urls")),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
handler403 = 'books.views.handler403'