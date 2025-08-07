import random
import matplotlib.pyplot as plt

def generate_and_sort_numbers():
    """
    Generate 15 random numbers from 50 to 100, sort them, and create a bar chart.
    """
    # Generate 15 random numbers between 50 and 100 (inclusive)
    numbers = [random.randint(50, 100) for _ in range(15)]
    
    print("Original numbers:", numbers)
    
    # Sort the numbers from lowest to highest
    sorted_numbers = sorted(numbers)
    
    print("Sorted numbers (lowest to highest):", sorted_numbers)
    
    # Create a bar chart
    plt.figure(figsize=(12, 6))
    x_positions = range(1, 16)  # Positions 1-15 for the bars
    
    # Create the bar chart
    bars = plt.bar(x_positions, sorted_numbers, color='skyblue', edgecolor='navy', alpha=0.7)
    
    # Customize the chart
    plt.title('15 Random Numbers (50-100) Sorted from Lowest to Highest', fontsize=14, fontweight='bold')
    plt.xlabel('Position', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels on top of each bar
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5, 
                f'{sorted_numbers[i]}', ha='center', va='bottom', fontsize=10)
    
    # Set y-axis range to show values clearly
    plt.ylim(45, 105)
    
    # Set x-axis ticks
    plt.xticks(x_positions)
    
    # Adjust layout and save/display
    plt.tight_layout()
    
    # Save the chart as an image file
    plt.savefig('random_numbers_chart.png', dpi=300, bbox_inches='tight')
    print("Bar chart saved as 'random_numbers_chart.png'")
    
    # Show the chart (if display is available)
    try:
        plt.show()
    except Exception as e:
        print(f"Display not available: {e}")
    
    return sorted_numbers

if __name__ == "__main__":
    # Run the function
    sorted_nums = generate_and_sort_numbers()
    
    # Print some statistics
    print(f"\nStatistics:")
    print(f"Minimum value: {min(sorted_nums)}")
    print(f"Maximum value: {max(sorted_nums)}")
    print(f"Average value: {sum(sorted_nums) / len(sorted_nums):.2f}")
