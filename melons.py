"""Classes for melon orders."""
import random
import datetime

class TooManyMelonsError(ValueError):
    def __init__(self):
        super().__init__("No more than 100 melons!")

class AbstractMelonOrder():

    def __init__(self, species, qty, tax):
        """Initialize melon order attributes."""
        #self.order_type = order_type
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax

        if qty > 100:
            raise TooManyMelonsError

    def get_base_price(self):

        base_price = random.randint(5, 10)

        now = datetime.datetime.now()

        if now.weekday() < 5 and 8 <= now.hour <= 11:
            base_price += 4
       
        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas":
            base_price = self.get_base_price() * 1.5
        else:
            base_price = self.get_base_price()

        total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    #order1 = DomesticMelonOrder("cantaloupe", 8)
    order_type = "domestic"
    
    def __init__(self, species, qty):
        super().__init__(species, qty, tax = 0.08)
 
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    #order0 = InternationalMelonOrder("watermelon", 6, "AUS")

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, tax = 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

    def get_total(self):
        parent_total = super().get_total()
        if self.qty < 10:
            parent_total += 3
        return parent_total

    
    
class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty, passed_inspection = False):
        super().__init__(species, qty, 0.17)
        self.passed_inspection = passed_inspection
    
    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True
#     #order2 = GovernmentMelonOrder("watermelon", 5)
# now = datetime.datetime.now()
# print(now.hour)






# >>> try:
# ...     ?
# ... except TooManyMelonErrors:
# ...     print “No more than 100 melons!”
# if self.qty > 100
#    raise TooManyMelonErrors(“No more than 100 melons!”)