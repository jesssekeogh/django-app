class Stocks():

    def __init__(self, sell_price, shares_amount, buy_price = 0):
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.shares_amount = shares_amount
    
    def capital_gain(self):
        gain = float(self.sell_price) - float(self.buy_price)
        gain = gain * self.shares_amount
        format_gain = "{:.2f}".format(gain)

        return format_gain
    
    def tax_due(self):
        #cgt_exemption = 1270
        tax = float(self.capital_gain()) * 0.33
        #if tax < 1270:
        #    tax = 0
        #else:
        if tax < 0:
            tax = 0 #- cgt_exemption
        format_tax = "{:.2f}".format(tax)
    
        return format_tax
    
    def tax_due_cgt(self):
        cgt_exemption = 1270
        tax = float(self.capital_gain()) * 0.33
        if tax < 1270:
            tax = 0
        else:
            tax = tax - cgt_exemption
        format_tax = "{:.2f}".format(tax)
    
        return format_tax

class real_estate():

    def __init__(self, sell_price, buy_price):
        self.buy_price = buy_price
        self.sell_price = sell_price

    def capital_gain_realestate(self):
        gain = float(self.sell_price) - float(self.buy_price)
        return gain
    
    def tax_due_realestate(self):
        cgt_exemption = 1270
        tax = float(self.capital_gain_realestate()) * 0.33
        if tax < 1270:
            tax = 0
        else:
            tax = tax - cgt_exemption
    
        return tax



#shares = Stocks(5000,1,4000)

#house = real_estate(25000,10000)

#print house.tax_due_realestate()
