from django.urls import path
from api.views import company_list, company_detail, login, logout


urlpatterns = [
    path('company/', company_list),
    path('company/<int:pk>/', company_detail),
    path('login/', login),
    path('logout/', logout)
]

