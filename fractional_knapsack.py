class Item:
    def __init__(self, weight, profit):
        self.weight = weight       # Store the weight of the item
        self.profit = profit       # Store the profit of the item
        self.ratio = profit / weight  # Calculate the profit-to-weight ratio

def fractional_knapsack(items, max_capacity):
    # Sort items based on the ratio in descending order
    items.sort(key=lambda item: item.ratio, reverse=True)
    total_value = 0
    current_weight = 0
    
    for item in items:
        if current_weight + item.weight <= max_capacity:
            # If the item can be added completely
            current_weight += item.weight
            total_value += item.profit
        else:
            # Take the fraction of the item that fits
            remaining_capacity = max_capacity - current_weight
            total_value += item.ratio * remaining_capacity
            break  # Exit loop after taking the fraction
    
    return total_value

# Example usage
items = [Item(10, 60), Item(20, 100), Item(30, 120)]
max_capacity = 50
max_value = fractional_knapsack(items, max_capacity)
print("Maximum value in the knapsack:", max_value)
