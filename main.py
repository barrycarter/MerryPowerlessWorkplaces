# 16 unique cards numbered 1-16, 28 duplicate cards numbered 17-44 for a total of 72 cards (note python's range function requires one number higher)

from random import *

cards = list(range(1, 17))
cards.extend(list(range(17, 45)))
cards.extend(list(range(17, 45)))


def run_test():
  return (len(set(sample(cards, 10))) == 10)


nodupes = 0

for i in range(1000):
  if (run_test()):
    nodupes += 1
  print(nodupes, i + 1)

