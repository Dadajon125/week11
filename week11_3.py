def checkout(inventory, cart):
    for item in cart:
        try:
            price = inventory[i]
            if price == None:
                raise TypeError("Price missing")
            if price < 0:
                raise ValueError("Invalid price")
            total_cost = price
        except KeyError:
            print(f"item not found: {i}") 
            failed_count += 1
        except (TypeError, ValueError) as error:
            print(f"Data error for {i}: {error}")
            failed_count +=1
        return total_cost, failed_count   
    
store_db = {
    "Apple": 0.50, 
    "Banana": 0.30, 
    "GhostItem": None,     # Corrupt data
    "GlitchItem": -5.00    # Corrupt data
}
my_cart = ["Apple", "Mango", "GhostItem", "Banana", "GlitchItem"]

cost, errors = checkout(store_db, my_cart)
print(f"Total: ${cost}, Errors: {errors}")
           
            
            