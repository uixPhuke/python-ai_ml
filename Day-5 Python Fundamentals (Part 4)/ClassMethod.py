class Laptop:
    storage_type="SSD"

    def __init__(self,RAM,Storage):
        self.RAM=RAM
        self.Storage=Storage

    #This classmehod decorator made this function is---->> class
    @classmethod
    def get_storage_type(cls):
        print(f"Stoage type= {cls.storage_type}")

    def info(self): #instance method
        print(f"Laptop has {self.RAM} GB RAM and {self.Storage} GB {self.storage_type}")

l1=Laptop("8","512")

l1.get_storage_type()

#class Methods
#1.  1st params class Attributes
#2. Decoretor
#3. classMethod
# cls only access class attribute
#@classmethod    def get_storage_type(cls):
        #print(f"Stoage type= {cls.storage_type} {cls.RAM}")
        #RAM cant be accessable because it RAM is finding under class 
        #which is not available
        
