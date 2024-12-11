from users import User
from shop import Shop
class Admin(User):
    def __init__(self, email, password):
        super().__init__(email, password)
    
    def view_menu(self,shop):
        shop.menu.view_menu()
    
    def add_item(self,shop,item):
        shop.menu.add_new_product(item)
    
    def remove_item(self,shop,item):
        shop.menu.remove_product(item)
    
