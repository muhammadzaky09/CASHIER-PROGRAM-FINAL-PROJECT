"""
    Muhammad Zaky Firdaus
    12/2/23
    Cash Register Program in Python Programming Language
 """
import transactionModule
import random

transaction = transactionModule.Transaction(random.randint(1,1000))
item_list = []
item_list_price = []
item_list_qty = []
total_price = 0

while True:
    print("Welcome to Cash Register Program".upper())
    print('================================================')
    print('1.Add items \n2.Update item name \n3.Update item price \n4.Update item quantity \n5.Delete item')
    print('6.Reset transaction \n7.Check order \n8.Check out transaction\n 9. Exit')
    print('================================================')
    option_1 = input('CHOOSE TRANSACTION : ')

    if option_1 == '1':
        transaction.add_item(item_list,item_list_price,item_list_qty)
        
    elif option_1 == '2':
        updated_item_name = input('Which item would you like to update')
        transaction.update_item_name(item_list,updated_item_name)

    elif option_1 == '3':
        updated_item_name = input('Which item would you like to update')
        transaction.update_item_name(item_list,updated_item_name)


    elif option_1 == '4':
        updated_item_name = input('Which item would you like to update')
        transaction.update_item_name(item_list,updated_item_name)


    #elif option_1 == '5':

    #elif option_1 == '6':

    #elif option_1 == '7':

    #elif option_1 == '8':
    
    elif option_1 == '9':
        break
    



   