"""realshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings
from main.views import *
from main.router import router


schema_view = get_schema_view(
   openapi.Info(
      title="Shop API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('ads/', ads),
    path('subcategory/', subcategory),
    path('add-card/', add_card),
    path('delete-card/<int:pk>/', delete_card),
    path('edit-card/<int:pk>/', edit_card),
    path('add-wishlist/', add_wishlist),
    path('delete-wishlist/<int:pk>/', delete_wishlist),
    path('create-order/', add_order),
    path('get-order-items/<int:pk>/', get_order_item),
    path('get-users/', getUsers.as_view()),
    path('create-user/', create_user.as_view()),
    path('login/', login.as_view()),
    path('faq/', faq),
    path('service/', service),
    path('category/', category),
    path('index-info/', index_info),
    path('app/', app),
    path('shop-banner/', in_slider),
    path('blog/', blog),
    path('blog-detail/<int:pk>/', blog_detail),
    path('about/', about),
    path('allproducts/', product),
    path('product-detail/<int:pk>/', product_detail),
    path('category-product/', category_product),
    path('product-search/', product_search),
    path('blog-search/', blog_name_search),
    path('price/', price),
    path('bonus-percent/', bunus_percent),
    path('blog-comment/<int:pk>/', blog_comment),
    path('r/', include(router.urls))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

