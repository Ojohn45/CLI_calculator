# Task 1
# book = {
#     "title": "Kaiju no 8",
#     "author": "yuji Itadori",
#     "pages": 100
# }

# print(book["title"]) 
# print("The boy is over there")

# Task 2
# book1 = {"title": "Kaiju no 8", "author": "yuji Itadori", "pages": 100}
# book2 = {"title": "Revese Revenge", "author": "Denji uzimaki", "pages": 75}

# listed = [book1, book2]

# print(f"{book1["title"]} by {book1["author"]}")   # Things Fall Apart
# print(len(listed))       

# Task 3
# book1 = {"title": "Kaiju no 8", "author": "yuji Itadori", "pages": 100}
# book2 = {"title": "Revese Revenge", "author": "Denji uzimaki", "pages": 75}

# listed = [book1, book2]

# book3 = {"title": "Revese chain", "author": "Boruto", "pages": 159}
# listed.append(book3)

# for lis in listed:
#     print(f"{lis['title']} by {lis['author']}")

# Task 4 
# books = [
#     {"title": "Kaiju no 8", "author": "yuji Itadori", "pages": 100},
#     {"title": "Revese Revenge", "author": "Denji uzimaki", "pages": 75},
#     {"title": "Revese chain", "author": "Boruto", "pages": 159},
# ]

# total = 0

# for lis in books:
#     total += lis["pages"]

# print(f"Total pages: {total}")  

# Task 5
# expenses =  [
#     {"Item": "Beans", "Amount": 100, "Category": "Food"},
#     {"Item": "Rice", "Amount": 500, "Category": "Food"},
#     {"Item": "Bus", "Amount": 200, "Category": "Transport"},
#     {"Item": "Bike", "Amount": 50, "Category": "Transport"},
# ]

# for lis in expenses:
#     print(f"{lis['Item']} - {lis['Amount']} - {lis['Category']}")

# total = 0

# for lis in expenses:
#     total += lis["Amount"]

# print(f"Total Amount: {total}")

# Category_total = 0
# for lis in expenses:
#     if lis["Category"] == "Transport":
#         Category_total += lis["Amount"]

# print(f"Total Transport Category: {Category_total}")

# Task 6
# expenses = []   # starts empty

# name = input("Enter exepenses item: ")
# amount = int(input("Enter amount: "))
# category = input("Enter category: ")

# listed = {"name": name, "amount": amount, "category": category}
# expenses.append(listed)

# print(expenses)   

# Task 7
# expenses = []

# while True:
#     item = input("Enter exepenses item (or q to quit): ")
#     if item == "q":
#         break

#     amount_text = input("Enter amount: ")
#     if amount_text == "q":
#         break

#     category = input("Enter category: ")
#     if category == "q":
#         break

#     try:
#         amount = int(amount_text)                    # convert after the q check
#     except ValueError:
#         print("Please enter a valid number!\n")
#         continue

#     expens = {"item": item, "amount": amount, "category": category}
#     expenses.append(expens)

# total = 0
# for expense in expenses:
#     print(f"{expense['item']} - {expense['amount']} ({expense['category']})")
#     total += expense["amount"]
        

# print(f"Total: {total}")

# Task 8
expenses = []

while True:
    item = input("Enter exepenses item (or q to quit): ")
    if item == "q":
        break

    amount_text = input("Enter amount: ")
    if amount_text == "q":
        break

    category = input("Enter category: ")
    if category == "q":
        break

    try:
        amount = int(amount_text)                    # convert after the q check
    except ValueError:
        print("Please enter a valid number!\n")
        continue

    expens = {"item": item, "amount": amount, "category": category}
    expenses.append(expens)

total = 0
for expense in expenses:
    print(f"{expense['item']} - {expense['amount']} ({expense['category']})")
    total += expense["amount"]

category_totals = {}

for categori in expenses:
    category = categori["category"]
    if category in category_totals:
        category_totals[category] += categori["amount"]
    else:
        category_totals[category] = categori["amount"]

print(category_totals)
for category, totals in category_totals.items():    
    print(f"{category}: {total}")