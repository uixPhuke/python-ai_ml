class Laptop:
    storage_type="SSD"

    def __init__(self,RAM,Storage):
        self.RAM=RAM
        self.Storage=Storage

    def info(self):
        print(f"Laptop has {self.RAM} GB RAM and {self.Storage} GB {self.storage_type}")

l1=Laptop("8","512")

l1.info()

#instance

#1. 1st params-->self
# 2.Access The class & Instance Attribute