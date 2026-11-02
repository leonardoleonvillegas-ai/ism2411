# 1. If order_total = 350 goes through my tier logic. It checks if total >= 500, and 350 is not >= 500
# it then skips down to the next check. Then it checks if total >= 200, and 350 is
# bigger than 200 so that one is true. So discount gets set to 10%. Once that
# condition is true python stops checking the rest of the elif/else because it
# already found a match. So final price ends up being 315.00.
#
# 2. if total > 100 and total < 500 is one condition made of two parts joined
# with so both parts have to be true at the same time for the code inside to
# run. Two separate if statements are different because each one runs on its own.
# If both separate ifs happen to have the same body they might look like they give the
# same result, but they don't behave the same way.
#
# 3. As a finance major I feel like I run into tiered conditional logic basically
# everywhere. Shipping fees are an example. Knowing Python conditionals helps me see
# these systems as if/elif/else. It kind of makes the finance side of things feel more logical.

# Exercise 1
total = float(input("Enter cart total: $"))

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")
print(f"Final price: ${final:.2f}")

# Exercise 2 
total = 750  

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

final = total * (1 - discount)

if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"

print(f"Status: {status}")

# Exercise 3
region = "South"
total = 250

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

bonus = 0
if region == "South" and total >= 100:
    bonus = 0.02
    print("Region bonus applied: additional 2% off")

final_discount = discount + bonus
final = total * (1 - final_discount)
print(f"Final discount: {final_discount*100:.0f}%")
print(f"Final price: ${final:.2f}")

# Exercise 4 
region = "South"
total = 150
customer_type = "wholesale"

if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03
else:
    extra_discount = 0

print(f"Extra discount: {extra_discount*100:.0f}%")

#Exercise 5
for amount in [-50, 500, 15000]:
    if amount <= 0:
        result = "SUSPICIOUS"
    elif amount >= 10000:
        result = "LARGE — REVIEW REQUIRED"
    else:
        result = "NORMAL"
    print(result)

# Exercise 6
total_spent = 2500
orders = 5
has_outstanding_balance = False

qualifies = (total_spent > 2000 or orders > 10) and not has_outstanding_balance

if qualifies:
    print("Qualifies for VIP upgrade")
else:
    print("Does not qualify for VIP upgrade")
