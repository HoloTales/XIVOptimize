from StatHolder import StatMods
from MarketFetch import MarketFetch

stats = StatMods(1236, 3944, 2494, 380, 5605, 180)
print(stats.chd, stats.chr, stats.dhr, stats.detmod, stats.wd, stats.atk, stats.tnc)

print(stats.damage(400))

market = MarketFetch()