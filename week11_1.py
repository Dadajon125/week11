def sum_valid_prices(price_list):
    total = 0.0
    for price in price_list:    
        clean_price = price.strip()  
        if clean_price.lower() == "free":
            value = 0.0
        else:
            if "$" in clean_price:
                clean_price = clean_price.replace("$", "")
            try:
                value = float(clean_price)
            except:
                print(f"Skipping invalid price: {price}")
                continue
        total += value
    return total
raw_prices = ["$12.50", "Free", "error_404", "$5.00", "2.50", "N/A"]
total = sum_valid_prices(raw_prices)
print(f"Total: ${total}")   