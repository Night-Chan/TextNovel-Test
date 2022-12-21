import time

speeddial = 0.5
longdial = 3
temp = 69
dial = 69
relationshiptemp = 69
step = 0
tohru = 5
thorne = 5
datalen = 1
savedat = []


class data:
	def save():
		global savedat
		global checkpoint
		if datalen >= 1:
			savedat.append(checkpoint)
			if datalen >= 2:
				savedat.append(0)
				savedat.append(tohru)
			if datalen >= 3:
				savedat.append(thorne)
			if datalen >= 4:
				savedat.append(club)

		for i in savedat:
			print(i, end="")
		print("")


		savedat = []

class error:
	def inputerror():
		print("")
		print("Hey! Thats not a valid input! Try again.")
		print("")

class txtp:
	def lines(numone, numtwo):
		dial = text.readlines()[numone:numtwo]
		lengthdial = len(dial)
		step = 0
		for i in range(lengthdial):
			print(dial[step])
			step = step + 1
			time.sleep(speeddial)
		step = 0



	def question(optionval, question, ifValOneDial1, ifValOneDial2, ifValTwoDial1, ifValTwoDial2, ifValThreeDial1, ifValThreeDial2, partnerrelationshiptruefalseval1, partnerrelationshiptruefalseval2, partnerrelationshiptruefalseval3, partnerRelationshipplus, partnerRelationshipminus, isSavable):
		global relationshiptemp
		temp = 99
		if isSavable == 1:
			print("(This input is savable, type 'save' to get save value)")
		if optionval == 2:
			while temp != 1 and temp != 2:
				temp = input(question)
				print("")
				if temp == "1" or temp == "2":
					temp = int(temp)
				elif temp == "save" and isSavable == 1:
					data.save()
				else:
					error.inputerror()

		if optionval == 3:
			while temp != 1 and temp != 2 and temp != 3:
				temp = input(question)
				print("")
				if temp == "1" or temp == "2" or temp == "3":
					temp = int(temp)
				elif temp == "save" and isSavable == 1:
					data.save()
				else:
					error.inputerror()

		if temp == 1:
			dial = text.readlines()[ifValOneDial1:ifValOneDial2]
			lengthdial = len(dial)
			step = 0
			for i in range(lengthdial):
				print(dial[step])
				step = step + 1
				time.sleep(speeddial)
			step = 0
			if partnerrelationshiptruefalseval1 == 1:
				relationshiptemp = partnerRelationshipplus
			if partnerrelationshiptruefalseval1 == 2:
				relationshiptemp = partnerRelationshipminus

		if temp == 2:
			dial = text.readlines()[ifValTwoDial1:ifValTwoDial2]
			lengthdial = len(dial)
			step = 0
			for i in range(lengthdial):
				print(dial[step])
				step = step + 1
				time.sleep(speeddial)
			step = 0
			if partnerrelationshiptruefalseval2 == 1:
				relationshiptemp = partnerRelationshipplus
			if partnerrelationshiptruefalseval2 == 2:
				relationshiptemp = partnerRelationshipminus

		if temp == 3:
			dial = text.readlines()[ifValThreeDial1:ifValThreeDial2]
			lengthdial = len(dial)
			step = 0
			for i in range(lengthdial):
				print(dial[step])
				step = step + 1
				time.sleep(speeddial)
			step = 0
			if partnerrelationshiptruefalseval3 == 1:
				relationshiptemp = partnerRelationshipplus
			if partnerrelationshiptruefalseval3 == 2:
				relationshiptemp = partnerRelationshipminus

class relate:
	def tohruplus():
		global tohru
		tohru = tohru + relationshiptemp
	def tohruminus():
		global tohru
		tohru = tohru - relationshiptemp
	def thorneplus():
		global thorne
		thorne = thorne + relationshiptemp
	def thorneminus():
		global thorne
		thorne = thorne - relationshiptemp





print("Hey welcome! Enter a code for a checkpoint save, or type 0 to start a new game!")
print("-------------------------------------------------------------------------------")
checkpointinputted = int(input("--------------------------------CHECKPOINT CODE---------------------------------\n"))

#FIRST ONE - TWO DIGITS ARE STORY LOCATION, STORY DAY
#ZERO SPLITS DATA BETWEEN DAY AND RELATIONSHIP
#FIRST DIGIT AFTER ZERO IS RELATIONSHIP WITH TOHRU, SECOND IS THORNE

#ADD A CHECK TO COUNT DIGITS

print(len(str(checkpointinputted)))

if int(str(checkpointinputted)[0]) != 0:
	if len(str(checkpointinputted)) == 2:
		if int(str(checkpointinputted)[1]) == 0:
			checkpoint = int(str(checkpointinputted)[0])
		elif int(str(checkpointinputted)[1]) > 0:
			checkpoint = (int(str(checkpointinputted)[0]) * 10) + int(str(checkpointinputted)[1])
	if len(str(checkpointinputted)) == 1:
		checkpoint = checkpointinputted

	if len(str(checkpointinputted)) >= 4:
		if int(str(checkpointinputted)[3]) != 0:
			tohru = int(str(checkpointinputted)[3])
		elif int(str(checkpointinputted)[3]) == 0 and len(str(checkpointinputted)) > 5:
			tohru = int(str(checkpointinputted)[4])
	if len(str(checkpointinputted)) >= 5:
		if int(str(checkpointinputted)[3]) != 0:
			thorne = int(str(checkpointinputted)[4])
		elif int(str(checkpointinputted)[3]) == 0 and len(str(checkpointinputted)) > 6:
			thorne = int(str(checkpointinputted)[5])
	if len(str(checkpointinputted)) >= 7:
		if int(str(checkpointinputted)[3]) != 0:
			club = int(str(checkpointinputted)[6])
		elif int(str(checkpointinputted)[3]) == 0 and len(str(checkpointinputted)) > 8:
			club = int(str(checkpointinputted)[7])

else:
	checkpoint = 0


if checkpoint == 0:
	with open('starttext.txt') as text:
		txtp.lines(0,8)
		gender = 0
		while gender != 1 and gender != 2 and gender != 3:
			gender = input("1: Male / 2: Female / 3: Omen of Death\n")
			if gender == "1" or gender == "2" or gender == "3":
				gender = int(gender)
				checkpoint = 1
			else:
				error.inputerror()

if checkpoint == 1:
	with open('dayone.txt') as text:
		txtp.lines(0,6)
		temp = 69
		text.close()
	with open('dayone.txt') as text:
		txtp.question(2, "1: Turn around / 2: Keep walking\n", 7, 11, 13, 21, 0, 0, 0, 0, 0, 0, 0, 1)
		text.close()
	with open('dayone.txt') as text:
		txtp.question(2, "1: No, I've been here for a while / 2: Yeah, I just came here\n", 29, 35, 23, 27, 0, 0, 2, 0, 0, 0, 1, 0)
		if temp == 1:
			relate.tohruminus()
		text.close()
	datalen = 2
	checkpoint = 2
	time.sleep(longdial)

if checkpoint == 2:
	with open('dayone.txt') as text:
		txtp.lines(36,42)
		time.sleep(longdial)
		text.close()
	with open('dayone.txt') as text:
		txtp.lines(44, 49)
		text.close()
	with open('dayone.txt') as text:
		txtp.question(3, "1: Yo / 2: Hey / 3: (stay silent)\n", 52, 59, 52, 59, 61, 67, 0, 1, 2, 1, 3, 0)
		if temp == 3:
			relate.thorneminus()
		datalen = 3
		checkpoint = 3
		time.sleep(longdial)

if checkpoint == 3:
	with open('dayone.txt') as text:
		txtp.lines(68,78)
		text.close()
	if tohru == 5:
		with open('dayone.txt') as text:
			txtp.lines(80,83)
	if thorne == 5:
		with open('dayone.txt') as text:
			txtp.lines(85,88)
			text.close()
	with open('dayone.txt') as text:
			txtp.lines(89,91)
			text.close()
	with open('dayone.txt') as text:
		txtp.question(3, "1: Theatre Club / 2: Modern Arts Club / 3: No Club\n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
		if temp == 1:
			club = "theatre"
		if temp == 2:
			club = "arts"
		if temp == 3:
			club = 0
		text.close()
	if club == "theatre":
		if tohru == 5:
			with open('dayone.txt') as text:
				txtp.lines(95,98)
	if club == "arts":
		if thorne == 5:
			with open('dayone.txt') as text:
				txtp.lines(102,104)
	if club == 0 or tohru < 5 or thorne < 5:
		txtp.lines(107,109)
	text.close()

	datalen = 4
	checkpoint = 4
	time.sleep(longdial)

