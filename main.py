def chop(target, integerArray):
  low = 0
  mid = int(len(integerArray) // 2)
  high = int(len(integerArray) - 1)
  indexOfNumber:int = 0
  searching = True

  while (searching):
    if(target == integerArray[low]):
      indexOfNumber = low
      searching = False
    elif(target == integerArray[high]):
      indexOfNumber = high
      searching = False
    elif(target == integerArray[mid]):
      indexOfNumber = mid
      searching = False
    else:
      if(target > integerArray[mid]):
        low = int(mid)
        mid = int((mid + high) // 2)
      elif(target < integerArray[mid]):
        high = int(mid)
        mid = int((mid + low) // 2)
      else:
        indexOfNumber = mid
        searching = False
  print("Index of number is: ", indexOfNumber)


numberArray01 = [1,3,5,7,9,11]
target01 = 5

numberArray02 = [2,4,6,8,10]
target02 = 2

numberArray03 = [2,4,6,8,10]
target03 = 10

numberArray04 = [2,4,6,8,10,12,14,16,18,20]
target04 = 12

numberArray05 = [2,4,6,8,10,11,12,13,14,15,16]
target05 = 8

chop(target01, numberArray01)
chop(target02, numberArray02)
chop(target03, numberArray03)
chop(target04, numberArray04)
chop(target05, numberArray05)

    