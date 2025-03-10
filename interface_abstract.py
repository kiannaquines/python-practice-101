from abc import ABC, abstractmethod

class Ticket(ABC):
    
    def __init__(self, ticket_number, ticket_amount):
        self.ticket_number = ticket_number
        self.ticket_amount = ticket_amount
        
    @abstractmethod
    def get_ticket_information(self):
        pass
    
    @abstractmethod
    def get_ticket_number(self):
        pass
    
    
    @abstractmethod
    def get_ticket_amount(self):
        pass


class BusTicket(Ticket):
    def __init__(self, ticket_number, ticket_amount):
        super().__init__(ticket_number, ticket_number)
        
    def get_ticket_information(self):
        ticket_information = f'Ticket No: {self.ticket_number} \nTicket Amount: {self.ticket_amount}'
        return ticket_information


bus_ticket = BusTicket("1234567890", "1000")
print(bus_ticket.get_ticket_information())
