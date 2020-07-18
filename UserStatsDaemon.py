"""
This Daemon is for updating User Stats,
This includes:
    1. Calculating net worth based on user portfolio and
        adding new entry to the Users.net_worth table
    2. Updating any other stats

Steps for getting net worth
    1. Get list of ALL stocks associated with a user
    2. Get current best price of that stock
    3. Calculate total net worth based on stock price and quantity in portfolio
    4. Populate Users.net_worth with value and a new net_worth_ts
"""



