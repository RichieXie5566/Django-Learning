from django.contrib import admin
from .models import ShippingAddress, Order,OrderItem
from django.contrib.auth.models import User

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

# 設定 OrderItem 內聯
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1  # 額外提供 1 個空白欄位，方便新增

# 設定 Order 的 Admin 設定
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_ordered"]
    inlines = [OrderItemInline] # 將內聯模型加入

# 註冊模型
admin.site.unregister(Order) # 先取消原本的 Order 註冊
admin.site.register(Order, OrderAdmin) # 重新註冊，並使用 OrderAdmin