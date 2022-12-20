from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = "__all__"


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class MainproductsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Mainproducts
        fields = "__all__"


class MainproductsBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainproducts
        fields = ["image", "in_slider"]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"


class IndexInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ["logo", 'telegram', 'insta', 'facebook']


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStyle
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class AllproductSerializer(serializers.ModelSerializer):
    class Meta:
        depth=1
        model = Mainproducts
        fields = ["name", "image", "bonus_percent", "rating", "price"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id', 'password']


class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = BlogDetail
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    product = MainproductsSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        depth=1
        model = Card
        fields = "__all__"


class WishlistSerializer(serializers.ModelSerializer):
    product = AllproductSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Wishlist
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    # product = AllproductSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    product = AllproductSerializer(read_only=True),
    order = OrderSerializer(read_only=True)
    # quantity = AllproductSerializer(read_only=True)
    # user = UserSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = "__all__"


