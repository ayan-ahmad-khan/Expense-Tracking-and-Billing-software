def add_product():
    print("\n--- Add New Product ---")
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))

    with open("products.txt", "a") as file:
        file.write(f"{product_name},{product_price},{product_quantity}\n")

    print(f"Product '{product_name}' added successfully!")