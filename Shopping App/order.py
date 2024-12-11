class Order:
    def __init__(self):
        self.items={}

    def add_product(self,product,quan):
        if product in self.items:
            self.items[product]+=quan
        else:
            self.items[product]=quan

    def remove_product(self,shop,item):
        Q=self.items[item]
        del self.items[item]
        shop.menu.add_quantity(item.name,Q)
        print(f'\n\t\t\tThe item {item.name} removed successfully\n')

    @property
    def total_price(self):
        return sum(product.price * quan for product,quan in self.items.items())

    def cart_clear(self):
        self.items={}
        
    

    

        