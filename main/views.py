from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status


class login(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
            try:
                users = User.objects.get(username=username)
                user = authenticate(username=username, password=password)
                if user is not None:
                    status = 200
                    token, created = Token.objects.get_or_create(user=user)
                    data = {
                        'username': username,
                        'user_id': users.id,
                        'token': token.key,
                    }
                else:
                    status = 403
                    message = 'Incorrect username/password!'
                    data = {
                        'status': status,
                        'message': message
                    }
            except User.DoesNotExist:
                    status = 404
                    message = 'User did not found'
                    data = {
                        'status': status,
                        'message': message
                    }
            return Response(data)
        except Exception as err:
            return Response({'error': f'{err}'})


class getUsers(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.all()
        u = UserSerializer(user, many=True)
        return Response(u.data, status=status.HTTP_200_OK)


class create_user(APIView):
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        u = User.objects.create_user(username=username, email=email, password=password)
        u.save()
        user = UserSerializer(u)
        return Response('successfully created')


class SubscribeView(viewsets.ModelViewSet):
    serializer_class = SubscribeSerializer
    queryset = Subscribers.objects.all()
    http_method_names = ['post']


# @api_view(['GET'])
# def banner(request):
#     s = Mainproducts.objects.all().order_by('-id')[:3]
#     global ser
#     if 'in_slider' == True:
#         banner1 = request.GET.get(s)
#         print(111111)
#         ser = MainproductsBannerSerializer(banner1, many=True)
#     else:
#         pass
#
#     return Response(ser.data)


@api_view(['GET'])
def ads(request):
    p = Ads.objects.all().order_by('-id')[:7]
    ser = AdsSerializer(p, many=True)
    return Response(ser.data)


@api_view(['GET'])
def service(request):
    s = Service.objects.all().order_by('-id')[:5]
    ser = ServiceSerializer(s, many=True)
    return Response(ser.data)


@api_view(['GET'])
def index_info(request):
    c = Information.objects.last()
    ser = IndexInfoSerializer(c)
    return Response(ser.data)


@api_view(['GET'])
def app(request):
    c = App.objects.all().order_by('-id')[:2]
    ser = AppSerializer(c, many=True)
    return Response(ser.data)


# @api_view(['POST'])
# def subscribe(request):
#     email = request.POST.get('email')
#     Subscribers.objects.create(email=email)
#     print(email)
#     return Response('successfully submitted!')


@api_view(['GET'])
def about(request):
    c = About.objects.all().order_by('-id')[:2]
    ser = AboutSerializer(c, many=True)
    return Response(ser.data)


@api_view(['GET'])
def product(request):
    c = Mainproducts.objects.all()
    ser = AllproductSerializer(c, many=True)
    return Response(ser.data)


# @api_view(['GET'])
# def rating(request):
#     rating = Rating.objects.all()
#     ser = RatingSerializer(rating, many=True)
#     return Response(ser.data)


# @api_view(['GET'])
# def brand(request):
#     brand = Brand.objects.all()
#     ser = BrandSerializer(brand, many=True)
#     return Response(ser.data)


@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def category(request):
    # user = request.user
    # print(user)
    category = Category.objects.all()
    ser = CategorySerializer(category, many=True)
    return Response(ser.data)


@api_view(['GET'])
def in_slider(request):
    in_sliderr = Mainproducts.objects.filter(in_slider=True)
    ser = MainproductsSerializer(in_sliderr, many=True)
    return Response(ser.data)


@api_view(['GET'])
def blog(request):
    blog = Blog.objects.all().order_by('-id')[:9]
    ser = BlogSerializer(blog, many=True)
    return Response(ser.data)


@api_view(['GET'])
def blog_detail(request, pk):
    blog_details = BlogDetail.objects.get(pk=pk)
    ser = BlogDetailSerializer(blog_details)
    data = {
        "blog_details": ser.data,
    }
    return Response(data)


@api_view(['POST'])
def blog_comment(request, pk):
    blogs = Blog.objects.get(pk=pk)
    text = request.POST.get('text')
    user = request.POST.get('user')
    blog = request.POST.get('blog')
    if text != '':
        BlogComment.objects.create(text=text, user_id=user, blog_id=blog)
        print(text)
        return Response('successfully submitted!')


@api_view(['GET'])
def faq(request):
    faq = Faq.objects.all().order_by('-id')[:7]
    ser = FaqSerializer(faq, many=True)
    return Response(ser.data)


@api_view(['GET'])
def subcategory(request):
    category = request.GET.get('category')
    sub = SubcategorySerializer(SubCategory.objects.filter(category_id=category), many=True).data
    return Response(sub)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_card(request):
    user = request.user
    product = request.POST.get('product')
    quantity = request.POST.get('quantity')
    card = Card.objects.create(user=user, quantity=quantity, product_id=product)
    c = CardSerializer(card)
    return Response(c.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_wishlist(request):
    user = request.user
    product = request.POST.get('product')
    wishlist = Wishlist.objects.create(user=user, product_id=product)
    c = WishlistSerializer(wishlist)
    return Response(c.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_order(request):
    user = request.user
    country = request.POST.get('country')
    f_name = request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    address = request.POST.get('address')
    city = request.POST.get('city')
    zipcode = request.POST.get('zipcode')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    total = 0
    order = Order.objects.create(user=user, country=country, f_name=f_name, l_name=l_name, address=address, city=city, zipcode=zipcode, email=email, phone=phone)
    card = Card.objects.filter(user=user)
    for i in card:
        OrderItem.objects.create(product=i.product, price=i.product.price, quantity=i.quantity, order=order)
        order.total += f'{i.quantity * i.product.price}'
        # productnum = int(Mainproducts.number) - i.quantity
        order.save()
    Card.objects.filter(user=user).delete()
    return Response(OrderSerializer(order).data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_order_item(request, pk):
    user = request.user
    order = Order.objects.get(id=pk)
    card = Card.objects.filter(user=user)
    for i in card:
        order.total += f'{i.quantity * i.product.price}'
    if user.id == order.user.id:
        items = OrderItem.objects.filter(order=order)
        return Response(OrderItemSerializer(items, many=True).data)
    else:
        return Response({'message': "Order with this number didn't found"})


@api_view(['GET'])
def product_detail(request, pk):
    product_details = Mainproducts.objects.get(pk=pk)
    ser = MainproductsSerializer(product_details)
    data = {
        "product_details": ser.data,
    }
    return Response(data)


@api_view(['POST'])
def category_product(request):
    category = request.POST.get('category')
    c = Mainproducts.objects.filter(name__icontains=category)
    ser = MainproductsSerializer(c, many=True)
    return Response(ser.data)


@api_view(['POST'])
def product_search(request):
    product = request.POST.get('product')
    p = Mainproducts.objects.filter(name__icontains=product)
    ser = MainproductsSerializer(p, many=True)
    return Response(ser.data)


@api_view(['POST'])
def price(request):
    min_price = request.POST.get('min_price')
    max_price = request.POST.get('max_price')
    filter_price_product = Mainproducts.objects.filter(price__range=(min_price, max_price))
    ser = MainproductsSerializer(filter_price_product, many=True)
    return Response(ser.data)


@api_view(['GET'])
def bunus_percent(request):
    bonus_product = []
    products = Mainproducts.objects.all()
    for i in products:
        if i.bonus_percent >= 1:
            bonus_product.append(i)
    ser = MainproductsSerializer(bonus_product, many=True)
    return Response(ser.data)


@api_view(['POST'])
def blog_name_search(request):
    blog_name = request.POST.get('blog_name')
    b = Blog.objects.filter(title__icontains=blog_name)
    ser = BlogSerializer(b, many=True)
    return Response(ser.data)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_card(request, pk):
    user = request.user
    card = Card.objects.get(id=pk)
    card.delete()
    return Response('Successfully deleted')


@api_view(['PUT', 'PATCH'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def edit_card(request, pk):
    user = request.user
    product = request.POST.get('product')
    quantity = request.POST.get('quantity')
    card = Card.objects.get(id=pk)
    card.product_id = product
    card.quantity = quantity
    card.product.save()
    card.save()
    ser = CardSerializer(card)
    return Response(ser.data)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_wishlist(request, pk):
    user = request.user
    wishlist = Wishlist.objects.get(id=pk)
    wishlist.delete()
    return Response('Successfully deleted')
