import pandas

class Level_Mods:
    job_mods = None
    level_mods = None
    race_mods = None

    def __init__(self):
        job_mods = pandas.read_csv("./mods/jobmods.csv")
        level_mods = pandas.read_csv("./mods/levelmods.csv")
        race_mods = pandas.read_csv("./mods/racemods.csv")


    #todo alter per level (use pandas)
    def getMainMod(self, level):
        return 340

    def getDivMod(self, level):
        return 3300

    def getSubMod(self, level):
        return 380

    def getJobMainstatMod(self, param):
        return 100
