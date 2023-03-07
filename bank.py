## Week 2 assignment

amount1 = int(input('Enter amount1(in cent): '))
amount2 = int(input('Enter amount2(in cent): '))

ttl_amount = amount1 + amount2

# converting cents to euros
euros = total_amount // 100
cents = total_amount % 100

print('The total amount is €{}.{}'.format(euros, cents))