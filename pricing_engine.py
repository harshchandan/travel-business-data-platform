def calculate_total_cost(hotel_cost, land_cost, markup_percentage):
    """
    Combine costs and apply markup.
    """
    total_cost = hotel_cost + land_cost
    final_price = total_cost * (1 + markup_percentage / 100)
    return total_cost, final_price