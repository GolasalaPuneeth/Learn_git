from abc import ABC, abstractmethod

class IRepo(ABC):
    @abstractmethod
    def create_customer(self,customer):
        ...
    @abstractmethod
    def get_customer(self,cus_id):
        ...
    @abstractmethod
    def get_customers(self):
        ...
    @abstractmethod
    def update_customer(self,cus_id,f_name,country,age):
        ...
    @abstractmethod
    def delete_customer(self,cus_id):
        ...
