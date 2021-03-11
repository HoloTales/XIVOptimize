import math
from level import Level_Mods

class StatMods:
    # mainstats
    level = 80
    mods = None

    dhr = None
    chr = None
    chd = None
    detmod = None

    def __init__(self, det, chr, dhr):
        self.mods = Level_Mods()
        self.detmod = math.floor((130*(det-self.mods.getMainMod(80)))/(self.mods.getDivMod(80)+1000))
        self.chr = math.floor((200*(chr-self.mods.getMainMod(80)))/(self.mods.getDivMod(80)+50))/10
        self.dhr = math.floor((550*(dhr-self.mods.getMainMod(80)))/(self.mods.getDivMod(80)))/10
        self.chd = math.floor((200*(chr-self.mods.getSubMod(80)))/(self.mods.getDivMod(80)+1400))
        print(self.chr, self.chd, self.dhr,  self.detmod)


