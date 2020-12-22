class LevelStat:
    def __init__(self, name, raw):
        # NOTE - raw data should be expected as...
        #        { rank, level, xp }
        
        self.name = name
        self.raw = raw

        data = raw.split(',')
        self.rank = data[0]
        self.level = data[1]
        self.xp = data[2]
