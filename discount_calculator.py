# Function to calculate discounted price
def calculate_discount(original_price, discount_percentage):
    # Calculate discount
    discount_price = original_price * (discount_percentage/100)
    # Return final price
    return (original_price - discount_price)

# Calculate discount for $100 item with 10% off
discounted_price = calculate_discount(original_price=100, discount_percentage=10)

# Print result
print(discounted_price)

# Decision-making structure based on the discounted price
if discounted_price < 50:
    print("Low-cost item.")
elif 50 <= discounted_price <= 100:
    print("Moderate-cost item.")
else:
    print("High-cost item.")