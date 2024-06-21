# simple_interest.py
def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    :param principal: The principal amount
    :param rate: The rate of interest per year
    :param time: The time the money is invested for in years
    :return: The simple interest
    """
    return (principal * rate * time) / 100

if __name__ == "__main__":
    # Sample inputs for demonstration
    principal = 1000  # in dollars
    rate = 5  # annual interest rate in percent
    time = 2  # in years
    
    interest = calculate_simple_interest(principal, rate, time)
    print(f"The simple interest is: ${interest}")
