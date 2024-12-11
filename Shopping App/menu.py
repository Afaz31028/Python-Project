class Menu:
    def __init__(self):
        self.items=[]
    
    def add_new_product(self,item):
        self.items.append(item)
        print(f'\n\t\t\tThe item {item.name} is successfull added')

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_product(self,item_name):
        item=self.find_item(item_name)
        if item == None:
            print("\n\t\t\tThe item is found")
        else:
            self.items.remove(item)

    def add_quantity(self,item_name,quan):
        for item in self.items:
            if item.name.lower()==item_name.lower():
                item.quantity+=quan

    def view_menu(self):
        print("\t\t\t---------Products----------")
        print("\t\t\tProduct\tPrice  Quantity")
        for item in self.items:
            print(f'\t\t\t{item.name}\t{item.price}\t{item.quantity}')
    
    
    


