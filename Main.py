import datetime


# x = datetime.datetime.now()

# print(x)

income = 0

expenses = {
    "Rent/Mortgage" : 0,
    "Bills" : 0,
    "Fuel" : 0,
    "Food" : 0,
    "Leisure" : 0,
}


income = float(input("What's your weekly income?:  "))

for i in expenses:
    inpval = float(input('How much you pay for ' + str(i) + '?:  '))
    expenses.update({i:inpval})
    income -= inpval

print(expenses)
print(income)

print("; Expenses ; Weekly Amount ;")

for item in expenses:
    print(";", item[0],";")
          



# Make a for loop that lets the user update all the dictionary keys' values
# ask user for weekly income
# print table showing the total spent and saved (look at mirror for table)