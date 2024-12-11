from users import User
from order import Order
from menu import Menu
class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.cart=Order()
    
    def add_to_cart(self,shop,item_name,quan):
        item=shop.menu.find_item(item_name)
        if quan > item.quantity:
            print("\n\t\t\tQuantity level excceeded\n")
        else:
            item.quantity-=quan
            self.cart.add_product(item,quan)

    def remove_item(self,shop,item_name):
        item=shop.menu.find_item(item_name)
        self.cart.remove_product(shop,item)
    
    
    def view_menu(self,shop):
        shop.menu.view_menu()
    
    def paybill(self):
        print(f'\n\t\tTotal bill {self.cart.total_price} taka paid')
        print("\t\tThank you for shopping from our shop!!\n")
        self.cart.cart_clear()   

    def view_cart(self):
        print("\t\t\t__________Cart_________")
        print("\t\t\tProduct\tprice\tQuantity")
        for product,quan in self.cart.items.items():
            print(f'\t\t\t{product.name}\t{product.price}tk\t{quan}')
        print(f'\n\t\t\tTotal Bill:{self.cart.total_price}\n')


    
