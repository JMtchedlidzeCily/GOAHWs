def check_discount(age):
    if age >= 18:
        return "You are not eligible for a discount."
    else:
        return "You are eligible for a discount."

# Example usage:
discount_status = check_discount(20)
print(discount_status)  # Output: You are not eligible for a discount.

discount_status = check_discount(16)
print(discount_status)  # Output: You are eligible for a discount.
