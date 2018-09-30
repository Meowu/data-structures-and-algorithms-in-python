class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, account, limit):
        """Create a new credit card instance
            
        The initial balance is zero.
        customer    the name of the customer
        bank        the name of the bank
        account     the account identifier
        limit       credit limit
        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name"""
        return self._bank

    def get_account(self):
        """return the card identifying number(typically stored as a string)"""
        return self._account

    def get_limit(self):
        """Return credit card limit"""
        return self._limit

    def get_balance(self):
        """return current balance"""
        return self._balance

    def charge(self, price):
        """return true if charge was processed, else return false"""
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """process payment that reduces balance"""
        self._balance -= amount
