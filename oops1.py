class Product:
    pass
prod = []

for i in range(1,4):
    obj = Product()
    obj.price = i *6
    prod.append(obj)

for i in prod:
    if prod.price > 10:
        print(prod.price)