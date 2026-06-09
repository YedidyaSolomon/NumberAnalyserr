number = int(input("Enter a positive integer: "))

lastDigit=0
##sum of the digits
def sumofDigits(number):
	temp=number
	sum=0
	while temp>0:
		lastDigit=temp%10
		sum+=lastDigit
		temp//=10
	print("Sum of digits: ", sum)

def productOfDigits(number):
	temp = number
	product=1
	while(temp>0):
		lastDigit=temp%10
		product*=lastDigit
		temp//=10
	print("Product of digits: ", product)


def reverseNumber(number):
	reverseDigit = 0
	temp = number
	while temp>0:
		lastDigit = temp%10
		reverseDigit = reverseDigit * 10 + lastDigit
		temp//=10
	
	print("Reverse: ", reverseDigit)
	return reverseDigit

def checkPalindrom(number):
	
	if reverseNumber(number) == number:
		print("Palindrome: True")

	else:
		print("Palindrome: false")

def findLargestDigit(number):
	temp = number
	lastDigit = 0
	largest = 0
	while temp>0:
		lastDigit = temp%10
		if lastDigit >= largest:
			largest = lastDigit
			temp//=10
	print("Largest digit: ", largest)

def findSmallestDigit(number):
	lastDigit = 0
	temp = number
	smallestDigit = 9
	while temp>0:
		lastDigit = temp%10
		if lastDigit <= smallestDigit:
			smallestDigit = lastDigit
		temp//=10
	print("smallest digit: ", smallestDigit)

def factorial(number):
	if number == 0:
		return 1
	else:
		return number * factorial(number - 1)
#print("factorial: ", factorial(number))


def countEvenOddDigits(number):
	temp = number
	evencount = 0
	oddcount = 0
	while temp>0:
		lastDigit = temp%10
		if lastDigit==0:
			temp//=10 
		elif lastDigit%2==0:
			evencount+=1
			temp//=10
			continue
		elif lastDigit%2!=0:
			oddcount+=1
			temp//=10
			continue
	print("Even digits: ", evencount)
	print("Odd digits: ", oddcount)

sumofDigits(number)
productOfDigits(number)
reverseNumber(number)
checkPalindrom(number)
findLargestDigit(number)
findSmallestDigit(number)
countEvenOddDigits(number)