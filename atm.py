from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
import os

# Data Models
@dataclass(frozen=True)
class Card:
    number: str
    password: str

@dataclass(frozen=True)
class TransactionInfo:
    id: int
    timestamp: datetime
    type: str
    amount: Optional[float] = None

# Domain Entities
class Account:
    def __init__(self, account_number: str):
        self.account_number = account_number
        self._balance: float = 0.0
        self._card: Optional[Card] = None
        self._transactions: List[TransactionInfo] = []

    @property
    def balance(self) -> float:
        return self._balance

    def link_card(self, card: Card) -> None:
        self._card = card

    def has_card(self, card_number: str, password: str) -> bool:
        return self._card and self._card.number == card_number and self._card.password == password

    def add_transaction(self, transaction: TransactionInfo) -> None:
        self._transactions.append(transaction)

    def get_transactions(self) -> List[TransactionInfo]:
        return self._transactions.copy()

class Customer:
    def __init__(self, name: str, address: str, phone: str, email: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self._accounts: List[Account] = []

    def add_account(self, account: Account) -> None:
        self._accounts.append(account)

    def find_account(self, card_number: str, password: str) -> Optional[Account]:
        return next((account for account in self._accounts 
                    if account.has_card(card_number, password)), None)

class Bank:
    def __init__(self, name: str, swift_code: str):
        self.name = name
        self.swift_code = swift_code
        self._customers: List[Customer] = []

    def add_customer(self, customer: Customer) -> None:
        self._customers.append(customer)

    def authenticate(self, card_number: str, password: str) -> Optional[Account]:
        return next((account for customer in self._customers 
                    for account in [customer.find_account(card_number, password)] 
                    if account), None)

# Interfaces
class Display:
    def show(self, message: str) -> None:
        print(message)

    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

class Input:
    def read(self, prompt: str) -> str:
        return input(prompt)

# Transactions
class Transaction(ABC):
    _counter: int = 0

    def __init__(self, type: str, amount: Optional[float] = None):
        self.info = TransactionInfo(
            id=Transaction._counter,
            timestamp=datetime.now(),
            type=type,
            amount=amount
        )
        Transaction._counter += 1

    @abstractmethod
    def execute(self, account: Account) -> bool:
        pass

class Withdraw(Transaction):
    def __init__(self, amount: float):
        super().__init__("Withdraw", amount)

    def execute(self, account: Account) -> bool:
        if self.info.amount > 0 and account.balance >= self.info.amount:
            account._balance -= self.info.amount
            account.add_transaction(self.info)
            return True
        return False

class Deposit(Transaction):
    def __init__(self, amount: float):
        super().__init__("Deposit", amount)

    def execute(self, account: Account) -> bool:
        if self.info.amount > 0:
            account._balance += self.info.amount
            account.add_transaction(self.info)
            return True
        return False

class Balance(Transaction):
    def __init__(self):
        super().__init__("Balance")

    def execute(self, account: Account) -> bool:
        account.add_transaction(self.info)
        return True

# ATM Controller
class ATMController:
    OPTIONS = {
        "1": ("Withdraw", lambda input, display: Withdraw(float(input.read("Enter amount to withdraw: ")))),
        "2": ("Deposit", lambda input, display: Deposit(float(input.read("Enter amount to deposit: ")))),
        "3": ("Balance", lambda input, display: Balance()),
        "4": ("View Transactions", None),
        "5": ("Exit", None)
    }

    def __init__(self, bank: Bank, location: str, display: Display, input: Input):
        self.bank = bank
        self.location = location
        self.display = display
        self.input = input

    def run(self) -> None:
        self.display.clear()
        card_number = self.input.read("Enter card number: ")
        password = self.input.read("Enter password: ")
        account = self.bank.authenticate(card_number, password)
        
        if account:
            self._run_menu(account)
        else:
            self.display.show("Authentication failed")

    def _run_menu(self, account: Account) -> None:
        while True:
            self.display.clear()
            self.display.show(self._format_menu())
            choice = self.input.read("Choose an option: ")
            
            if choice == "5":
                self.display.show("Ejecting card...\nGoodbye")
                break
            
            self._process_choice(choice, account)

    def _format_menu(self) -> str:
        return "\n".join(f"{key}. {value[0]}" for key, value in self.OPTIONS.items())

    def _process_choice(self, choice: str, account: Account) -> None:
        try:
            if choice not in self.OPTIONS:
                self.display.show("Invalid choice")
                return

            if choice == "4":
                self._show_transactions(account)
                return

            _, transaction_factory = self.OPTIONS[choice]
            if transaction_factory:
                transaction = transaction_factory(self.input, self.display)
                success = transaction.execute(account)
                self._show_result(transaction, account, success)

        except ValueError:
            self.display.show("Invalid amount")

    def _show_transactions(self, account: Account) -> None:
        self.display.clear()
        for t in account.get_transactions():
            amount = f"{t.amount:.2f}" if t.amount else "N/A"
            self.display.show(f"ID: {t.id}, Type: {t.type}, Amount: {amount}, Time: {t.timestamp}")

    def _show_result(self, transaction: Transaction, account: Account, success: bool) -> None:
        self.display.clear()
        if transaction.info.type == "Balance":
            self.display.show(f"Balance: {account.balance:.2f}")
        elif success:
            self.display.show(f"{transaction.info.type} successful. New balance: {account.balance:.2f}")
        else:
            self.display.show(f"Failed: Insufficient funds or invalid amount")

# Usage example
if platform.system() != "Emscripten":
    if __name__ == "__main__":
        bank = Bank("MyBank", "MYBK1234")
        customer = Customer("John Doe", "123 Main St", "555-1234", "john@example.com")
        account = Account("ACC123")
        account.link_card(Card("CARD123", "1234"))
        customer.add_account(account)
        bank.add_customer(customer)
        atm = ATMController(bank, "Main Branch", Display(), Input())
        atm.run()