#Design & create an online store for Products (name, price).
#Track total products being created.
#Create a static method to calculate discount on each product based on a % parameter.

class ProductStore:
    store_name="Infotech"
    count=0

    def __init__(self,name,price):  #Constructor
        self.name=name
        self.price=price
        ProductStore.count+=1
        #self.count+=1. #This count will different for this particular count

    def info(self):    #instance method
        print(f"{self.name} Price is Rs. {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total no. of Product in STORE= {cls.count}")

    @staticmethod
    def cal_percentage(price,discount):
        total_discount=price-(price*discount/100)
        print(f"The Discount Received= {total_discount}")

p1=ProductStore("Laptop",100_000)
p2=ProductStore("Phone",10_000)
p3=ProductStore("Headphone",2_000)

p1.info()#1

ProductStore.get_count()#2

p1.cal_percentage(p2.price,12)#3
