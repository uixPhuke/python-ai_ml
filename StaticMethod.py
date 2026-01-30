#Static methods has no compulspry parameter
#Self XX
#cls XX
#Neighter can acess class or instance attribute
#using @staticMethod


class Laptop:
    storage_type="SSD"

    def __init__(self,RAM,Storage):
        self.RAM=RAM
        self.Storage=Storage

    
    @classmethod
    def get_storage_type(cls):
        print(f"Stoage type= {cls.storage_type}")

    def info(self): #instance method
        print(f"Laptop has {self.RAM} GB RAM and {self.Storage} GB {self.storage_type}")


    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"discounted Price ={final_price}")


l1=Laptop("8","512")

l1.calc_discount(40_000,10)
