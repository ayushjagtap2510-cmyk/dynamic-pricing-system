# Dynamic Demand-Based Pricing System

## Overview
The Dynamic Demand-Based Pricing System is a Python-based web application developed using Flask. It calculates product prices dynamically based on customer demand and available stock.

The system helps demonstrate how product prices can be adjusted according to changing market conditions.

## Features
- Displays multiple products with their base prices.
- Calculates dynamic prices using demand and stock levels.
- Allows users to update product demand.
- Allows users to update available stock.
- Automatically recalculates prices after updates.
- Provides a simple and user-friendly web interface.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- Jinja2

## Pricing Formula

Dynamic Price = Base Price + (Demand × 2) − Stock

The calculated price is restricted to a minimum of zero.

## Project Structure

```text
dynamic_pricing/
│
├── app.py
├── requirements.txt
├── .gitignore
│
└── templates/
    └── index.html
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ayushjagtap2510-cmyk/dynamic-pricing-system.git
```

### 2. Navigate to the project folder

```bash
cd dynamic-pricing-system
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

Visit:

```text
http://127.0.0.1:5000
```

## How It Works

1. The application displays available products.
2. Each product has a base price, demand and stock value.
3. The pricing formula calculates the dynamic price.
4. Users can modify demand and stock values.
5. The application recalculates and displays the updated price.

## Learning Outcomes
- Understanding Flask web application development.
- Implementing dynamic pricing logic using Python.
- Understanding the relationship between demand and supply.
- Handling HTML forms using Flask.
- Displaying dynamic data using Jinja2 templates.

## Future Improvements
- Integrate MySQL database connectivity.
- Store product and pricing information permanently.
- Add customer purchase history.
- Implement graphical price analysis.
- Introduce advanced demand forecasting techniques.

## Author
Ayush Jagtap

## Disclaimer
This project is an educational prototype using sample in-memory product data. It does not currently implement a production pricing engine or persistent database storage.
