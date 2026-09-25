# Inventory Management System

**High School Computing Science** · Python · Sep 2021 – Jan 2022

A console inventory and ordering system for a fictional online store, "Bamazon".

## How it works
1. **Supplying:** an employee logs in and enters the product list, which is saved to `products_base.txt`
2. **Stocking:** the employee enters a quantity for each product, which is saved to `products_stock.txt`
3. **Shopping:** customers place orders, and stock is updated after every purchase. Orders are saved to `purhcase_order.txt`

## Checks
- Rejects products that aren't carried
- Reports when a product is out of stock
- Caps an order at the available quantity when a customer asks for more than is in stock

## Run it
Requires Python 3 (standard library only).
```
python Inventory.py
```
The three `.txt` files are created in the folder you run it from.
