"""
calculate the  early termination charge for a lease
Args:
     remaining_months: int, the number of months remaining on the lease

     difference_per_month(float): the difference between in monthly payments (R).
     
     total_months: int, the total number of months in the lease (default is 48 months)

     Returns:
        float: the early termination charge
        

"""

def calculate_early_termination_charge(remaining_months,
                                       difference_per_month,
                                       total_months=48):
    return remaining_months * difference_per_month

def main():
    try:
        #get user input
        remaining_months = int(input("Enter the number of months remaining on the lease: "))
        difference_per_month = float(input("Enter the difference in monthly payments (R): "))
        #calculate the early termination charge
        early_termination_charge = calculate_early_termination_charge(remaining_months, difference_per_month, total_months=48)
        print(f"The early termination charge for terminating a 48-month lease after {remaining_months} months: R{early_termination_charge:.2f}")
    except ValueError:
        print("Please enter a valid number")

if __name__ == '__main__':
    main() 