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

#        Or I can probably make this a method somewhere, and then just iterate and call that 
#        method to do the parsing.

raw = data[1].split(',')
attack = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

# FIXME - Potentially defense is swapped with hitpoints.
raw = data[2].split(',')
defense = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[3].split(',')
strength = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

# FIXME - Potentially defense is swapped with hitpoints.
raw = data[4].split(',')
hitpoints = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

ranged = data[5].split(',')
defense = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[6].split(',')
prayer = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[7].split(',')
magic = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[8].split(',')
cooking = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[9].split(',')
woodcutting = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[10].split(',')
fletching = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[11].split(',')
fishing = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[12].split(',')
firemaking = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[13].split(',')
crafting = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[14].split(',')
smithing = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[15].split(',')
mining = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[16].split(',')
herblore = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[17].split(',')
agility= {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[18].split(',')
thieving = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[19].split(',')
slayer = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[20].split(',')
farming = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[21].split(',')
runecraft = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[22].split(',')
hunter = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

raw = data[23].split(',')
construction = {
    "rank": raw[0],
    "level": raw[1],
    "xp": raw[2]
}

# FIXME - Potentially defense is swapped with hitpoints.
# print(attack, defense, strength, hitpoints, ranged, prayer, magic, cooking, woodcutting, fletching, fishing, firemaking, crafting, smithing, mining, herblore, agility, thieving, slayer, farming, runecraft, hunter,construction)

# ---



# SECTION - Create graph

# Data to plot
labels = 'Attack', 'Defense', 'Strength', 'Hitpoints'
# 'Ranged', 'Prayer', 'Magic', 'Cooking', 'Woodcutting', 'Fletching', 'Fishing', 'Firemaking', 'Crafting', 'Smithing', 'Mining', 'Herblore', 'Agility', 'Thieving', 'Slayer', 'Farming', 'Runecraft', 'Hunter', 'Construction'
sizes = [215, 130, 245, 210]
colors = ['#333333', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
