




def total_mortgage(principal, rate, time):
    mortgage = (principal*(1 + rate/100)**time)
    print(f'Amount:{mortgage:,.2f}')

def display_title():
    print('-------------------')
    print('Mortgage Calculator')
    print('-------------------')

def main():
    display_title()    
    principal = (float(input('Enter principle')))
    rate = (float(input('Enter interest rate')))
    years = (int(input('Enter years')))

    while principal < 0:
        print('Principle must be greater than zero.')
        principal = (float(input('Enter principle')))

    while rate < 1 or rate > 10:
        print('Rate must be between 1 and 10.')
        rate = (float(input('Enter interest rate')))

    while years < 5 or years > 30:
        print('Years must be in range 5-30.')
        years = (int(input('Enter years')))

    print('Principal:', principal)
    print('Rate:', rate)
    print('Term:', years)
    total_mortgage(principal, rate, years)

main()