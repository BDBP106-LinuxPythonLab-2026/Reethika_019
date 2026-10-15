"""10. Inventory and Billing System
Concepts: dictionary of tuples, nested data, while loop, if validation, string formatting
with ljust()/rjust()/f-strings
inventory = {
"pen": (10.0, 50), # (price, quantity in stock)
"notebook": (45.0, 20),
"eraser": (5.0, 100),

"marker": (30.0, 15),
}
Let the customer keep entering item quantity (for example pen 3) until they type done.
For each entry:
• reject unknown items and quantities that aren't valid numbers
• reject the order if there isn't enough stock
• otherwise, add it to a cart dictionary (merging repeated items) and reduce the
stock (tuples can't be changed, so replace the tuple)
At the end, print an aligned receipt with the item, quantity, unit price and line total.
Apply a 10% discount if the subtotal is over ₹500. Then print the updated inventory, and
mark items with fewer than 10 left as LOW STOCK."""
inventory = {
    "pen": (10.0, 50),        # (price, quantity in stock)
    "notebook": (45.0, 20),
    "eraser": (5.0, 100),
    "marker": (30.0, 15),
}

cart = {}
print("Enter orders like: pen 3   (type 'done' to finish)")

while True:
    entry = input("Order: ").strip().lower()

    if entry == "done":
        break

    parts = entry.split()
    if len(parts) != 2:
        print("Please enter in the format: item quantity")
        continue

    item, qty_text = parts

    # reject unknown items
    if item not in inventory:
        print(f"'{item}' is not available.")
        continue

    if not qty_text.isdigit() or int(qty_text) <= 0:
        print("Quantity must be a positive whole number.")
        continue
    qty = int(qty_text)

    price, stock = inventory[item]

    if qty > stock:
        print(f"Only {stock} {item}(s) in stock.")
        continue

    cart[item] = cart.get(item, 0) + qty

    inventory[item] = (price, stock - qty)
    print(f"Added {qty} {item}(s) to cart.")

print("\n" + "=" * 46)
print("RECEIPT".center(46))
print("=" * 46)
print("Item".ljust(12) + "Qty".rjust(6) + "Unit Price".rjust(14) + "Total".rjust(14))
print("-" * 46)

subtotal = 0
for item, qty in cart.items():
    price = inventory[item][0]
    line_total = price * qty
    subtotal += line_total
    print(f"{item.ljust(12)}{str(qty).rjust(6)}{('₹' + format(price, '.2f')).rjust(14)}{('₹' + format(line_total, '.2f')).rjust(14)}")

print("-" * 46)
print("Subtotal".ljust(32) + f"₹{subtotal:.2f}".rjust(14))

discount = 0
if subtotal > 500:
    discount = subtotal * 0.10
    print("Discount (10%)".ljust(32) + f"-₹{discount:.2f}".rjust(14))

print("Total to pay".ljust(32) + f"₹{subtotal - discount:.2f}".rjust(14))
print("=" * 46)

print("\nUpdated Inventory")
print("-" * 40)
for item, (price, stock) in inventory.items():
    status = "  LOW STOCK" if stock < 10 else ""
    print(f"{item.ljust(12)}{('₹' + format(price, '.2f')).rjust(10)}{str(stock).rjust(8)}{status}")