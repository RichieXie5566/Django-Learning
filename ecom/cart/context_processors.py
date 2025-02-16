from .cart import Cart

# 建立可以讓購物車用在所有頁面的處理器
def cart(request):
    # 從購物車回傳數據
    return {'cart':Cart(request)}