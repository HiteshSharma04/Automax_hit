from django.urls import path
from .views import login_view, Register_View, logout_view, ProfileView
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login_view, name = 'login'),
    path('register/', Register_View.as_view(), name = 'register'),
    path('logout/', logout_view, name = 'logout'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
]
