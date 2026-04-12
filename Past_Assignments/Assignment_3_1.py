#!/usr/bin/env python
# coding: utf-8

################################

# Student: Justin Hudson
# Instructor: Kaleab Gorfu
# CS 121: Python for DS and ML
# Date: 09/04/2026

#################################

# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import random 

# Constant variable to control number of rolls 
NUMBER_OF_ROLLS = 1000

# Role dice and calculate frequency
rolls = [random.randint(1,6) for i in range(NUMBER_OF_ROLLS)]
values = [1,2,3,4,5,6]
frequencies = [rolls.count(v) for v in values]

# Create bar graph with Seaborn
sns.set_style("darkgrid")
figure = plt.figure("Rolling a Six-Sided Die")
axes = sns.barplot(x=values, y=frequencies, hue=values, legend=False, palette="colorblind")

# Add title and label axes
axes.set_title(f"Rolling a Six-Sided Dice {len(rolls):,} Times")
axes.set(xlabel="Die Value", ylabel="Frequency")

# Set upper limit of y-axis
axes.set_ylim(top=max(frequencies) * 1.10)

# Add data labels for each bar
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f"{frequency:,}\n{frequency / len(rolls):.3%}"
    axes.text(text_x, text_y, text, fontsize=11, ha="center", va="bottom")

# Display bar graph
plt.show()

