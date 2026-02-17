def apply_discount(price,discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    if price<=0:
        return "The price should be greater than 0"
    if discount<0 or discount>100:
        return "The discount should be between 0 and 100"
    
    return price * (1 - discount / 100)

if __name__ == "__main__":
    while True:
        print("\n--- Discount Calculator ---")
        price_input = input("Enter price (or 'q' to quit): ")
        
        if price_input.lower() == 'q':
            print("Exiting...")
            break
            
        discount_input = input("Enter discount percentage: ")
        
        try:
            p = float(price_input)
            d = float(discount_input)
            result = apply_discount(p, d)
            if isinstance(result, (int, float)):
                print(f"Final Price: {result:.2f}")
            else:
                print(result)
        except ValueError:
            print("Error: Please enter valid numbers.")