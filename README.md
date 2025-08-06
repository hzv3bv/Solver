# Random Number Sorter and Bar Chart Generator

This Python script generates 15 random numbers between 50 and 100, sorts them from lowest to highest, and creates a visual bar chart.

## Features

- Generates 15 random integers in the range 50-100 (inclusive)
- Sorts the numbers from lowest to highest
- Creates a professional bar chart with:
  - Value labels on each bar
  - Grid lines for better readability
  - Custom styling with colors and transparency
  - Proper axis labels and title
- Saves the chart as a high-quality PNG image
- Displays basic statistics (min, max, average)

## Requirements

- Python 3.6+
- matplotlib library

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Or install matplotlib directly:
```bash
pip install matplotlib
```

## Usage

Run the script directly:
```bash
python number_sorter.py
```

## Output

The script will:
1. Print the original randomly generated numbers
2. Print the sorted numbers (lowest to highest)
3. Create and save a bar chart as `random_numbers_chart.png`
4. Display basic statistics about the numbers

### Example Output
```
Original numbers: [66, 77, 52, 62, 55, 68, 92, 100, 90, 82, 63, 62, 81, 94, 98]
Sorted numbers (lowest to highest): [52, 55, 62, 62, 63, 66, 68, 77, 81, 82, 90, 92, 94, 98, 100]
Bar chart saved as 'random_numbers_chart.png'

Statistics:
Minimum value: 52
Maximum value: 100
Average value: 76.13
```

## Files

- `number_sorter.py` - Main Python script
- `requirements.txt` - Python dependencies
- `random_numbers_chart.png` - Generated bar chart (created after running the script)

## Customization

You can easily modify the script to:
- Change the number of random numbers generated (currently 15)
- Adjust the range of random numbers (currently 50-100)
- Modify the chart styling and colors
- Change the output image format or filename

Simply edit the relevant values in `number_sorter.py`.
