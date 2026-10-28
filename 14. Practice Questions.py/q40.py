#write a function called discount_price that takes original_price and discount_percent as parameter and prints the final price after discount

def discount_price(original_price,discount_percent):
    final_price=original_price-(original_price*discount_percent/100)
    print(f" Final Price is {final_price}")
discount_price(899,5)