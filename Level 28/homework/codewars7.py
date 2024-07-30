def rental_car_cost(d):
    cost_per_day = 40
    total_cost = d * cost_per_day
    
    if d >= 7:
        total_cost -= 50
    elif d >= 3:
        total_cost -= 20
    
    return total_cost
