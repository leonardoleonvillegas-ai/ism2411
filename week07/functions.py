#1. The first bug was a missing colon on the second for loop. I found it from the traceback since it was a SyntaxError. The total = sale bug didn’t crash, so I needed print() to catch it. That tells me I lean on error messages and need to check values more.
#2 It takes a price and a tier (“gold,” “silver,” “bronze”) and returns the discounted price: 15%, 10%, 5%, or 0%. Yes, a colleague could use it from the name alone.
#3 For exercise 5 I checked to make sure that the code was running properly, I used Claude.


# --- Exercise 1 ---
# Define calculate tax function
def calculate_tax(price, rate):
    return price * rate

# Calling the function 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}") #7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}")  #20.00 
print(f"Another Tax: ${calculate_tax(150,0.05):.2f}") #7.50 

# ---Exercise 2---
def apply_discount(price, tier): 
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price *0.95
    else:
        return price

#Calling the function
price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# ---Exercise 3---
# Using both functions together
discounted = apply_discount(200, "gold")
after_tax = discounted + calculate_tax(discounted, 0.07)

print(f"After gold discount: ${discounted:.2f}") #170.00
print(f"After tax: ${after_tax:.2f}") #181.90

# Define final price function
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)

#Calling the function
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}') #181.90

# ---Exercise 4---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# ---Exercise 6---
x = 100   

def double_it():
    x = 999   
    return x * 2

print(x)           
print(double_it()) 
print(x)           

# 1. The first bug was a missing colon on the second for loop. I found it from the traceback since it was a SyntaxError and nothing ran. The total = sale bug didn’t crash, so I needed print() to catch it. That tells me I lean on error messages and need to check values more.