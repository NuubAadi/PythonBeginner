"""
Write the pseudocode to print the bill depending
upon the price and quantity of an item. Also print
Bill GST, which is the bill after adding 5% of tax in
the total bill.
"""
per_item_price = float(input("Per item price:"))
quantity = int(input("Quantity of item :"))
total_price = per_item_price*quantity
gst = total_price*0.05
total_bill = total_price+gst
print("\n----BILL----")
print(f"Total bill (without gst) {total_price}")
print(f"GST amout is :{gst}")
print(f"Total bill (with GST is) :{total_bill}")