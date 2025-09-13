def calculate_bill(item_cost, quantity, tax=0.05, discount=0.1):
    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount
    return total


if (__name__ == "__main__"):
    bill = calculate_bill(100, 2)
    print("Total bill amount : ", bill)

    bill_with_custom_tax = calculate_bill(100, 2, tax=0.08)
    print("Total bill amount with custom tax : ", bill_with_custom_tax)

    bill_with_custom_tax_and_discount = calculate_bill(100, 2, tax=0.08, discount=5)
    print("Total bill amount with custom tax and discount : ", bill_with_custom_tax_and_discount)