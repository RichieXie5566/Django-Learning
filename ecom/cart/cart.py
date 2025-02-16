from store.models import Product, Profile
import json

class Cart():
    def __init__(self,request):
        self.session = request.session
        # 取得request
        self.request = request
        # 取得已存在的鍵值
        cart = self.session.get('session_key')

        # 新使用者則建立新的鍵值
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        # 確定購物車可以用在每個頁面
        self.cart = cart
    
    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        
        # 判斷商品有沒有在購物車裡
        if product_id in self.cart: 
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # 處理已登入的會員
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            carty = str(self.cart)
            carty = json.dumps(self.cart) #carty.replace("\'","\"")
            current_user.update(oldcart = str(carty))


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        
        # 判斷商品有沒有在購物車裡
        if product_id in self.cart: 
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # 處理已登入的會員
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            carty = str(self.cart)
            carty = json.dumps(self.cart) #carty.replace("\'","\"")
            current_user.update(oldcart = str(carty))

    def __len__(self): 
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys() # 從購物車獲取產品id
        products = Product.objects.filter(id__in = product_ids) # 用id在資料庫尋找產品
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product) # 確保product_id為字串，(Django session 存儲的鍵必須是字串)
        product_qty = int(quantity) # 確保quantity是整數，防止類型錯誤

        ourcart = self.cart # 取得目前購物車的內容
        ourcart[product_id] = product_qty # 更新購物車內該商品的數量

        self.session.modified  = True # 標記 session 已修改，確保變更會被保存

        # 處理已登入的會員
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            carty = str(self.cart)
            carty = json.dumps(self.cart) #carty.replace("\'","\"")
            current_user.update(oldcart = str(carty))
        
        thing = self.cart # 返回更新後的購物車內容（可用於除錯）
        return thing
    
    def delete(self, product):
        product_id = str(product) # 確保為字串

        if product_id in self.cart:
            del self.cart[product_id] # 如果商品存在於購物車內，則將其刪除

        self.session.modified = True # 標記 session 已修改，確保變更會被保存

        # 處理已登入的會員
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            carty = str(self.cart)
            carty = json.dumps(self.cart) #carty.replace("\'","\"")
            current_user.update(oldcart = str(carty))

    def cart_total(self):
        product_ids = self.cart.keys() # 取得購物車內所有商品的 ID
        products = Product.objects.filter(id__in=product_ids) # 從資料庫查詢這些商品的詳細資訊
        quantities = self.cart # 取得購物車內的商品數量
        total = 0 # 初始化總金額
        for key, value in quantities.items(): 
            key = int(key)     # 轉換 ID 為整數變數(確保與資料庫中的 ID 匹配)
            for product in products:
                if product.id == key: # 確保對應正確的商品
                    if product.is_sale:
                        total = total + (product.sale_price * value) # 如果商品有特價，使用特價計算總額
                    else:
                        total = total + (product.price * value) # 否則使用原價計算總額
        return total