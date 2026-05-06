import os

DB_FILENAME = "medicines.txt"

def load_all_medicines():
    # This loads all the data from txt file and returns list of dictionary.
    med_list = []
    
    try:
        with open(DB_FILENAME, "r") as f:
            lines = f.readlines()
            for row in lines:
                row = row.strip()
                if row == "":
                    pass
                else:
                    data = row.split(",")
                    if len(data) == 6:
                        med_info = {
                            "med_name": data[0].strip(),
                            "company": data[1].strip(),
                            "qty_in_stock": int(data[2].strip()),
                            "tab_price": float(data[3].strip()),
                            "strip_price": float(data[4].strip()),
                            "tabs_per_strip": int(data[5].strip())
                        }
                        med_list.append(med_info)
    except FileNotFoundError:
    # This here returns an empty list of dictionary if there is no information in the txt file.
        print("Warning: medicines.txt not found. Starting with an empty inventory.")
        
    return med_list

def save_all_medicines(med_list):
    # This here overwrites the file with the updated list.
    with open(DB_FILENAME, "w") as f:
        for item in med_list:
            f.write(f"{item['med_name']}, {item['company']}, {item['qty_in_stock']}, {int(item['tab_price'])}, {int(item['strip_price'])}, {item['tabs_per_strip']}\n")

def show_inventory(med_list):
    print("\n" + "="*80)
    print(f"{'ID':<5} {'Medicine Name':<25} {'Brand/Company':<15} {'Stock':<10} {'Per Tab':<10} {'Per Strip':<10}")
    print("-" * 80)
    
    counter = 1
    for item in med_list:
        print(f"{counter:<5} {item['med_name']:<25} {item['company']:<15} {item['qty_in_stock']:<10} Rs.{item['tab_price']:<9} Rs.{item['strip_price']:<10}")
        counter += 1
        
    print("="*80 + "\n")

def ask_for_number(msg, min_value=0):
    # Here is the code for asking the user until he types a valid number.
    while True:
        user_input = input(msg)
        try:
            num = int(user_input)
            if num < min_value:
                print(f"Oops! The number cannot be less than {min_value}.")
            else:
                return num
        except ValueError:
            print("Invalid input! Please enter a number instead of text.")
