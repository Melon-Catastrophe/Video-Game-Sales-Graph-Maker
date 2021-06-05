import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable
import PySimpleGUI as sg

# These three lines enable some options for displaying pandas dataframes when printing to the console.
pd.set_option("display.precision", 3)   
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", None)

# This dictionary easily allows me to set what data types I want each column to be. 
dtypes = {
    "Name": "object",
    "Platform": "category",
    "Year_of_Release": "category",
    "Publisher": "category",
    "Global_Sales": "float64",
    "NA_Sales": "float64",
    "EU_Sales": "float64",
    "JP_Sales": "float64",
    "Critic_Score": "float64",
    "Developer": "category",
}

# Reading the data from a .csv file and making a new column "plat_num" containing number of games per platform.
vg = pd.read_csv("vg_sales.csv", dtype=dtypes, usecols=list(dtypes))
vg["plat_num"] = vg.groupby(["Platform"])["Name"].transform("count")


# A quick search function that allows one to return a key given a lookup in a dictionary.
def search(myDict, lookup):
    for key, value in myDict.items():
        if lookup in value:
            return key


# This class is what is able to make the graph. It gathers the data and plots it according to how the user desires.
class TopGameSalesByPlatform:
    def __init__(self):
        # List of regions the dataset supports with more readable names.
        self.country_full = {
            "Global": "Worldwide",
            "NA": "North America",
            "EU": "European Union",
            "JP": "Japan"
        }

        # List of platforms/consoles the dataset supports with more readable names.
        self.console = {
            "NES": "NES",
            "SNES": "Super NES",
            "N64": "Nintendo 64",
            "GC": "GameCube",
            "Wii": "Wii",
            "WiiU": "WiiU",

            "GB": "GameBoy",
            "GBA": "Game Boy Advanced",
            "DS": "DS",
            "3DS": "3DS",

            "XB": "Xbox",
            "X360": "Xbox 360",
            "XOne": "Xbox One",

            "PS": "PlayStation",
            "PS2": "PlayStation 2",
            "PS3": "PlayStation 3",
            "PS4": "PlayStation 4",
            "PSP": "PlayStation Portable",
            "PSV": "PlayStation Vita",

            "GEN": "Sega Genesis",
            "GG": "Game Gear",
            "SCD": "Sega CD",
            "SAT": "Sega Saturn",
            "DC": "Dreamcast",

            "3DO": "3DO Interactive Multiplayer",
            "2600": "Atari 2600",
            "NG": "Neo Geo",
            "TG16": "TurboGrafx-16",
            "WS": "WonderSwan",
            "PCFX": "PC-FX",
            "PC": "PC",
        }

    # get_region_names and get_console_names return the appropriate list of names for the GUI to display.
    def get_region_names(self):
        names = []
        i = 0
        for x in self.country_full.items():
            for y in x:
                i += 1
                if i % 2 == 0:
                    if y == "Worldwide":
                        names.append("Global")
                    else:
                        names.append(y)
        return names

    def get_console_names(self):
        names = []
        i = 0
        for x in self.console.items():
            for y in x:
                i += 1
                if i % 2 == 0:
                    names.append(y)
        return names


    def show_graph(self, country, platform, num_items):
        # This block below allows the program to accept either the key or item names for the self.console dictionary.
        console_key_used = True
        if search(self.console, platform) != None:
            console_key_used = False
            platform = search(self.console, platform)

        # Grabs the data needed from the dataset.
        vg_country = vg.sort_values("{}_Sales".format(country), ascending=False)
        platform_top_country = vg_country.groupby("Platform")[["Name", "{}_Sales".format(country)]]

        # Styles, makes, and shows the graph.
        plt.style.use('seaborn')
        graph = platform_top_country.get_group(platform).head(num_items).plot(kind="barh", x="Name", y="{}_Sales".format(country), figsize=(9, 6), legend=None)
        plt.autoscale(enable=True)
        divider = make_axes_locatable(graph)
        divider.add_auto_adjustable_area(use_axes=graph, pad=-0.7, adjust_dirs=["left"])
        plt.ylabel("Name of {} Game".format(self.console[platform]))
        plt.xlabel("Millions of Copies Sold")
        title1 = "Top {} {} Games Sold".format(num_items, self.console[platform] if console_key_used == True else self.console[platform])
        title2 = self.country_full[country] if country == "Global" else "in"
        title3 = self.country_full[country] if country != "Global" else ""
        title = title1 + " " + title2 + " " + title3
        plt.title(title)
        plt.show()


if __name__ == "__main__":
    game_top = TopGameSalesByPlatform()

    # The rest of the code is for the GUI. The layout dictionary controls the layout of the window.
    layout =    [[sg.Text("Pick a Console:")],
                 [sg.Combo(values = game_top.get_console_names(), size=(20,1), key="-CONSOLE-", enable_events=True)],
                 [sg.Text("Pick a Region:")],
                 [sg.Combo(values = game_top.get_region_names(), key='-REGION-')],
                 [sg.Text("Number of Items to Graph:")],
                 [sg.Input(key='-NUMBER-')],
                 [sg.Text("", key="-ERROR-", size=(41,1), text_color="red")],
                 [sg.Button("Submit"), sg.Button("Exit")] ]

    # Makes the window.
    window = sg.Window("Game Graph Maker", layout)

    # Keeps the window running until someone exits the window.
    # This loop reads events controls what happens when those events are read.
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == "Submit":
            window['-ERROR-'].update("")
            try:
                game_top.show_graph(search(game_top.country_full, values['-REGION-']) if values['-REGION-'] != "Global" else "Global", search(game_top.console, values['-CONSOLE-']), int(values['-NUMBER-']))
            except ValueError:
                window['-ERROR-'].update("ValueError: Please enter a whole number.")
            except KeyError:
                window['-ERROR-'].update("KeyError: Please select a Console and Region to graph.")


# TODO: I could also make a class for Top Game USER SCORE By Platform