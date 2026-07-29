Scope Summary (The LEGB Rule)
Python looks up variables in a strict order of scopes, known as the LEGB hierarchy:

Local: Inside the current function.
Enclosing: Inside any parent nested functions.
Global: Outside all functions at the top level of the file.
Built-in: Python's pre-installed names (like print or len).
Global Scope (whiteboard)
    └── Outer Function Scope (assistant's notebook)
        └── Inner Function Scope (your napkin note)



        Real-World Application
Scope boundaries are the primary security mechanisms used to isolate user data in multi-user applications, such as secure mobile banking systems.

In a banking application:

Global Scope: Constant global values like MAX_DAILY_WITHDRAWAL_LIMIT = 1000.00 are set at the top level. They are read-only and accessible by all functions.
Local Scope: When a customer requests a transaction, the app runs a transaction function. Inside that function, variables like requested_transfer_amount and recipient_account are created locally. They only exist in memory for the duration of that specific transfer, and are completely erased from RAM the moment the transaction completes.
If a developer mistakenly declared requested_transfer_amount as a global variable instead of a local one, the transaction amount from one customer could remain stuck in memory. When a completely different customer logged in and initiated a transfer, the application might read the previous customer's transfer amount, moving incorrect funds and violating privacy. Restricting variables to local scopes and managing their lifetimes is what keeps digital systems secure and reliable.
