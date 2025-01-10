import time # Imports the time module which will be used to simulate realistic dispensing and receipt generation by adding a delay.

# Inventory System
# The 'inventory' dictionary has categories of products as keys (e.g., "SnugglePals").
# Each category maps to another dictionary, where each key is the code of an item (e.g., "SP01"),
# and the value is a list containing a products: [Name, Description, Price, Stock].
inventory = {
    "SnugglePals": {
        "SP01": ["Frosty", "a Polar Bear Plushie", 15, 5],
        "SP02": ["Cocoa", "a Grizzly Bear Plushie", 16, 5],
        "SP03": ["Bamboo", "a Panda Bear Plushie", 14.50, 5],
        "SP04": ["Snowflake", "a Husky Plushie", 17, 5],
        "SP05": ["Sunny", "a Golden Retriever Plushie", 18, 5],
    },
    "YummyBuddies": {
        "YB01": ["Creamie", "a Cheesecake Plushie", 12, 5],
        "YB02": ["Patty", "a Burger Plushie", 10.50, 5],
        "YB03": ["Cheeza", "a Pizza Plushie", 13, 5],
        "YB04": ["Syrup", "a French Toast Plushie", 9.50, 5],
        "YB05": ["Choco", "a Chocolate Bar Plushie", 5, 5],
    },
    "SippySquad": {
        "SS01": ["Yumi", "a Yakult Plushie", 3, 5],
        "SS02": ["Milky", "a Milkis Plushie", 3.50, 5],
        "SS03": ["Pearlie", "a Boba Tea Plushie", 5.50, 5],
        "SS04": ["Matchy", "a Matcha Latte Plushie", 4, 5],
        "SS05": ["Choco", "a Chuckie Plushie", 2.50, 5],
    },
}

# Recommend Items
# This function suggests other items for purchase that come from the same category
# but doesn't include the recently purchased item.
def recommend_items(category, recent_item):
    print("Based on your selection, you might also like:")
    # This shows all items in the selected category.
    for code, details in inventory[category].items():
        if code != recent_item:  # This excludes the recently selected item by checking its code.
            print(f"- [{code}] {details[0]}: {details[1]} ({details[2]}$)")
    print("\n")

# Receipt System
# This function generates a receipt for the purchased item.
def generate_receipt(item, payment, change):
    # Generates and prints out a receipt with item details, payment, and change.
    print("Generating receipt...\n")
    time.sleep(1)  # Simulates a delay by adding a one second pause.
    print("CuddleCo Vending Machine Receipt")
    print("-" * 30)  # Prints a separator line using dashes to improve formatting.
    # Print details we want to add to the receipt such as item name, description, price, payment, and change.
    print(f"Item: {item[0]} ({item[1]})")
    print(f"Price: {item[2]}$")
    print(f"Payment: {payment}$")
    print(f"Change: {change}$")
    print("-" * 30)
    print("Thank you for your purchase!\n")

# Purchase Function
# This function is responsible for the main interaction in purchasing an item.
def product_prompt(category, item_code):
    # Handles the purchase process for a selected item, including stock verification and payment.
    # Access the selected item from the inventory dictionary.
    item = inventory[category][item_code]
    # Check if the item is out of stock by comparing its stock count to zero.
    if item[3] <= 0:
        print(f"Sorry, {item[0]} is out of stock.\n")
        return

    # Prompt the user to confirm their purchase.
    answer = input(f"You chose {item[0]}, {item[1]}. That item costs {item[2]}$ and there's {item[3]} in stock. Would you like to continue with your purchase? yes/no  ").lower()
    print("\n")
    if answer == "yes":
        try:
            # Ask the user to input the payment amount then converts the input into a float for calculations.
            charge = float(input("Please insert your money amount here:  "))
            print("\n")
        except ValueError:
            # Handle invalid inputs such as non-numeric values.
            print("\nInvalid input, please enter a valid number for the payment.")
            print("\n")
            return

        if charge < item[2]:  # Check if the user has provided enough money for payment.
            print("You have inserted an insufficient amount, please try again.")
            print("\n")
        elif charge >= item[2]:  # Process the purchase if the payment is enough.
            change = round(charge - item[2], 2)  # Calculates the change to two decimal places to streamline info displayed to the user.
            print(f"Payment successful. Dispensing your item...\n")
            # Displays a countdown before dispensing the item to add realism to the vending machine.
            for count in range(3, 0, -1):
                print(f"Dispensing in {count}...")
                time.sleep(1)  # Simulates a delay by adding a one second pause.
            print(f"\nDispenser: {item[0]}\n")
            print(f"{item[0]} has been dispensed successfully.\n")
            item[3] -= 1  # Decrease the stock count by 1 to manage inventory.
            generate_receipt(item, charge, change)  # Call the receipt generation function.
            recommend_items(category, item_code)  # Call the item recommendation function.
    else:
        # If the user cancels, this will display other items from the same category as the originally selected item.
        print("No worries! Here are other items you might like:\n")
        recommend_items(category, item_code)

# Menu
# Function to display the menu of items available in the vending machine.
def display_menu():
    # Display the vending machine's welcome message.
    print("Welcome to the CuddleCo. vending machine 🧸✨\n")

    # Display the "SnugglePals" section, which has animal plushies.
    print(
    "🌟 SnugglePals: Furry Friends Edition\n" 
    f"{'Code':<6} {'Name':<12} {'Description':<20} {'Price':<8}\n" # Defines the widths for each column and left-aligns the column names.
    + "-" * 50 + "\n"  # Divider using dashes for readability
    "SP01   Frosty       Polar Bear           $15.00  \n"
    "SP02   Cocoa        Grizzly Bear         $16.00  \n"
    "SP03   Bamboo       Panda Bear           $14.50  \n"
    "SP04   Snowflake    Husky                $17.00  \n"
    "SP05   Sunny        Golden Retriever     $18.00  \n\n"
    
    # Display the "YummyBuddies" section, which has snack plushies.
    "🌟 YummyBuddies: Snacktime Squad\n"
    f"{'Code':<6} {'Name':<12} {'Description':<20} {'Price':<8}\n"
    + "-" * 50 + "\n"
    "YB01   Creamie      Cheesecake           $12.00  \n"
    "YB02   Patty        Burger               $10.50  \n"
    "YB03   Cheeza       Pizza                $13.00  \n"
    "YB04   Syrup        French Toast         $9.50   \n"
    "YB05   Choco        Chocolate Bar        $5.00   \n\n"
    
    # Display the "SippySquad" section, which has drink plushies.
    "🌟 SippySquad: Drink Delights\n"
    f"{'Code':<6} {'Name':<12} {'Description':<20} {'Price':<8}\n"
    + "-" * 50 + "\n"
    "SS01   Yumi         Yakult               $3.00   \n"
    "SS02   Milky        Milkis               $3.50   \n"
    "SS03   Pearlie      Boba Tea             $5.50   \n"
    "SS04   Matchy       Matcha Latte         $4.00   \n"
    "SS05   Choco        Chuckie              $2.50   \n"
    )

# Main Loop
# This is the main function that runs the vending machine system.
def main():
    display_menu()  # Show the menu at the start.
    # Ask the user if they want to make a purchase.
    user_decision = input("Would you like to purchase an item? yes/no  ").lower()
    print("\n")
    while user_decision == "yes":  # Continue until the user decides not to purchase.
        item_code = input("Please input the code of your desired item:  ").upper()  # Get the item code.
        print("\n")
        found = False  # Flag to track if the item code is valid.
        # Check each category for the entered item code.
        for category, items in inventory.items():
            if item_code in items:  # If the item code exists in the inventory.
                product_prompt(category, item_code)  # Start the purchase process.
                found = True  # Set the flag to True.
                break
        if not found:  # If the item code could not be found, display an error message.
            print("Invalid item code, please try again.")
            print("\n")
        # Ask the user if they want to make another purchase.
        user_decision = input("Would you like to purchase another item? yes/no  ").lower()
        print("\n")

    print("Thank you for using the CuddleCo Vending machine.")  # Exit message.

# Run the Program
# This checks if the program is being executed directly and is not imported as a module.
# If so, it will call the main function.  
if __name__ == "__main__":
    main()