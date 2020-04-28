import random
def quickselect(l, k, time) :
  length = len(l)
  # Pick a random pivot element from the list, each
  # equally likely
  randIndex = random.randint(0,length-1)
  pivot = l[randIndex]
  l_small = []
  l_big = []

  # Put all elements smaller than pivot into l_small, and all
  # larger elements into l_big.
  for i in range(length):
    if l[i] > pivot:
      l_small.append(l[i])
    elif l[i] < pivot:
      l_big.append(l[i])
  # We assume all elements are distinct, so (besides the pivot) every element
  # should go into l_small or l_big
  assert(length == len(l_small) + len(l_big) + 1)
  
  if k <= len(l_small):
  # kth largest must be l_small
    time+=1
    res = quickselect(l_small, k, time)
    return res
  elif k > len(l_small) + 1:
  # kth largest must be in l_big
    k_updated = k - len(l_small) - 1
    time+=1
    res = quickselect(l_big, k_updated, time)
    return res
  else:
    return pivot, time

#Make your code return both the kth largest element and the number of calls to QUICK- SELECT (or its double-pivot variant) it took to find it.
calls = 0
for i in range(20000):
  a=[i for i in range(75)]
  tuble = quickselect(a, 30, 1)
  calls += tuble[1]
print("Average calls: ", calls/20000)