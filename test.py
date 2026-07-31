stock = {"cups": 100, "lids": 150}
double_stock = {item: count * 2 for item, count in stock.items()}
print(double_stock)