def total(items):
    return sum(i["price"] * i["qty"] for i in items)

def with_tax(amount, rate=0.17):
    return round(amount * (1 + rate), 2)
