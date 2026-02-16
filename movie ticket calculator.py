base_price = int(input('Enter the base price of the ticket: '))
age = int(input('Enter the age of the user: '))
seat_type = input('Enter the seat type (Standard/Premium/Gold): ')
show_time = input('Enter the show time (Morning/Evening): ')

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

member_check = input('Is the user a member? (yes/no): ').lower()
if member_check == 'yes':
    is_member = True
    print('User is a member')
else:
    is_member = False
    print('User is not a member')

weekend_check = input('Is it a weekend? (yes/no): ').lower()
if weekend_check == 'yes':
    is_weekend = True
    print('It is a weekend')
else:
    is_weekend = False
    print('It is not a weekend')

discount = 0
if is_member and age >= 21:
    discount = 25
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 33
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    if seat_type == 'Premium':
        service_charges = 45
    elif seat_type == 'Gold':
        service_charges = 55
    else:
        service_charges = 15
    print('Service charges:', service_charges)    
else:
    print('Ticket booking failed due to restrictions')
    service_charges = 0

total_price = base_price + extra_charges + service_charges - discount
print('Total price of the ticket:', total_price) 
print('Thank you for using the movie ticket calculator!')


