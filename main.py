# module name: main
import read
import purchase
import write
import add_product
import delete_product

again = "Y"
while again.upper() == "Y":
    print("\n--- Main Menu ---")
    print("1. Process a purchase")
    print("2. Add a new product")
    print("3. Delete a product")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        a = read.read_file()
        b = purchase.purchase(a)
        write.over_write(a, b)
    elif choice == "2":
        add_product.add_product()
    elif choice == "3":
        delete_product.delete_product()
    else:
        print("Invalid choice. Please try again.")

    again = input("\nDo you want to perform another operation? (Y/N): ")

print("\nThank you for shopping from our store!!")
print("Please check your invoice for your shopping details, \nWhich we have created in .txt file format.")
