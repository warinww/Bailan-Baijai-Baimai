class PaymentMethod:
    def __init__(self,channel_name, channel_id):
        self.__channel_name = channel_name
        self.__channel_id = channel_id
    
    @property
    def channel_name(self):
        return self.__channel_name
    
    @property
    def channel_id(self):
        return self.__channel_id