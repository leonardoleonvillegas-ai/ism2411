
# 1. Explain the accumulator pattern to a classmate (three steps + why each matters).    
#    ANSWER: You need to set a variable to 0 before the loop to give it a starting point. Inside the loop you then add each item to it. After that loop is done you print the final number.
#
# 2. While loop vs for loop: code length and trade-offs.
#    ANSWER: White loop was longer because I made it and added 1 to it myself. While the for loop does that for me. I would use a loop for the lists. 
#
# 3. Real dataset from my major / job where I'd loop to compute a summary stat.
#    ANSWER: If I was an intern at a fuel company, I could use a loop to go through a list of fuel inovces to add up the total for the month.


sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0                      
for sale in sales:
    total = total + sale       
print(f"Total: ${total}")      



sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0                      
count = 0                      
for sale in sales:
    total = total + sale       
    count = count + 1          
average = total / count        
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")



sales = [120, 80, 250, 175, 90, 410, 60, 215]
current_max = sales[0]         
for sale in sales:
    if sale > current_max:
        current_max = sale     
print(f"Largest sale: ${current_max}")   


sales = [120, 80, 250, 175, 90, 410, 60, 215]
big_count = 0                  
big_total = 0                  
for sale in sales:
    if sale > 100:
        big_count = big_count + 1      
        big_total = big_total + sale   
print(f"Sales over $100: {big_count}")       
print(f"Total of those sales: ${big_total}")



sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found — ${sale}. Stopping.")
        break                  
    if sale <= 100:
        continue               
    print(f"${sale}")



sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0                     
i = 0                          
while i < len(sales):
    total = total + sales[i]   
    i = i + 1                  
print(f"Total: ${total}")     




sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
    if sale >= 200:
        discount = 10
    elif sale >= 100:
        discount = 5
    else:
        discount = 0
    final_price = sale * (100 - discount) / 100
    amount = f"${sale}"        
    print(f"{amount:<4} → {discount}% discount → ${final_price:.2f}")
