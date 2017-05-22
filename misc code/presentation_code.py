def make_sandwich(knife, bread, pb, j):
  slice1 = knife.spread(bread[0], pb)
  slice2 = knife.spread(bread[1], j)
  sandwich = [slice1, slice2]
  return sandwich