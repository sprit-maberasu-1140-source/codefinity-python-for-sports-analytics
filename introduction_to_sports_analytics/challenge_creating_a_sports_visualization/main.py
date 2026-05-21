import pandas as pd
import matplotlib.pyplot as plt

def plot_player_performance(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Game"], df["Points"], marker="o", label="Points")
    plt.plot(df["Game"], df["Assists"], marker="s", label="Assists")
    plt.plot(df["Game"], df["Rebounds"], marker="^", label="Rebounds")
    plt.title("Player Performance Over the Season")
    plt.xlabel("Game")
    plt.ylabel("Count")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Sample DataFrame for testing
data = {
    "Game": [1, 2, 3, 4, 5],
    "Points": [22, 18, 30, 25, 27],
    "Assists": [5, 7, 6, 8, 7],
    "Rebounds": [10, 9, 12, 11, 13]
}
df = pd.DataFrame(data)

plot_player_performance(df)
