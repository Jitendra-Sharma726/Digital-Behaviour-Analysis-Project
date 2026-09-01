import pandas as pd

import matplotlib
matplotlib.use("Agg") # Headless mode for saving files

import matplotlib.pyplot as plt

# Constants
FILE_NAME = "digital_behaviour.csv"
DAILY_LIMIT = 6.0


def load_data(filename):
    """
    Load data and convert Date column.
    """
    try:
        df = pd.read_csv(filename)
        df['Date'] = pd.to_datetime(df['Date'])

        # Sort the DataFrame by 'Date' and return the sorted DataFrame
        df = df.sort_values('Date')
        
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return pd.DataFrame()
    

def visualize_digital_behavior(df):
    """
    Create a side-by-side plot layout.
    """
    # 1. Setup Subplots (1 Row, 2 Columns)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

    # Assign axes to variables for easier use
    ax1 = axes[0]
    ax2 = axes[1]

    # Main Title
    fig.suptitle('Project 3: Digital Behaviour Analysis')

    # === PLOT 1: Daily Trends (Line Plot) ===
    # Plot two lines: ScreenTime and AppUsage
    ax1.plot(df['Date'], df['ScreenTime'], label='Screen Time')
    ax1.plot(df['Date'], df['AppUsage'], label='App Usage', linestyle='--')

    # Add a horizontal line for the limit (axhline)
    ax1.axhline(y=DAILY_LIMIT, color='red', linestyle='--', label='Daily Limit')

    # Labels
    ax1.set_title('Daily Usage Trends')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Hours')
    ax1.legend()
    
    # Rotate date labels
    ax1.tick_params(axis='x', rotation=45)

    # === PLOT 2: Correlations (Scatter with Color Map) ===
    # Scatter plot: x=Unlocks, y=ScreenTime, color=AppUsage
    scatter = ax2.scatter(
        df['Unlocks'], 
        df['ScreenTime'], 
        c=df['AppUsage'],   # Map color to AppUsage
        cmap='viridis',     # Choose a color theme
        alpha=0.7
    )

    # Labels
    ax2.set_title('Unlocks vs. Screen Time')
    ax2.set_xlabel('Unlocks')
    ax2.set_ylabel('Screen Time')

    # Add Colorbar
    plt.colorbar(scatter, ax=ax2, label='App Usage (Hours)')

    # Final Layout Adjustment & Save
    plt.tight_layout() 
    plt.savefig('digital_behaviour_analysis.png')
    print("Plot saved as 'digital_behaviour_analysis.png'")

if __name__ == "__main__":
    df = load_data(FILE_NAME)
    
    if not df.empty:
        visualize_digital_behavior(df)


