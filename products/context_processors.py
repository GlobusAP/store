from .models import Basket, ProductCategory


def baskets(request):
    user = request.user
    return {'baskets': Basket.objects.filter(user=user) if user.is_authenticated else []}


def categories(request):
    all_categories = ProductCategory.objects.all()
    return {'categories': all_categories}
