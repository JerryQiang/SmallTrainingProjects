# 产品库存管理——创建一个管理产品库存的应用。建立一个产品类，包含价格、id、库存数量。然后建立一个库存类，记录各种产品并能计算库存的总价值。

class product(object):
    def __init__(self,id,price,amounts):
            self.id = id
            self.price = price
            self.amounts = amounts

class inventory(object):
    def __init__(self):
        self.stock = []
        self.value = 0

    def add_product(self,product):
        self.stock.append(product)

    def get_value(self):
        for product in self.stock:
            self.value += product.price * product.amounts
        return self.value

product_1 = product(1,2,5)
product_2 = product(2,3,6)

inventory_1 = inventory()

inventory_1.add_product(product_1)
inventory_1.add_product(product_2)

print(inventory_1.get_value())