ROUTE_PRICES = {
    "Station A - Station B": 50,
    "Station A - Station C": 80,
    "Station B - Station C": 40
}

def calculate_price(route):
    if route not in ROUTE_PRICES:
        raise ValueError("Invalid route selected")
    return ROUTE_PRICES[route]
