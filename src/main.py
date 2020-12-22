import sys
import matplotlib.pyplot as plt
from LevelStat import LevelStat



# SECTION - Parse stats
data = sys.argv[1].split("\n")
rank = data[0].split(',')[0]            # TODO - Make this more effecient
total_lvl = data[0].split(',')[1]       # TODO - Make this more effecient
total_xp = data[0].split(',')[2]        # TODO - Make this more effecient

ls_atk = LevelStat("attack", data[1])
ls_def = LevelStat("defense", data[2])
ls_str = LevelStat("strength", data[3])
ls_hit = LevelStat("hitpoints", data[4])
ls_ran = LevelStat("ranged", data[5])
ls_pry = LevelStat("prayer", data[6])
ls_mag = LevelStat("magic", data[7])
ls_cok = LevelStat("cooking", data[8])
ls_wcg = LevelStat("woodcutting", data[9])
ls_fle = LevelStat("fletching", data[10])
ls_fsh = LevelStat("fishing", data[11])
ls_fmk = LevelStat("firemaking", data[12])
ls_cra = LevelStat("crafting", data[13])
ls_smi = LevelStat("smithing", data[14])
ls_min = LevelStat("mining", data[15])
ls_hrb = LevelStat("herblore", data[16])
ls_agl = LevelStat("agility", data[17])
ls_thv = LevelStat("thieving", data[18])
ls_sly = LevelStat("slayer", data[19])
ls_far = LevelStat("farming", data[20])
ls_rnc = LevelStat("runecraft", data[21])
ls_hun = LevelStat("hunter", data[22])
ls_con = LevelStat("construction", data[23])



# SECTION - Create graph

# # Data to plot
# labels = 'Attack', 'Defense', 'Strength', 'Hitpoints', 'Ranged', 'Prayer', 'Magic', 'Cooking', 'Woodcutting', 'Fletching', 'Fishing', 'Firemaking', 'Crafting', 'Smithing', 'Mining', 'Herblore', 'Agility', 'Thieving', 'Slayer', 'Farming', 'Runecraft', 'Hunter', 'Construction'
# sizes = [215, 130, 245, 210]
# colors = ['#333333', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0)  # explode 1st slice

# # Plot
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)

# plt.axis('equal')
# plt.show()
