from routers.PaymentHistory_class import PaymentHistory
from routers.CoinTransaction_class import Coin_transaction
from routers.Cart_class import Cart

class Account:
    def __init__(self, account_name, password):
        self.__account_name = account_name
        self.__password = password
        self.__id_account = 0
        self.__coin = 0
        self.__book_collection_list = []
        self.__payment_history_list = []
        self.__coin_transaction_history_list = []
    
    @property
    def account_name(self):
        return self.__account_name

    @property
    def id_account(self):
        return self.__id_account
    
    @property
    def password(self):
        return self.__password
    
    @property
    def coin(self):
        return self.__coin
    
    @property
    def book_collection_list(self):
        return self.__book_collection_list
    
    @property
    def payment_history_list(self):
        return self.__payment_history_list

    @property
    def coin_transaction_history_list(self):
        return self.__coin_transaction_history_list
    
    @id_account.setter
    def id_account(self, id_account):
        self.__id_account = id_account
        
    def add_coin(self, added_coins):
        self.__coin += added_coins
        
    def lost_coin(self, lost_coins):
        self.__coin -= lost_coins
        
    def update_book_collection_list(self, book):
        self.__book_collection_list.append(book)

    def update_payment_history_list(self,money,date_time):
        self.__payment_history_list.append(PaymentHistory(money,date_time))   

    def update_coin_transaction_history_list(self, coin,date_time,type):
        self.__coin_transaction_history_list.append(Coin_transaction(coin,date_time,type))


class Reader(Account):
    def __init__(self, account_name, password):
        super().__init__(account_name, password)
        self.__cart = Cart()
        self.__cart_list = []

    @property
    def cart(self):
        return self.__cart
    
    @property
    def cart_list(self):
        return self.__cart_list
        
    @cart.setter
    def cart(self, new_cart):
        self.__cart = new_cart
        
    def update_cart_of_book_list(self, book):
        self.__cart_list.append(book)
        

class Writer(Account):
    def __init__(self, account_name, password):
        super().__init__(account_name, password)
        self.__money = 0
    
    @property
    def money(self):
        return self.__money
    
    def add_money(self, added_money):
        self.__money += added_money