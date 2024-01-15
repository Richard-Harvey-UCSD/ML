import array as arr

array = [6, 4, 3, 2, 1, 7]
vals = arr.array('i', array)
print(vals.tolist())

vals.append(1)
print(vals.tolist())
vals.insert(1, 9)
print(vals.tolist())
vals.pop(2)
print(vals.tolist())
print(vals.index(7))

# brute force method
def has_pair_with_sum(arr, sum):
  len_arr = len(arr)
  for i in range(0, len_arr):
    for j in range(i + 1, len_arr):
      if arr[i] + arr[j] == sum:
        return True
  return False


# better solution
def has_pair_with_sum2(arr, sum):
  complement_set = set()
  len_arr = len(arr)
  for i in range(0, len_arr):
    if arr[i] in complement_set:
      return True
    complement_set.add(sum - arr[i])
  return False


print(has_pair_with_sum2(array, 12))
