#Q81
#Construct a dict containing four product names and their prices. Prompt the user to enter a prouct name. Use the in keyword to check if it exists; if so, display its price. Otherwise, inform the user 'Product not found'.

Products = {
    "Fan": 1599,
    "Saree": 2499,
    "Phone": 179000,
    "Jeans": 1600,
}

product_name = input("Enter Product Name:")
ans = Products.get(product_name)
if product_name in Products:
    print(f"Price of {product_name} is {ans}")
else:
    print("Product not found")