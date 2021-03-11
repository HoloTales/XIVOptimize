import math
from level import Level_Mods

class StatMods:
    # mainstats
    # See readme for location of info
    level = 80
    mods = None

    dhr = None
    chr = None
    chd = None
    detmod = None
    wd = None
    atk = None

    def __init__(self, determination, crit, directhit, weapondamage):
        self.mods = Level_Mods()

        self.detmod = math.floor((130 * (determination - self.mods.getMainMod(80))) / (self.mods.getDivMod(80) + 1000))

        self.chr = math.floor((200 * (crit - self.mods.getMainMod(80))) / (self.mods.getDivMod(80) + 50)) / 10

        self.dhr = math.floor((550 * (directhit - self.mods.getMainMod(80))) / (self.mods.getDivMod(80))) / 10

        self.chd = math.floor((200 * (crit - self.mods.getSubMod(80))) / (self.mods.getDivMod(80) + 1400))

        self.wd = math.floor(((self.mods.getMainMod(80)*self.mods.getJobMainstatMod(80))/1000)+weapondamage)

        self.atk = math.floor((165*(weapondamage-340))/340)+100


        print(self.chr, self.chd, self.dhr,  self.detmod)

