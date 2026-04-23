
# It creates an empty list to store medicines
medicines = []

# It opens the file and reads the data
file = open("medicines.txt", "r")
data = file.readlines()
file.close()

# It processes each line and stores it in dictionary format in the list "medicines".
#  Each line is stripped of whitespace, split by commas, and the relevant details are
#  stored in a dictionary with appropriate keys. The stock, price per tablet, price per
#  strip, and tablets per strip are converted to integers for easier manipulation later on.
for line in data:
    line = line.strip() 
    parts = line.split(",")
    medicine = {
        "name": parts[0],
        "brand": parts[1],
        "stock": int(parts[2]),
        "price_tablet": int(parts[3]),
        "price_strip": int(parts[4]),
        "tablets_per_strip": int(parts[5])
    }

    medicines.append(medicine)

# It displays all the details of medicines stored in the dictionary in a formatted manner.
print("\n--- Available Medicines ---\n")

for m in medicines:
    print("Medicine Name :", m["name"])
    print("Brand         :", m["brand"])
    print("Stock         :", m["stock"], "tablets")
    print("Price/Tablet  : Rs.", m["price_tablet"])
    print("Price/Strip   : Rs.", m["price_strip"])
    print("Tablets/Strip :", m["tablets_per_strip"])
    print("-------------------------")
