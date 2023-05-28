from random import shuffle
from abc import ABC, abstractmethod


class SupportTicket:
    def __init__(self, customer, description) -> None:
        self.customer_name = customer
        self.issue = description


def fifo_order(list):
    return list


def lifo_order(list):
    new_list = list.copy()
    return reversed(new_list)


def random_order(list):
    new_list = list.copy()
    shuffle(new_list)
    return new_list


class CustomerSupport:
    def __init__(self, processing_strategy) -> None:
        self.tickets = []
        self.strategy = processing_strategy

    def create_ticket(self, customer, description):
        self.tickets.append(SupportTicket(customer, description))

    def process_tickets(self):
        ticket_list = self.strategy(self.tickets)
        for ticket in ticket_list:
            print(ticket.customer_name)


app = CustomerSupport(random_order)

app.create_ticket("James", "Unable to discover FREs")
app.create_ticket("Ken", "Attribute error in TPE json")
app.create_ticket("lohan", "random iusse")


app.process_tickets()
