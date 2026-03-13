#luhn Algorithm 
def verify_card_number(card_number):
    card_number=card_number.replace(' ','').replace('-','')
    digits=[int(d) for d in card_number][::-1]
    total=0
    for i in range(len(digits)):
        num = digits[i]
        if i%2==1:
            num*=2
            if num>9:
                num-=9
        total+=num        
    if total % 10 == 0:
        return "Valid!"
    else:
        return "Invalid"

if __name__ == "__main__":
    user_input = input("Enter a credit card number to verify: ")
    print(verify_card_number(user_input))