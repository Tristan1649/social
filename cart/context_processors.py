from .cart import Cart
# давай мне вон то! А Чо я вон у тех спроси?

def cart(request):
    return {'cart': Cart(request)}