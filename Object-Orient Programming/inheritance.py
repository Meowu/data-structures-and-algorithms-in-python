from .class_definition import CreditCard


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, account, limit, apr):
        """Create a new predatory credit card instance.
        The initial balance is zero.
        
        """
        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        :param price: 
        :return: Return True if charge was processed.
        :return: False and assess $5 fee if charge if denied.
        """
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""

        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor
