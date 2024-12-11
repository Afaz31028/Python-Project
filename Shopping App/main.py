from admin import Admin
from customer import Customer
from menu import Menu
from order import Order
from products import Product
from shop import Shop
from users import User

shop=Shop('Al Baraka Fashion')
print("\n<-----Bismilaahir Rahmanir Rahim---->")
def Customer_interface():
        email=input("\tEmail:")
        password=input("\tPassword:")
        customer=Customer(email,password)
        while True:
            print(f'\t\tWelcome to Our Shop, Sir/Madam!!!')
            print("\t\t1.  View Menu List")
            print("\t\t2.  Add to Cart")
            print("\t\t3.  Remove the Cart")
            print("\t\t4.  View Cart")
            print("\t\t5.  Pay Bill")
            print("\t\t6.  Exit")
            option=int(input("\n\t\t\tEnter one option:"))
            if option==1:
                customer.view_menu(shop)
            elif option ==2:
                item=input("\t\t\tItem Name:")
                Q=int(input("\t\t\tItem Quantity:"))
                customer.add_to_cart(shop,item,Q)
            elif option ==3:
                item=input("\t\t\tItem Name:")
                customer.remove_item(shop,item)
            elif option==4:
                customer.view_cart()
            elif option==5:
                customer.paybill()
            elif option==6:
                break
            else:
                print("\t\t\tInvalid Input,try again")
def Admin_inteface():
    email=input("\tEmail:")
    password=input("\tPassword:")
    admin=Admin(email,password)
    while True:
        print(f'\n\t\tWelcome Sir!!!')
        print("\t\t1.  View Menu List")
        print("\t\t2.  Add New Product")
        print("\t\t3.  Remove Product")
        print("\t\t4.  Exit")
        choice=int(input("\t\t\tChoose an option:"))
        if choice==1:
            admin.view_menu(shop)
        elif choice==2:
            item_name=input("\t\t\tItem Name:")
            Q=int(input("\t\t\tQuantity:"))
            P=int(input("\t\t\tPrice:"))
            item=Product(item_name,P,Q)
            admin.add_item(shop,item)
        elif choice==3:
            item=input("\t\t\tItem Name:")
            admin.remove_item(shop,item)
        elif choice==4:
            break
        else:
            print("\t\t\tInvalid Input,try again")

while True:
    print("******Main Interface******")
    print("\t1.  Admin")
    print("\t2.  Customer")
    print("\t3.  Exit")
    option=int(input("\tChoose one option:"))
    if option==1:
        Admin_inteface()
    elif option==2:
        Customer_interface()
    else:
        break

