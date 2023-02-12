# Cashier Program 
class Transaction:
    """
    
    """
    
    def __init__(self,transaction_id):
        """
        Constructor Method to initialize the transaction
        Parameters:
        1. self
        2. transaction_id : uniquely generated id for the current transaction
        """
        self.transaction_id = transaction_id
        item_list = []
        item_list_price = []
        item_list_qty = []
        total_price = 0
        
    
    def add_item(cls,item_list, item_list_price, item_list_qty):
        """
        Method for adding new items and its quantity & price 
        Parameters:
        1. item_list : name of the item
        2. item_list_price : price of the item
        3. item_list_qty : quantity of the item
        """
        for i in range(1000):
            print("=========ADDING NEW ITEM=========")
            
            item_list.append(input(f'Masukkan nama item ke - {i} : ').lower())
            item_list_price.append(int(input('Masukkan harga item :')))
            item_list_qty.append(int(input('Masukkan jumlah item :')))
            
            add_choose = input('Apakah Anda ingin menambah item ? Y/N :')
            if add_choose.upper() == 'N':
                continue
            
            
    def update_item_name(cls,item_list,updated_item_name):
        """
        Method to update the name of the item
        Parameters:
        1. item_list : name of the item (pre-update)
        2. updated_item_name : new name of the item (post-update)
        """
        for item in item_list:
            if item_list[item]  == item_list.lower():
                item_list[item] = updated_item_name.lower()
        print("Update succeded")
        
    def update_item_qty(cls,item_list,item_list_qty,updated_item_qty):
        """
        Method to update the name of the item
        Parameters:
        1. item_list : name of the target item 
        2. item_list_qty : qty of the target item (pre-update)
        3. updated_item_qty : qty of the target item (post-update)
        """
        for item in item_list:
            if item_list[item]  == item_list.lower():
                item_list_qty[item] = updated_item_qty
        print("Update succeded")
            
    
    def update_item_price(cls,item_list,item_list_price,updated_item_price):
        """
        Method to update the name of the item
        Parameters:
        1. item_list : name of the target item 
        2. item_list_price : price of the target item (pre-update)
        3. updated_item_price : price of the target item (post-update)
        """
        for item in item_list:
            if item_list[item]  == item_list.lower():
                item_list_price[item] = updated_item_price
        print("Update succeded")
    
    def delete_item(cls,item_list, item_list_price, item_list_qty):
        """
        Method to update the name of the item
        Parameters:
        1. item_list : name of the item (pre-update)
        2. item_list_price 
        3. item_list_qty
        """
        for item in item_list:
            if item_list[item]  == item_list.lower():
                item_list.remove(item_list[item])
                item_list_price.remove(item_list_price[item])
                item_list_qty.remove(item_list_qty[item])
    
    def reset_transaction(cls,item_list, item_list_price, item_list_qty):
        """
        Method to reset transaction
        Parameters:
        1. item_list : name of the item
        2. item_list_price : price of the item
        3. item_list_qty : quantity of the item
        """
        try:
            reset_choose = input('Apakah Anda ingin mereset transaksi? Y/N')
        except:
            raise ValueError
        item_list.clear()
        item_list_price.clear()
        item_list_qty.clear()
        
    def check_order(cls,item_list,item_list_price,item_list_qty):
        """
        Method to check and display order
        Parameters:
        1. item_list : name of the item
        2. item_list_price : price of the item
        3. item_list_qty : quantity of the item
        """
        
        print('| No | Nama Item | Jumlah Item |   Harga/Item   |  Total Harga')
        print('----------------------------------------------------------------')
        for i in range(len(item_list)):
            print(f"| No | {item_list[i]} | {item_list_qty[i]} | Rp. {item_list_price[i]} | Rp. {item_list_qty[i]*item_list_price[i]}")
            print('----------------------------------------------------------------')
        
    def total_price(cls,item_list_price, item_list_qty):
        """
        Method to calculate total price
        Parameters:
        1. item_list : name of the item
        2. item_list_price : price of the item
        3. item_list_qty : quantity of the item
        """
        for i in range(len(item_list_price)):
            total = total + (item_list_price[i] * item_list_qty[i])
            
        if total < 300000:
            total = total - (total*0.05)
        
        elif total < 500000:
            total = total - (total*0.08)
        
        elif total > 500000:
            total = total - (total*0.1)
        
        print(total)
            
        
        
            
        
        
        

    
    
    