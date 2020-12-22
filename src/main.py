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



# SECTION - Graph creation
# NOTE - For more information, visit https://pythonspot.com/matplotlib-pie-chart/
# TODO - Can this be more effecient? What if everything was stored as a dict, and then just passing
#    that dict on directly to the pie object?
labels = ['Attack', 'Defense', 'Strength', 'Hitpoints', 'Ranged', 'Prayer', 'Magic', 'Cooking',
          'Woodcutting', 'Fletching', 'Fishing', 'Firemaking', 'Crafting', 'Smithing', 'Mining',
          'Herblore', 'Agility', 'Thieving', 'Slayer', 'Farming', 'Runecraft', 'Hunter',
          'Construction']
sizes = [ls_atk.xp, ls_def.xp, ls_str.xp, ls_hit.xp, ls_ran.xp, ls_pry.xp, ls_mag.xp, ls_cok.xp,
         ls_wcg.xp, ls_fle.xp, ls_fsh.xp, ls_fmk.xp,
         ls_cra.xp, ls_smi.xp, ls_min.xp, ls_hrb.xp, ls_agl.xp, ls_thv.xp, ls_sly.xp, ls_far.xp,
         ls_rnc.xp, ls_hun.xp, ls_con.xp]
colors = ['#b50c00', '#65c7c5', '#387328', '#e2e6e1', '#868f47', '#f5f7e6', '#2759b0', '#701596',
          '#91712c', '#1d5454', '#adcdd9', '#fa9923', '#613418', '#706158', '#87827f', '#4e8042',
          '#031b40', '#4e2b5e', '#0d0d0d', '#0e7810', '#bdaf1a', '#5c5a54', '#b8a46a']

plt.figure(num="Graph my OSRS Stats - %s" % (sys.argv[2]))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
