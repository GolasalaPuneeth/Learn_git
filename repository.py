from irepository import IRepo
from sqlmodel import select
from models import Customers

class Repo(IRepo):

    def __init__(self, session):
        self.session = session

    # CREATE
    def create_customer(self, customer):
        self.session.add(customer)
        self.session.commit()
        self.session.refresh(customer)
        return customer

    # READ ONE
    def get_customer(self, cus_id):
        statement = select(Customers).where(
            Customers.cus_id == cus_id
        )
        result = self.session.exec(statement)
        customer = result.first()
        return customer

    # READ ALL
    def get_customers(self):
        statement = select(Customers)
        result = self.session.exec(statement)
        customers = result.all()
        return customers

    # UPDATE
    def update_customer(self, cus_id, f_name, country, age):
        customer = self.get_customer(cus_id)
        if customer:
            customer.f_name = f_name
            customer.country = country
            customer.age = age
            self.session.add(customer)
            self.session.commit()
            self.session.refresh(customer)
            return customer
        return None

    # DELETE
    def delete_customer(self, cus_id):
        customer = self.get_customer(cus_id)
        if customer:
            self.session.delete(customer)
            self.session.commit()
            return True
        return False

# Create session
# with Session(engine) as session:
#     repository = Repo(session)

    # READ ALL
    # repository.get_customers()

    # repository.get_customer(11)
    # CREATE
    # new_customer = Customers(
    #     cus_id=11,
    #     f_name="Gowri",
    #     country="India",
    #     age=22
    # )
    # repository.create_customer(new_customer)

    # # UPDATE
    # repository.update_customer(
    #     11,
    #     "Priya",
    #     "India",
    #     23
    # )

    # # DELETE
    # repository.delete_customer(11)


