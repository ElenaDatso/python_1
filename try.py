def some(arr):
  def another(i, j):
    arr[i], arr[j] = arr[j], arr[i]
  n = len(arr)
  done = True
  x= 1
  while done:
    done = False
    x = x +1
    for i in range(1, n-x):
      if arr[i - 1] > arr[i]:
        another(i-1, i)
        done = True
  return arr

print(some([1,4,2,6,3,58,34,23,9][0:0]))

