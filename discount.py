# Create a function named calculate_discount(price, discount_percent)
# that calculates the final price after applying a discount.
# The function should take the original price (price) and
# the discount percentage (discount_percent) as parameters.
# If the discount is 20% or higher, apply the discount; otherwise,
# return the original price.
def calculate_discount(price, discount_percent):
    discount_percent = discount_percent/100
    minimum_discount = 20/100
    discounted_price = price * discount_percent
    if discount_percent < minimum_discount:
        return price
    return price - discounted_price


def check_int(string):
    if string.isdigit():
        string = float(string)
    else:
        print("Enter a valid number, price cannot be a string")
        return

    return string


# Using the calculate_discount function,
# prompt the user to enter the original price of an item
# and the discount percentage.
# Print the final price after applying the discount,
# or if no discount was applied,
# print the original price.
def main():
    while True:
        amount = input(
            "Enter the original price (or type 'exit' to quit):R")
        if amount.lower() in ['exit', 'quit']:
            break

        amount = check_int(amount)
        if amount is None:
            continue

        discount = input("Enter your discount rate:%")
        if discount.lower() in ['exit', 'quit']:
            break

        discount = check_int(discount)
        if discount is None:
            continue

        price_to_pay = calculate_discount(amount, discount)
        print(f"The final price after applying {
              discount}% discount is R{price_to_pay}")


if __name__ == "__main__":
    main()
