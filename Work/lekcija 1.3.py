principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
months=0

while principal > 0:
    months += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment


    if extra_payment_start_month<= months <= extra_payment_end_month:
        total_paid += extra_payment
        principal -= extra_payment
    if principal<0:
        total_paid+= principal
        principal=0

        print(months, round(total_paid, 2), round(principal,  2))
    print('Total paid', round(total_paid, 2))
    print('months', months)




