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
    tnc = None
    mainstat = None

    def __init__(self, determination, crit, directhit, tnc, mainstat, weapondamage):
        self.mods = Level_Mods()

        self.mainstat = mainstat

        self.detmod = math.floor(((130 * (determination - self.mods.getMainMod(80))) / (self.mods.getDivMod(80))) + 1000)

        self.chr = math.floor((200 * (crit - self.mods.getMainMod(80))) / (self.mods.getDivMod(80) + 50)) / 10

        self.dhr = math.floor((550 * (directhit - self.mods.getMainMod(80))) / (self.mods.getDivMod(80))) / 10

        self.chd = math.floor(((200 * (crit - self.mods.getSubMod(80))) / (self.mods.getDivMod(80))) + 1400)

        self.wd = math.floor(((self.mods.getMainMod(80)*self.mods.getJobMainstatMod(80))/1000)+weapondamage)

        self.atk = math.floor((165*(mainstat-340))/340)+100

        self.tnc = math.floor(((100*(tnc-self.mods.getSubMod(80)))/(self.mods.getDivMod(80)))+1000)

        print(self.chr, self.chd, self.dhr,  self.detmod)

    def damage(self, potency):
        d1a = math.floor(potency*self.atk*self.detmod)
        d1b = math.floor(d1a/100)
        d1c = math.floor(d1b/1000)
        print(d1c)

        print("d2")
        d2a = math.floor(d1c*self.tnc)
        d2b = math.floor(d2a/1000)
        print(d2b)

        d2c = math.floor(d2b/self.wd)
        d2d = math.floor(d2c/100)
        print(d2d,self.wd,d2c)

        d2e = math.floor(d2d*self.mainstat)
        d2f = math.floor(d2e/100)
        print(d2f)

        d3a = math.floor(d2f*self.crit())
        d3b = math.floor(d3a/1000)
        d3c = math.floor(d3b*self.directhit())
        d3d = math.floor(d3c/100)
        print(d3d)

        da = math.floor(d3d*self.rand())
        db = math.floor(da/100)
        print(db)
        return db
        #todo buffs
        #dc = math.floor()

    #todo logic based
    def crit(self):
        return self.chd

    def directhit(self):
        return 125

    def rand(self):
        return 100