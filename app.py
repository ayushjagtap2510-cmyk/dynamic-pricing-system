
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample product data
products = [
    {
        "id": 1,
        "name": "Laptop",
        "base_price": 50000,
        "demand": 10,
        "stock": 20
    },
    {
        "id": 2,
        "name": "Smartphone",
        "base_price": 25000,
        "demand": 15,
        "stock": 10
    },
    {
        "id": 3,
        "name": "Headphones",
        "base_price": 2000,
        "demand": 5,
        "stock": 30
    }
]

# Calculate dynamic price
def calculate_price(base_price, demand, stock):
    return max(0, base_price + (demand * 2) - stock)


@app.route("/")
def home():
    for product in products:
        product["dynamic_price"] = calculate_price(
            product["base_price"],
            product["demand"],
            product["stock"]
        )

    return render_template("index.html", products=products)


@app.route("/update", methods=["POST"])
def update():
    product_id = int(request.form["product_id"])
    demand = int(request.form["demand"])
    stock = int(request.form["stock"])

    for product in products:
        if product["id"] == product_id:
            product["demand"] = max(0, demand)
            product["stock"] = max(0, stock)
            break

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

