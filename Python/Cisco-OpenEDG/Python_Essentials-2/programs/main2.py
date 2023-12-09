from sys import path
path.append("..\\packages")
# when using a zipped file as a package
# path.append("..\\packages\\extrapack.zip")

import extra.iota
# using "import iota" will cause an error

import extra.good.alpha as alp
import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.iota.funI())
print(alp.funA())
print(extra.good.best.sigma.funS())
print(funT())
