# Overview
I wrote this program to learn what games were popular in Japan versus North America, especially for Wii games. The data needed to be able to be displayed in graph form. So, I found a dataset and got to work!

The dataset used contains information on the sales and user/critic scores for video games that were sold before 2016. This information was obtained by scraping the website Metacritic.  

[Video Game Sales Dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings)  
[Software Demo Video](https://youtu.be/FjRroXOOmxo)

# Data Analysis Results
1. What are the differences between the Top 10 Wii games sold in Japan and those sold in North America?
    * The Top 10 Games sold in Japan vs. North America were pretty similar, surprisingly, so I decided to expand it to the Top 20 Games. In Japan, people seem to prefer games such as Rhythm Heaven, Monster Hunter: Tri, and Dragon Quest: X (which was never released in the US for the Wii). People in North America seem to prefer games in the Zelda and Just Dance Series. Graphs of these categories are available in the "Charts" folder.
2. What were the Top 3 Games sold for the Nintendo 64?
    * Super Mario 64, Mario Kart 64, and GoldenEye 007.

# Development Environment
I used VSCodium to write this program in Python. I used the following libraries:
* Pandas (to sort through the data)
* Matplotlib (to graph the data)
* PySimpleGUI (to provide the Graphical User Interface)

# Useful Websites
* [W3Schools - Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
* [Python Central Ternary Operator Tutorial](https://www.pythoncentral.io/one-line-if-statement-in-python-ternary-conditional-operator/)

# Future Work
* There are several bugs that need to be fixed.
* Make a class that will graph the top games based on user ratings.
* Allow the user to type 'N64' as well as 'Nintendo 64' into the GUI to display a Nintendo 64 graph. However, I would need to redesign a lot of my code to make this work.