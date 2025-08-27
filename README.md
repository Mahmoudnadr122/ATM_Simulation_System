ATM Simulation System:
A Python-based simulation of an ATM system, built using OOP principles. This project demonstrates a fully functioning banking environment that includes user authentication, balance inquiries, deposits, withdrawals, and transaction history.

Features:

- Card authentication with number & password
- Deposit and withdraw money with validation
- Real-time balance inquiry
- Transaction history logging
- Modular and extensible OOP design
- Command-line user interface

Technologies Used:

- Python 3.10+
- Object-Oriented Programming (OOP)
- `@dataclass` for data modeling
- Abstract classes (`abc`) for transactions
- Command Line Interface (CLI)
  
Project Structure :

```bash
atm_project/
│
├── models.py             # Data models like Card and TransactionInfo
├── entities.py           # Domain logic: Account, Customer, Bank
├── transactions.py       # Withdraw, Deposit, Balance operations
├── ui.py                 # Input/output interfaces
├── controller.py         # ATMController handles interaction logic
├── main.py               # Entry point
└── README.md             # This file
