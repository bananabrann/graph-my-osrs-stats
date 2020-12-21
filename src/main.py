import sys
import matplotlib.pyplot as plt



# SECTION - Parse stats
data = sys.argv[1].split("\n")
rank = data[0].split(',')[0]            # TODO - Make this more effecient
total_lvl = data[0].split(',')[1]       # TODO - Make this more effecient
total_xp = data[0].split(',')[2]        # TODO - Make this more effecient

# TODO - This can be more effecient as well, most likely by creating and index array and then 
#        looping through the data and dynamically assigning the dicts. But for now, it will be
#        done like this becuase MVP.

raw = data[1].split(',')
attack = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[2].split(',')
defense = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

print(attack)
print(defense)

# ---



# SECTION - Create graph

# Data to plot
labels = 'Attack', 'Defense', 'Strength', 'Hitpoints'
# 'Ranged', 'Prayer', 'Magic', 'Cooking', 'Woodcutting', 'Fletching', 'Fishing', 'Firemaking', 'Crafting', 'Smithing', 'Mining', 'Herblore', 'Agility', 'Thieving', 'Slayer', 'Farming', 'Runecraft', 'Hunter', 'Construction'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
# plt.show()
