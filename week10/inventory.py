# AI USE: Generator (Claude wrote the exercise code; I reviewed every line and wrote the reflection answers myself)
#
# Reflection
# 1. What is the most surprising thing about how lists work in Python
#    compared to what you expected coming in?
#    [Your 2-3 sentences]
#
# 2. Describe one real business situation where a Python list would have
#    saved you time compared to doing it manually in Excel.
#    [Your 2-3 sentences]


# --- Exercise 1 ---
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# --- Exercise 2 ---
middle = len(inventory) // 2  # middle position computed from the length
print(inventory[0])            # first item (positive index)
print(inventory[-1])           # last item (negative index)
print(inventory[middle])       # middle item

# --- Exercise 3 ---
print(inventory[:3])    # first three
print(inventory[-2:])   # last two
print(inventory[::2])   # every other item

# --- Exercise 4 ---
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# --- Exercise 5 ---
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples can't be changed, which is good for coordinates: a location "
          "should stay fixed so no part of the program can accidentally move it.")
print(coords)

# --- Exercise 6 ---
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average:.1f}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

# --- Exercise 7 ---
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))  # 10% off, rounded to cents
print(f"Original:   {prices}")
print(f"Discounted: {discounted}")

# --- Exercise 8 ---
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for day in sales:
    if day > 300:
        high_sales.append(day)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")
