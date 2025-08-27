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

![UML Diagram](https://www.plantuml.com/plantuml/dpng/dLD9Jnin5BxFhx1o6g11xNM4410kIArwGUgXgg8Nso5Ml8piDqrHslzUZvVOP2XLE7bvYx_b-SOXM1oKRAW4vyW2B2FxXf0vqODQSTiHXpQSUn_V6SlYpPycLJnQq0ue2gCVzDgaOk7JXCQmHw6uGr1zHnWW7u_n_hddfJqeCsZioDT-R0No-reQm1_beLjAnupq0CJJyXZbSWKIDFMDGtsye-1X1sxnZ0MpwyXduV3gYCQrJxmWaruNH0gz3VtQqlIi8p-DO26-0LV2DReFBmNqDIjZPAW1ncf8RRNlZlMjtthY-89AU_OFCaN4nU3GA6wpnw1g2nYptBdAyetHLPmh4BAIEdcG9Km6NMTEETwcjSiMrXpMGfV4_sgMEnH2Tw2thv9nEx769JMCLuXfefyXPpaAvfpHvartqAo63GDkk4P10VbxODyBrqju9llGpMtChbLUUdYAQEkdgEHWstHJEZpeVi1KRpcmjhT6zPZBqn-5bTy0HJBvhFcZwhMP35beodznEY2Vk9Scjo3v9d33BEp8_hIwUzuR9_3KihluAKyjkttyiZ0QhP7oCFuhqDikZ50uIaDXbA0C38isTTcl99bNlei6HFa7NVjJYtprUpu_23I9P0acWKooQH8TCliq8-S-CFjuUUct2x3irTZvR69cdj_Zl3oK8__ZMAvfcagtrCACQNuTwzu89ydUo8WAtd3D1YN_0W00)

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

