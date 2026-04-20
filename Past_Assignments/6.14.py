# 6.14

# Import necessary libraries
from matplotlib import animation
import matplotlib.pyplot as plt
import seaborn as sns
import random 
import sys

def positive_int(number_string):
    if number_string.isdecimal() and int(number_string) > 0:
        return True
    else:
        return False

def int_greater_than_one(number_string):
    if number_string.isdecimal() and int(number_string) > 1:
        return True
    else:
        return False

# Define function to be run for each frame of FuncAnimation
def update(frame_number, flips, sides, frequencies):
    for i in range(flips):
        frequencies[random.randint(1, 2) - 1] += 1 

    plt.cla()
    axes = sns.barplot(x=sides, y=frequencies, hue=sides, legend=False, palette="colorblind")  
    axes.set_title(f"Flipping a Coin {sum(frequencies):,} Times")
    axes.set(xlabel="Coin Value", ylabel="Frequency")  
    axes.set_ylim(top=max(frequencies) * 1.10)

    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0  
        text_y = bar.get_height() 
        text = f"{frequency:,}\n{frequency / sum(frequencies):.3%}"
        axes.text(text_x, text_y, text, ha="center", va="bottom")

# Add two command-line arguments for number of frames in FuncAnimation and number of rolls per frame
first_arg = sys.argv[1]
second_arg = sys.argv[2]

if int_greater_than_one(first_arg) and positive_int(second_arg):
    number_of_frames = int(first_arg) - 1
    flips_per_frame = int(second_arg)
else:
    while True:
        user_input = input("\nInvalid input. Please enter your arguments again: ").split()
        if int_greater_than_one(user_input[0]) and positive_int(user_input[1]):
            number_of_frames = int(user_input[0]) - 1
            flips_per_frame = int(user_input[1])
            break

# Create bar graph with Seaborn
sns.set_style("darkgrid")
figure = plt.figure("Flipping a Coin")
values = ["Heads","Tails"]
frequencies = [0,0]

# Start animation that calls update function for each frame
die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=33,
    fargs=(flips_per_frame, values, frequencies))

# Display bar graph
plt.show() 