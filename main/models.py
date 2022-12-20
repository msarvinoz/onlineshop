from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Rating(models.Model):
    rate = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Size(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Advantage(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Info(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ads(models.Model): #-----> partner
    image = models.ImageField(upload_to='media/')


class Mainproducts(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    in_slider = models.BooleanField(default=True)
    bonus_percent = models.IntegerField()
    is_top = models.BooleanField(default=False)
    advantage = models.ManyToManyField(Advantage)
    is_recommended = models.BooleanField(default=True)
    info = models.ManyToManyField(Info)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    review = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    price = models.IntegerField()
    number = models.IntegerField()
    sold = models.IntegerField()
    text = models.TextField()
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    weight = models.CharField(max_length=255, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    discount = models.CharField(max_length=255, null=True, blank=True)
    shipping = models.CharField(max_length=255)
    care_info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Information(models.Model):
    logo = models.ImageField(upload_to='media/')
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    insta = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255)
    longtitude = models.CharField(max_length=255)


class Service(models.Model): #-------> sevice
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')


class Subscribers(models.Model):
    email = models.EmailField()


class Card(models.Model):
    product = models.ForeignKey(Mainproducts, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Wishlist(models.Model):
    product = models.ForeignKey(Mainproducts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    country = models.CharField(max_length=255)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    total = models.CharField(max_length=255)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Mainproducts, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()


class App(models.Model):
    logo = models.ImageField(upload_to='media/')
    link = models.CharField(max_length=255)


class WorkStyle(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')
    statistic = models.IntegerField()


class Team(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')
    profession = models.CharField(max_length=255)
    account = models.URLField()


class Location(models.Model):
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')
    location = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.EmailField()


class About(models.Model):
    main_image = models.ImageField(upload_to='media/')
    main_title = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    mini_text = models.CharField(max_length=200)
    text = models.CharField(max_length=255)
    add_image = models.ImageField(upload_to='media/')
    map = models.URLField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    work = models.ForeignKey(WorkStyle, on_delete=models.CASCADE)


class Address(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()


class Blog(models.Model):
    main_image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class BlogDetail(models.Model):
    title = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    img = models.ImageField(upload_to='blogs/')
    created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    comment = models.ForeignKey(BlogComment, on_delete=models.CASCADE)


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
