import datetime
from routers.Complain_class import Complain
from routers.Account_class import Reader, Writer

class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__complain_list = []
        self.__book_list = []
        self.__payment_method_list = []
        self.__promotion = None
        self.__num_of_book = 0
        self.__num_of_account = 0

    @property
    def reader_list(self):
        return self.__reader_list
    
    @property
    def writer_list(self):
        return self.__writer_list

    @property
    def complain_list(self):
        return self.__complain_list

    @property
    def book_list(self):
        return self.__book_list

    @property
    def payment_method_list(self):
        return self.__payment_method_list
    
    @property
    def promotion(self):
        return self.__promotion
    
    @promotion.setter
    def promotion(self, new_promotion):
        if self.__promotion is None:
            self.__promotion = new_promotion
        else:
            return "This promotion is not timed out."

# Add
    def add_reader(self, reader):
        self.__num_of_account += 1
        reader.id_account = self.__num_of_account
        self.__reader_list.append(reader)
        
    def add_writer(self, writer):
        self.__num_of_account += 1
        writer.id_account = self.__num_of_account
        self.__writer_list.append(writer)

    def add_complain(self, complain):
        self.__complain_list.append(complain)
        
    def add_payment_method(self, payment_method):
        self.__payment_method_list.append(payment_method)

    def upload_book(self, book, writer):
        self.__num_of_book += 1
        book.id = self.__num_of_book
        book.writer = writer
        self.__book_list.append(book)
        writer.book_collection_list.append(book)
        return "Success"

# Book
    def get_all_book(self):
        list = []
        for book in self.__book_list:
            format = {
                "id": book.id,
                "book_name" : book.name,
                "writer_name" : book.writer.account_name,
                "rating" : book.review.rating,
                "price" : book.price
            }
            list.append(format)
        if list:
            return list
        else:
            return None

    def search_reader_by_id(self, reader_id):
        for reader in self.__reader_list:
            if reader.id_account == reader_id:
                return reader
        return None
    
    def search_writer_by_id(self, writer_id):
        for writer in self.__writer_list:
            if writer.id_account == writer_id:
                return writer
        return None
    
    def search_book_by_id(self, book_id):
        for book in self.__book_list:
            if book.id == book_id:
                return book
        return None
    
    def get_coin(self, account_id):
        account = self.search_reader_by_id(account_id)
        if account is None:
            account = self.search_writer_by_id(account_id)
            if account is None:
                return "Not found account"
        return account.coin
    
    def search_book_by_bookname(self, bookname):
        new_book_list = []
        for book in self.__book_list:
            if book.name.lower() == bookname.lower() or bookname.lower() in book.name.lower():
                format = {
                    "id": book.id,
                    "book_name" : book.name,
                    "writer_name" : book.writer.account_name,
                    "type_book" : book.book_type,
                    "rating" : book.review.rating,
                    "price" : book.price
                }
                new_book_list.append(format)
        if new_book_list:
            return new_book_list
        else:
            return None

    def search_book(self,bookname=None,writer=None,type=None): #searchทุกอย่าง
        new_book_list = []
        if writer == None and type == None: #bookname
            for book in self.__book_list:
                if book.name == bookname or bookname in book.name:
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif bookname == None and type == None: #writer
            for book in self.__book_list:
                if book.writer.account_name == writer or writer in book.writer.account_name:
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif bookname == None and writer == None: #type
            for book in self.__book_list:
                if book.book_type == type:
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif type == None: #bookname writer
            for book in self.__book_list:
                if (book.writer.account_name == writer and book.name == bookname) or (writer in book.writer.account_name and book.name == bookname) or (book.writer.account_name == writer and bookname in book.name) or ( bookname in book.name and writer in book.writer.account_name):
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif writer == None: #bookname type
            for book in self.__book_list:
                if (book.name == bookname and book.book_type == type) or (bookname in book.name and book.book_type == type):
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif bookname == None: #writer type
            for book in self.__book_list:
                if (book.writer.account_name == writer and book.book_type == type) or (writer in book.writer.account_name and book.book_type == type):
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)
        elif bookname and writer and type: #bookname writer type
            for book in self.__book_list:
                if bookname in book.name and writer in book.writer.account_name and book.book_type == type:
                    format = [f'Book Name: {book.name}' , f'Writer Name: {book.writer.account_name}' , f'Type of Book: {book.book_type}']
                    new_book_list.append(format)

        if new_book_list:
                return new_book_list
        else:
                return None
            
    def search_book_by_promotion(self, promotion_name):
        books = []
        if self.__promotion is not None:
            if self.__promotion.name_festival == promotion_name:
                for book in self.__promotion.book_list:
                    format = {
                        "id": book.id,
                        "book_name" : book.name,
                        "writer_name" : book.writer.account_name,
                        "type_book" : book.book_type,
                        "rating" : book.review.rating,
                        "price" : book.price
                    }
                    books.append(format)
                return books
            return "Not found this promotion"
        return "Don't have promotion now"
    

    def show_book_info(self, book_id):
        book = self.search_book_by_id(book_id)
        if book is None:
            return 'Not found book'
        format = {
                "book_name" : book.name,
                "writer_name" : book.writer.account_name,
                "type_book" : book.book_type,
                "intro" : book.intro,
                "rating" : book.review.rating,
                "price" : book.price,
                "rating" : book.review.rating,
                "promotion" : book.get_promotion_info()
            }
        return format
        
            
    def show_book_collection_of_writer(self,writer_name):
        book_collection = []
        for account in self.__writer_list:
            if account.account_name == writer_name:
                for book in account.book_collection_list:
                    format = {
                        "id": book.id,
                        "book_name" : book.name,
                        "writer_name" : book.writer.account_name,
                        "type_book" : book.book_type,
                        "intro" : book.intro,
                        "rating" : book.review.rating,
                        "price" : book.price
                    }
                    book_collection.append(format)
                return book_collection
        return "Not found account"
    
    def show_book_collection_of_reader(self, reader_id):
        book_collection = []
        account = self.search_reader_by_id(reader_id)
        if account is not None:
            for book in account.book_collection_list:
                format = {
                    "id": book.id,
                    "book_name" : book.name,
                    "writer_name" : book.writer.account_name,
                    "type_book" : book.book_type,
                    "intro" : book.intro,
                    "rating" : book.review.rating,
                    "price" : book.price
                }
                book_collection.append(format)
        if book_collection:
            return book_collection
        else:
            return "No Book"

# Cart
    def add_book_to_cart(self, book_id, reader_id):
        book = self.search_book_by_id(book_id)
        if book is not None:
            reader = self.search_reader_by_id(reader_id)
            if reader is not None:
                if book not in reader.cart.book_cart_list and book not in reader.book_collection_list:
                    reader.cart.add_book_to_cart(book)
                    return "Success"
                elif book in reader.book_collection_list:
                    return "You already have this book"
                elif book in reader.cart.book_cart_list:
                    return "Book is already in the cart"
            return "Not found this account"  
        return "Not found this book"  
    
    def remove_book_from_cart(self, reader_id, book_id):
        reader = self.search_reader_by_id(reader_id)
        if reader is not None:
            if reader.cart is not None:
                for book in reader.cart.book_cart_list:
                    if book.id == book_id:
                        reader.cart.book_cart_list.remove(book)
                        return "Book removed from the cart"
                return "Book not found in the cart"
            else:
                return "Reader's cart is empty"
        else:
            return "Reader not found"
        
    def show_reader_cart(self, reader_id):
        reader = self.search_reader_by_id(reader_id)
        if reader is not None:
            if reader.cart is not None and reader.cart.book_cart_list:
                cart_info = []
                for book in reader.cart.book_cart_list:
                    cart_info.append({"name": book.name, "price": book.price, "id": book.id})
                return cart_info
            else:
                return "Reader's cart is empty"
        else:
            return "Reader not found"
        
    def select_book_checkout(self, reader_id, book_ids):
        reader = self.search_reader_by_id(reader_id)
        if reader is not None:
            if reader.cart is not None and reader.cart.book_cart_list:
                selected_books = [book for book in reader.cart.book_cart_list if book.id in book_ids]
                if selected_books:
                    total_coin = sum(book.price for book in selected_books)
                    return {"message": "Books selected for checkout", "total_coin": total_coin, "list book": book_ids}
                else:
                    return {"error": "Invalid book selection"}
            else:
                return {"error": "The shopping cart is empty."}
        else:
            return {"error": "The reader does not exist."}

# History
    def show_cointrasaction_history(self,account_id):
        coin_tran_list = []
        account = self.search_reader_by_id(account_id)
        if account is None:
            account = self.search_writer_by_id(account_id)
            if account is None:
                return "Not Found Account"
        
        for info in account.coin_transaction_history_list:
            if info.type == "buy" or info.type == "rent":
                coin_tran_list.append(f"You {info.type} books by using {info.coin} coin on {info.date_time}.")
            elif info.type == "top up" or info.type == "exchange":
                coin_tran_list.append(f"You {info.type} {info.coin} coin on {info.date_time}.")
        if coin_tran_list:
            return coin_tran_list
        else:
            return "Not History"
        
    def show_payment_history(self,account_id):
        payment_list = []
        account = self.search_reader_by_id(account_id)
        if account is not None:
            for data in account.payment_history_list:
                payment_list.append(f"You top up {data.money} Bath on {data.date_time}")
        account = self.search_writer_by_id(account_id)
        if account is not None:
            for data in account.payment_history_list:
                payment_list.append(f"You exchange coins for {data.money} Bath on {data.date_time}")
        if payment_list:
            return payment_list
        else:
            return "No History"

# Money
    def show_payment_method(self):
        channels = []
        for c in self.__payment_method_list:
             format = {
                 "id":c.channel_id,
                "name":c.channel_name
             }
             channels.append(format)
        return channels

    def top_up(self, id_account, money, channel):
        account = self.search_reader_by_id(id_account)
        if account is not None:  
            for c in self.__payment_method_list:
                if c.channel_id == channel:
                    if money % 2 == 0:
                        coin = money/2
                        date_time = datetime.datetime.now()
                        account.add_coin(coin)
                        account.update_payment_history_list(money,date_time)
                        account.update_coin_transaction_history_list(coin,date_time,"top up")
                        return "Success"
                    else : return "Please increse/decrese money 1 Baht"
            return "Not Found Channel"
        return "Don't Have any Account"
    def exchange(self, writer_id, coin):
        account = self.search_writer_by_id(writer_id)
        if account is not None:
            if account.coin >= coin:
                money = coin*2
                date_time = datetime.datetime.now()
                account.add_money(money)
                account.lost_coin(coin)
                account.update_payment_history_list(money,date_time)
                account.update_coin_transaction_history_list(coin, date_time, "exchange")
                return "Success"
            return "You don't have enough coin"
        return "Not found your account"

# Buy / Rent
    def rent_book(self, reader_id, book_id_list):
        account = self.search_reader_by_id(reader_id)
        if account is None:
            return "Account not found"

        for book_id in book_id_list:
            book = self.search_book_by_id(book_id)
            if book is None:
                return f"Book not found"
            
            if book in account.book_collection_list:
                return f"You already have book"
            
            if account.coin < book.price:
                return f"Not enough coins"
            
            account.lost_coin(book.price)
            account.update_book_collection_list(book)
            date_time = datetime.datetime.now()
            account.update_coin_transaction_history_list(book.price, date_time, "rent")
            book.add_num_of_reader(1)
            book.update_book_status("Rent")
            book.writer.add_coin(book.price)

        return f"Success"
    

    def rent_book(self, reader_id, book_id_list):
        account = self.search_reader_by_id(reader_id)
        if account is None:
            return "Account not found"

        for book_id in book_id_list:
            book = self.search_book_by_id(book_id)
            if book is None:
                return f"Book not found"
            
            if book in account.book_collection_list:
                return f"You already have book"
            
            new_book_price = book.price * 0.8
            if account.coin < new_book_price:
                return f"Not enough coins"
            
            account.lost_coin(new_book_price)
            account.update_book_collection_list(book)
            date_time = datetime.datetime.now()
            account.update_coin_transaction_history_list(new_book_price, date_time, "rent")
            book.add_num_of_reader(1)
            book.update_book_status("Rent")
            book.writer.add_coin(new_book_price)

        return f"Success"
    
# Review
    def add_rating(self, book_id, rating):
        book = self.search_book_by_id(book_id)
        if book is not None:
            if rating < 0 or rating >5:
                return "Please rate this book in 0-5"
            else:
                book.review.add_rating(rating)
                return book.review.rating
        return "Not found book"
    
    def submit_comment(self, reader_id, book_id, message):
        reader_account = self.search_reader_by_id(reader_id)
        if reader_account is not None:
            book = self.search_book_by_id(book_id)
            if book is not None:
                book.review.add_comment(reader_account, message)
                return "Success"
            return "Not found book"
        return "Not found account"

    def view_comment(self, book_id):
        comment_list = []
        book = self.search_book_by_id(book_id)

        if book is not None:
            for account, comment, date_time in book.review.comment_list:
                format = {
                    "account" : account.account_name,
                    "comment" : comment,
                    "datetime" : date_time
                }
                comment_list.append(format)
            return comment_list
        return "Not found book"


# Complain
    def submit_complaint(self, user_id, message):
        complain = Complain(user_id, message)
        
        user = self.search_reader_by_id(user_id)
        if user is None:
            user = self.search_writer_by_id(user_id)
            if user is None:
                return "Not found account"
            
        date_time = datetime.datetime.now()
        complain.date_time = date_time
        self.__complain_list.append((user.account_name, message, complain.date_time))
        return "Success"

    def view_complaints(self):
        if not self.complain_list:
            return "No complaints available."
        complaints_info = []
        for account, message, datetime in self.__complain_list:
            format = {
                "account": account,
                "message": message,
                "datetime": datetime
            }
            complaints_info.append(format)
        if complaints_info == []:
            return "Have no complain."
        return complaints_info

    def login(self, account_name, password):
        for account in self.__reader_list:
            if account.account_name == account_name and account.password == password:
                return account.id_account, "reader"
        for account in self.writer_list:
            if account.account_name == account_name and account.password == password:
                return account.id_account, "writer"
        return None, None

    def register_reader(self, account_name, password):
        for reader in self.__reader_list:
            if reader.account_name == account_name:
                return "Username already exists. Please choose another one."

        self.__num_of_account += 1
        reader = Reader(account_name, password)
        reader.id_account = self.__num_of_account
        self.__reader_list.append(reader)
        
        return "Reader registered successfully."
    
    def register_writer(self, account_name, password):
        for writer in self.__writer_list:
            if writer.account_name == account_name:
                return "Username already exists. Please choose another one."

        self.__num_of_account += 1
        writer = Writer(account_name, password)
        writer.id_account = self.__num_of_account
        self.__writer_list.append(writer)
        
        return "Writer registered successfully."