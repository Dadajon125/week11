# Format: {StationID: {"price": float}}
stations = {
    "S_Fast": {"price": 0.50},
    "S_Slow": {"price": 0.20}
}

# Format: {DriverID: {"wallet": float, "plan": str}}
drivers = {
    "D1": {"wallet": 10.0, "plan": "Guest"},
    "D2": {"wallet": 10.0, "plan": "Subscriber"} # 25% off
}

requests = [
    ("D1", "S_Slow", 20),      # Valid. Cost: 4.0. Rem: 6.0.
    ("D2", "S_Fast", 20),      # Valid. Cost: (10.0 * 0.75) = 7.5. Rem: 2.5.
    ("D1", "S_Fast", 50),      # Error: Cost 25.0 > 6.0.
    ("D1", "S_Hyper", 10),     # Error: Station offline.
    ("D9", "S_Slow", 10),      # Error: Driver not found.
    ("D1", "S_Slow", -5)       # Error: Invalid kWh amount.
]

def start_charging(drivers_db, stations_db, driver_id, station_id, kwh_amount):
    if driver_id not in drivers_db:
        raise KeyError("Driver not found")
    if station_id not in stations_db:
        raise KeyError("Station offline")
    if type(kwh_amount) != (int or float) or kwh_amount <= 0:
        raise ValueError("Invalid kWh amount")
    driver = drivers_db[driver_id]
    station = stations_db[station_id]
    total_cost = kwh_amount * station["price"]
    if driver.get("plan") == "Subscriber":
        total_cost = total_cost * 0.75
    if driver.get("wallet", 0) < total_cost:
        raise ValueError("Insufficient funds")
    driver["wallet"] -= total_cost
    return float(total_cost)

def batch_charge_requests(drivers_db, stations_db, request_list):
    revenue = 0.0
    denied_sessions = 0
    for driver_id, station_id, kwh_amount in request_list:
        try:
            cost = start_charging(
            drivers_db,
            stations_db,
            driver_id,
            station_id,
            kwh_amount)
            revenue += cost
        except Exception as e:
            denied_sessions += 1
            print(f"Charge Error for {driver_id}: {e}")
    return {
        "revenue": float(revenue),
        "denied_sessions": denied_sessions
        }
result = batch_charge_requests(drivers, stations, requests)
print(result)
