import json
import os

shopping_cart = []

# ---------------- FILE HANDLING ----------------

def load_products():
    if os.path.exists("products.json"):
        with open("products.json", "r") as file:
            return json.load(file)
    return []

def save_products(products):
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)

# Load products permanently
products = load_products()

# ---------------- ADMIN LOGIN ----------------

ADMIN_USER = "admin"
ADMIN_PASS = "admin123"

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == ADMIN_USER and password == ADMIN_PASS:
        print("\nWelcome Admin!")
        admin_panel()
    else:
        print("\nWelcome Customer!")
        show_products()

# ---------------- ADMIN PANEL ----------------

def admin_panel():
    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. View Products")
        print("2. Increase Quantity")
        print("3. Decrease Quantity")
        print("4. Adjust Price")
        print("5. Add Product")
        print("6. Logout")

        choice = input("Choose => ")

        if choice == '1':
            admin_view_products()
        elif choice == '2':
            increase_quantity()
        elif choice == '3':
            decrease_quantity()
        elif choice == '4':
            adjust_price()
        elif choice == '5':
            add_product()
        elif choice == '6':
            break
        else:
            print("Invalid choice")

def admin_view_products():
    for item in products:
        print(f"ID: {item['id']} | {item['title']} | Qty: {item['quantity']} | Price: {item['price']}")

# ---------------- ADD PRODUCT ----------------

def add_product():
    product = {}

    product["id"] = max([p["id"] for p in products], default=0) + 1
    product["title"] = input("Enter product title: ")
    product["price"] = float(input("Enter product price: "))
    product["description"] = input("Enter product description: ")

    while True:
        category = input("Enter category (summer/winter): ").lower()
        if category in ["summer", "winter"]:
            product["category"] = category
            break
        print("Invalid category!")

    while True:
        subcategory = input("Enter subcategory (men/women/kids): ").lower()
        if subcategory in ["men", "women", "kids"]:
            product["subcategory"] = subcategory
            break
        print("Invalid subcategory!")

    product["quantity"] = int(input("Enter quantity: "))

    products.append(product)
    save_products(products)
    print("Product added successfully!")

# ---------------- STOCK & PRICE ----------------

def adjust_price():
    pid = int(input("Enter Product ID => "))
    price = float(input("Enter new price => "))

    for item in products:
        if item["id"] == pid:
            item["price"] = price
            save_products(products)
            print("Price updated")
            return
    print("Product not found")

def increase_quantity():
    pid = int(input("Enter Product ID => "))
    qty = int(input("Enter quantity to add => "))

    for item in products:
        if item["id"] == pid:
            item["quantity"] += qty
            save_products(products)
            print("Quantity updated")
            return
    print("Product not found")

def decrease_quantity():
    pid = int(input("Enter Product ID => "))
    qty = int(input("Enter quantity to remove => "))

    for item in products:
        if item["id"] == pid:
            if item["quantity"] >= qty:
                item["quantity"] -= qty
                save_products(products)
                print("Quantity updated")
            else:
                print("Not enough stock")
            return
    print("Product not found")

def cart():
    pid = int(input("Enter Product ID to add => "))

    # Find the product
    for item in products:
        if item["id"] == pid:
            if item["quantity"] > 0:
                while True:
                    try:
                        qty = int(input(f"How many '{item['title']}' do you want to add? Available: {item['quantity']} => "))
                        if qty <= 0:
                            print("Quantity must be at least 1")
                        elif qty > item["quantity"]:
                            print(f"Only {item['quantity']} items are available. Please enter a valid quantity.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid number.")

                # Check if product already in cart
                for cart_item in shopping_cart:
                    if cart_item["id"] == pid:
                        cart_item["cart_quantity"] += qty
                        break
                else:
                    # Add new product to cart with cart_quantity
                    new_item = {
                        "id": item["id"],
                        "title": item["title"],
                        "price": item["price"],
                        "cart_quantity": qty
                    }
                    shopping_cart.append(new_item)

                # Update stock
                item["quantity"] -= qty
                save_products(products)
                print(f"Added {qty} x '{item['title']}' to cart")
            else:
                print("Out of stock")
            break
    else:
        print("Invalid Product ID")
        return

    # Checkout option
    while True:
        choice = input("Checkout? (Y/N) => ").upper()
        if choice == 'Y':
            generate_bill()
            return
        elif choice == 'N':
            show_products()
            return
        else:
            print("Invalid input")
# --------generate bill-----------
def generate_bill():
    total = 0
    print("\n--- CART ITEMS ---")
    
    for item in shopping_cart:
        # Use only price * cart_quantity
        line_total = item["price"] * item["cart_quantity"]
        print(f"{item['id']} | {item['title']} | Price: {item['price']} USD | Quantity: {item['cart_quantity']} | Sub Total: {round(line_total,2)} USD")
        total += line_total

    print(f"\nTotal Bill: {round(total, 2)} USD")
    print("Thank you for shopping!")


# ---------------- PRODUCT DISPLAY ----------------

def show_products():
    for i in products:
        print(f"{i['id']} | {i['title']} | {i['price']} USD")

    while True:
        choice = input("Add product to cart? (Y/N) => ").upper()
        if choice == 'Y':
            cart()
            return
        elif choice == 'N':
            print("Thank you for browsing!")
            return
        else:
            print("Invalid input")

# ---------------- START PROGRAM ----------------

login()
    