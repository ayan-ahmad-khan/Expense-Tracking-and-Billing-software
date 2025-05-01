def delete_product():
    print("\n--- Delete Product ---")
    product_name = input("Enter the name of the product to delete: ")

    try:
        with open("products.txt", "r") as file:
            products = file.readlines()

        updated_products = []
        product_found = False
        for product in products:
            name, price, quantity = product.strip().split(",")
            if name.lower() != product_name.lower():
                updated_products.append(product)
            else:
                product_found = True

        with open("products.txt", "w") as file:
            file.writelines(updated_products)

        if product_found:
            print(f"Product '{product_name}' deleted successfully!")
        else:
            print(f"Product '{product_name}' not found in the list.")

    except FileNotFoundError:
        print("Error: The product file does not exist. Please add products first.")