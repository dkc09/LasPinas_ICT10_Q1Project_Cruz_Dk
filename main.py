

from pyscript import display, document
from html import escape


def SKU_generator(e):
    document.getElementById("sku_output").innerHTML = ""

   
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value.strip()
    stock_qty = document.getElementById("quantity").value

    
    if not category or not product_name or not stock_qty:
        document.getElementById("sku_output").innerText = (
            "Please complete all fields."
        )
        return

    try:
        quantity = int(stock_qty)
        if quantity < 0:
            document.getElementById("sku_output").innerText = (
                "Quantity cannot be negative."
            )
            return
    except ValueError:
        document.getElementById("sku_output").innerText = (
            "Please enter a valid whole number."
        )
        return

  
    sku = (
        category[:3].upper()
        + "-"
        + product_name[:4].upper()
        + "-"
        + str(quantity)
    )

    
    display("SKU: ", sku, target="sku_output")


def create_order(e):
    
    customer = document.getElementById("customer").value.strip()

    if not customer:
        customer = "Guest"

    
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")

    
    subtotal = (
        float(prod1.value) * prod1.checked
        + float(prod2.value) * prod2.checked
        + float(prod3.value) * prod3.checked
        + float(prod4.value) * prod4.checked
        + float(prod5.value) * prod5.checked
    )


    tax_rate = 0.12
    tax = subtotal * tax_rate
    total = subtotal + tax

    
    menu_items = [
        ("Burger", prod1),
        ("Fries", prod2),
        ("Sandwich", prod3),
        ("Juice", prod4),
        ("Water", prod5)
    ]

    selected_items = ""

    for name, item in menu_items:
        if item.checked:
            price = float(item.value)
            selected_items += (
                f"<p>{escape(name)} - ₱{price:.2f}</p>"
            )

    
    receipt = f"""
    <h3>Receipt</h3>
    <p><strong>Customer:</strong> {escape(customer)}</p>
    <hr>
    <h4>Ordered Items</h4>
    {selected_items if selected_items else "<p>No items selected.</p>"}
    <hr>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>VAT (12%): ₱{tax:.2f}</p>
    <p><strong>Total: ₱{total:.2f}</strong></p>
    """


    document.getElementById("show").innerHTML = receipt