def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * discount_percent / 100
        final_price = price - discount
        return final_price
    else :
            price
original_price = float(input("Enter the original price"))  
discount_percent = float(input ("Enter the discount percentage"))          

final_price = calculate_discount(original_price, discount_percent) 
print("Final price:", final_price)


      