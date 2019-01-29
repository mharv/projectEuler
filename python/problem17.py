# project euler problem 17

# first a method of getting each word for corresponding number needs to exist

# create a dictionary

numberDict = {
	"0": "",
	"00": "",
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "nine",
	"10": "ten",
	"11": "eleven",
	"12": "twelve",
	"13": "thirteen",
	"14": "fourteen",
	"15": "fifteen",
	"16": "sixteen",
	"17": "seventeen",
	"18": "eighteen",
	"19": "nineteen",
	"20": "twenty",
	"30": "thirty",
	"40": "forty",
	"50": "fifty",
	"60": "sixty",
	"70": "seventy",
	"80": "eighty",
	"90": "ninety"
} 

def getCharacterCount(number):
	numberString = str(number)
	digitCount = len(numberString)
	word = []
	result = ""	
	count = 0
	
	if digitCount == 4:
		word.append(numberDict[numberString[0]])
		word.append("thousand")
	
	if digitCount == 3:
		word.append(numberDict[numberString[0]])
		word.append("hundred")
		if numberString[1:] != "00":
			word.append("and")
			if numberString[2] == "0" or numberString[1] == "1":
				word.append(numberDict[numberString[1:]])
			else:
				word.append(numberDict[numberString[1] + "0"])
				word.append(numberDict[numberString[2]])
	
	if digitCount == 2:
		if numberString[0] == "1" or numberString[1] == "0":
			word.append(numberDict[numberString])
		else:
			word.append(numberDict[numberString[0] + "0"])
			word.append(numberDict[numberString[1]])
	
	if digitCount == 1:
		word.append(numberDict[numberString])
		
	for i in word:
		result = result + i
	
	for char in result:
		count = count + 1	
	
	return count 

# get answer
answer = 0
for i in range(1, 1001):
	answer = answer + getCharacterCount(i)

print(answer)

