import random

def makeTesterNum(num):
  if num[0] == '-':
    return num[1:]
  else:   
    return num

def makingLow():
  lowNum = input("Choose the lower bound: ")
  lowNumTester = makeTesterNum(lowNum)
  while lowNumTester.isdigit() == False:   
    print ("Error. Only integers are allowed")
    lowNum = input("Choose the lower bound: ")
    lowNumTester = makeTesterNum(lowNum)
    if lowNumTester.isdigit() == True:
      break

  lowNum = int(lowNum)
  return lowNum

def makingHigh():
  highNum = input("Choose the upper bound: ")
  highNumTester = makeTesterNum(highNum)
  while highNumTester.isdigit() == False:   
    print ("Error. Only integers are allowed")
    highNum = input("Choose the upper bound: ")
    highNumTester = makeTesterNum(highNum)
    if highNumTester.isdigit() == True:
      break

  highNum = int(highNum)
  return highNum
    
def makingGuess():
  userGuess = input("Now, make your guess: ")
  userGuessTester = makeTesterNum(userGuess)
  while userGuessTester.isdigit() == False:   
    print ("Error. Only integers are allowed")
    userGuess = input("Now, make your guess: ")
    userGuessTester = makeTesterNum(userGuess)
    if userGuessTester.isdigit() == True:
      break

  userGuess = int(userGuess)
  return userGuess

def checkingRange(lowNum, highNum):
  while lowNum >= highNum:
    print("Make sure your lower bound number is less than your upper bound number")
    lowNum = makingLow()
    highNum = makingHigh()
    if lowNum < highNum: 
      break
  return [lowNum,highNum]

def main():
  print("Welcome to Guess the Number!")
  print ("")
  print("In this game, you will (1) choose a range (2) guess a random number we generate within that range! Remember to only input integers.")
  print ("")
  print("CHOOSING THE RANGE:")

  lowNum = makingLow()
  highNum = makingHigh()

  createdRange = checkingRange(lowNum, highNum)

  lowNum = createdRange[0]
  highNum = createdRange[-1]
  
  print("Your range is", lowNum, "to", highNum)

  randNum = random.randint(lowNum, highNum)

  print("")
  print("GUESSING THE NUMBER:")
  userGuess = makingGuess()

  while userGuess != randNum:
    if userGuess < randNum:
      print("Incorrect. The number is higher")
      userGuess = makingGuess()
    elif userGuess > randNum:
      print("Incorrect. The number is lower")
      userGuess = makingGuess()
    else:
      break
  print("Congratulations! You guessed the number")
      
main()
