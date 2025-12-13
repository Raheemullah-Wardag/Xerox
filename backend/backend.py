
shopping_cart = []

# PRODUCTS CATALOGUE
products = [
    {
        "id": 1,
        "title": "Men's Summer Cotton Shirt",
        "price": 22.99,
        "description": "Lightweight breathable cotton shirt ideal for hot summer days.",
        "category": "summer",
        "subcategory": "men",
        "quantity": 35
    },
    {
        "id": 2,
        "title": "Women's Floral Summer Dress",
        "price": 28.50,
        "description": "Soft flowy dress designed for comfort and summer outings.",
        "category": "summer",
        "subcategory": "women",
        "quantity": 18
    },
    {
        "id": 3,
        "title": "Kids Printed Summer T-Shirt",
        "price": 9.99,
        "description": "Comfortable cotton tee with cute summer-themed prints.",
        "category": "summer",
        "subcategory": "kids",
        "quantity": 42
    },
    {
        "id": 4,
        "title": "Men's Summer Shorts",
        "price": 17.00,
        "description": "Soft cotton shorts perfect for daily casual wear.",
        "category": "summer",
        "subcategory": "men",
        "quantity": 27
    },
    {
        "id": 5,
        "title": "Women's Sleeveless Tank Top",
        "price": 12.99,
        "description": "Lightweight sleeveless top ideal for hot weather.",
        "category": "summer",
        "subcategory": "women",
        "quantity": 50
    },
    {
        "id": 6,
        "title": "Kids Summer Shorts",
        "price": 11.50,
        "description": "Durable and comfortable shorts perfect for outdoor play.",
        "category": "summer",
        "subcategory": "kids",
        "quantity": 31
    },
    {
        "id": 7,
        "title": "Men's Winter Fleece Jacket",
        "price": 39.99,
        "description": "Warm fleece jacket offering comfort in cold weather.",
        "category": "winter",
        "subcategory": "men",
        "quantity": 14
    },
    {
        "id": 8,
        "title": "Women's Woolen Sweater",
        "price": 32.00,
        "description": "Soft knitted sweater for cozy winter evenings.",
        "category": "winter",
        "subcategory": "women",
        "quantity": 22
    },
    {
        "id": 9,
        "title": "Kids Hooded Winter Hoodie",
        "price": 19.99,
        "description": "Warm hoodie designed to keep kids comfortable in winter.",
        "category": "winter",
        "subcategory": "kids",
        "quantity": 19
    },
    {
        "id": 10,
        "title": "Men's Thermal Innerwear Set",
        "price": 25.99,
        "description": "Insulated thermal wear for layering in cold climates.",
        "category": "winter",
        "subcategory": "men",
        "quantity": 26
    },
    {
        "id": 11,
        "title": "Women's Winter Puffer Jacket",
        "price": 55.50,
        "description": "Thick puffer jacket providing extra warmth in harsh winters.",
        "category": "winter",
        "subcategory": "women",
        "quantity": 12
    },
    {
        "id": 12,
        "title": "Kids Winter Beanie Cap",
        "price": 8.50,
        "description": "Soft woolen beanie to keep children warm in winter.",
        "category": "winter",
        "subcategory": "kids",
        "quantity": 60
    },
    {
        "id": 13,
        "title": "Men's Lightweight Summer Polo",
        "price": 16.75,
        "description": "Breathable polo shirt ideal for warm summer days.",
        "category": "summer",
        "subcategory": "men",
        "quantity": 33
    },
    {
        "id": 14,
        "title": "Women's Winter Scarf",
        "price": 14.00,
        "description": "Soft wool scarf offering warmth and style.",
        "category": "winter",
        "subcategory": "women",
        "quantity": 45
    },
    {
        "id": 15,
        "title": "Kids Summer Sandals",
        "price": 13.99,
        "description": "Comfortable lightweight sandals perfect for summer.",
        "category": "summer",
        "subcategory": "kids",
        "quantity": 29
    }
]

# ADMIN LOGIN 
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

#  ADMIN PANEL 
def admin_panel():
    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. View Products")
        print("2. Increase Quantity")
        print("3. Decrease Quantity")
        print("4. Logout")

        choice = input("Choose => ")

        if choice == '1':
            admin_view_products()
        elif choice == '2':
            increase_quantity()
        elif choice == '3':
            decrease_quantity()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

def admin_view_products():
    for item in products:
        print(f"ID: {item['id']} | {item['title']} | Qty: {item['quantity']}")

def increase_quantity():
    pid = int(input("Enter Product ID => "))
    qty = int(input("Enter quantity to add => "))
    for item in products:
        if item["id"] == pid:
            item["quantity"] += qty
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
                print("Quantity updated")
            else:
                print("Not enough stock")
            return
    print("Product not found")

#  SHOPPING CART 
def cart():
    buy = int(input("Enter Product ID to add => "))

    for item in products:
        if item["id"] == buy:
            if item["quantity"] > 0:
                shopping_cart.append(item)
                item["quantity"] -= 1
                print("Added to cart")
            else:
                print("Out of stock")
            break
    else:
        print("Invalid Product ID")
        show_products()
        return

    
    while True:
        choice = input("Checkout? (Y/N) => ").upper()

        if choice == 'Y':
            generate_bill(shopping_cart)
            return
        elif choice == 'N':
            show_products()
            return
        else:
            print("Invalid input! Please enter Y or N.")


# BILLING 
def generate_bill(cart):

    while True:
        total = 0
        print("\n--- CART ITEMS ---")

        if not cart:
            print("Your cart is empty.")
            return

        for item in cart:
            print(f"{item['id']} | {item['title']} | {item['price']} USD")
            total += item["price"]

        print(f"Total Bill: {round(total,2)} USD")

        choice = input("\nDo you want to remove any item? (Y/N) => ").upper()

        if choice == 'Y':
            rid = int(input("Enter Product ID to remove => "))
            found = False

            for item in cart:
                if item["id"] == rid:
                    item["quantity"] += 1   # restore stock
                    cart.remove(item)
                    print("Item removed successfully.")
                    found = True
                    break

            if not found:
                print("Product not found in cart.")

        else:
            checkout = input("\nProceed to checkout? (Y/N) => ").upper()
            if checkout == 'Y':
                print("\nThank you for shopping with us!")
                return

#  PRODUCT DISPLAY
def show_products():
    for i in products:
        print(f"{i['id']} | {i['title']} | {i['price']} USD")

    # SAFE INPUT LOOP
    while True:
        choice = input("Add product to cart? (Y/N) => ").upper()

        if choice == 'Y':
            cart()
            return
        elif choice == 'N':
            print("Thank you for browsing!")
            return
        else:
            print("Invalid input! Please enter Y or N.")

#  START PROGRAM
login()
