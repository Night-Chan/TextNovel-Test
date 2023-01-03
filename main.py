import time

speeddial = 0.5
longdial = 3
temp = 69
dial = 69
relationshiptemp = 69
step = 0
tohru = 5
thorne = 5
abby = 5
datalen = 1
far = 0
club = 0
savedat = []
checklist = [0]
event = 0
tohrudate = 0
thornedate = 0
abbydate = 0
tohrudead = 0
thornedead = 0
abbydead = 0
quickdial = 0



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



class recheck:
	def checkdate():
		global tohru
		global thorne
		global event
		global tohrudate
		global thornedate
		
		if tohru == 8 or tohru == 9:
			if event != 1 and tohrudate != 1:
				with open('characterevents/datetohru.txt') as text:
					txtp.lines(0,3)
					event = 1
					tohrudate = 1
		if thorne == 8 or thorne == 9:
			if event != 1 and thornedate != 1:
				with open('characterevents/datethorne.txt') as text:
					txtp.lines(0,3)
					event = 1
					thornedate = 1
	def checkkill():
		global tohru
		global thorne
		global event
		global tohrudead
		global thornedead
		if tohru == 0 or tohru == 1:
			if event != 1 and tohrudead != 1:
				with open('characterevents/xxtohru.txt') as text:
					txtp.lines(0,3)
					event = 1
					tohrudead = 1
		if thorne == 0 or thorne == 1:
			if event != 1 and thornedead != 1:
				with open('characterevents/xxthorne.txt') as text:
					txtp.lines(0,3)
					event = 1
					thornedead = 1


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
	def daytwolines(numone,numtwo):
		with open('daytwo.txt') as text:
			dial = text.readlines()[numone:numtwo]
			lengthdial = len(dial)
			step = 0
			for i in range(lengthdial):
				print(dial[step])
				step = step + 1
				time.sleep(speeddial)
			step = 0
			text.close()




	def question(optionval, question, ifValOneDial1, ifValOneDial2, ifValTwoDial1, ifValTwoDial2, ifValThreeDial1, ifValThreeDial2, partnerrelationshiptruefalseval1, partnerrelationshiptruefalseval2, partnerrelationshiptruefalseval3, partnerRelationshipplus, partnerRelationshipminus, isSavable):
		global relationshiptemp
		global temp
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

	def daytwoquestion(optionval, question, ifValOneDial1, ifValOneDial2, ifValTwoDial1, ifValTwoDial2, ifValThreeDial1, ifValThreeDial2, partnerrelationshiptruefalseval1, partnerrelationshiptruefalseval2, partnerrelationshiptruefalseval3, partnerRelationshipplus, partnerRelationshipminus, isSavable):
		global relationshiptemp
		global temp
		temp = 99
		with open('daytwo.txt') as text:
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
			text.close()

class relate:
	def tohruplus():
		global relationshiptemp
		global tohru
		global tohrudate
		if tohrudate == 0 and tohru != 9:
			tohru = tohru + relationshiptemp
		if tohru > 9:
			tohru = 9
	def tohruminus():
		global relationshiptemp
		global tohru
		global tohrudate
		if tohrudate == 0 and tohru != 0:
			tohru = tohru - relationshiptemp
		if tohru < 0:
			tohru = 0
	def thorneplus():
		global relationshiptemp
		global thorne
		global thornedate
		if thornedate == 0 and thorne != 9:
			thorne = thorne + relationshiptemp
		if thorne > 9:
			thorne = 9
	def thorneminus():
		global relationshiptemp
		global thorne
		global thornedate
		if thornedate == 0 and thorne != 0:
			thorne = thorne - relationshiptemp
		if thorne < 0:
			thorne = 0
	def abbyplus():
		global relationshiptemp
		global abby
		global abbydate
		if abbydate == 0 and abby!= 9:
			abby = abby + relationshiptemp
		if abby > 9:
			abby = 9
	def abbyminus():
		global relationshiptemp
		global abby
		global abbydate
		if abbydate == 0 and abby!= 0:
			abby = abby - relationshiptemp
		if abby < 0:
			abby = 0


	


class speak:
	def daytwo(lineone,linetwo):
		with open('daytwo.txt') as text:
			txtp.daytwolines(lineone,linetwo)
			text.close()
	def twoquestion(val,ask,d1,d2,d21,d22,d31,d32,yn1,yn2,yn3,pl,mn,dat):
		with open('daytwo.txt') as text:
			txtp.daytwoquestion(val,ask,d1,d2,d21,d22,d31,d32,yn1,yn2,yn3,pl,mn,dat)
			text.close()






print("Hey welcome! Enter a code for a checkpoint save, or type 0 to start a new game!")
print("-------------------------------------------------------------------------------")
checkpointinputted = int(input("--------------------------------CHECKPOINT CODE---------------------------------\n"))

#FIRST ONE - TWO DIGITS ARE STORY LOCATION, STORY DAY
#ZERO SPLITS DATA BETWEEN DAY AND RELATIONSHIP
#FIRST DIGIT AFTER ZERO IS RELATIONSHIP WITH TOHRU, SECOND IS THORNE

#ADD A CHECK TO COUNT DIGITS


fulllist = list(map(int, str(checkpointinputted)))


for i in range(0, len(fulllist)):
	if int(fulllist[i]) != 0 and far == 0:
		checklist.append(int(fulllist[i]))
		digits = i + 1
	if int(fulllist[i]) == 0 and len(fulllist) >= 2:
		far = 1
	if far == 1:
		tohru = int(fulllist[i])
		thorne = int(fulllist[(i+1)])
		club = int(fulllist[(i+2)])
		break

if len(checklist) == 1:
	checkpoint = int(checklist[0])
if len(checklist) == 2:
	checkpoint = (10*int(checklist[0]))+int(checklist[1])

print("")
print("")

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
		txtp.question(3, "1: Yo / 2: Hey / 3: (stay silent)\n", 52, 59, 52, 59, 61, 67, 0, 1, 2, 1, 2, 0)
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
			club = 1
		if temp == 2:
			club = 2
		if temp == 3:
			club = 0
		text.close()
	if club == 1:
		if tohru == 5:
			with open('dayone.txt') as text:
				txtp.lines(95,98)
	if club == 2:
		if thorne == 5:
			with open('dayone.txt') as text:
				txtp.lines(102,104)
	if club == 0 or tohru < 5 and thorne < 5:
		with open('dayone.txt') as text:
			txtp.lines(107,109)
	text.close()

	datalen = 4
	checkpoint = 4
	time.sleep(longdial)

if checkpoint == 4:
	with open('dayone.txt') as text:
		txtp.lines(113,119)
		text.close()
	with open('dayone.txt') as text:
		txtp.question(3,"1: Call Tohru / 2: Call Thorne / 3: Dont call anyone\n",125,128,174,176,214,216,1,1,0,1,0,0)
		called = temp
		text.close()
		
	if called == 1:
		relate.tohruplus()
		with open('dayone.txt') as text:
			txtp.lines(125,128)
			text.close()
		with open('dayone.txt') as text:
			txtp.question(2,"1: About the clubs... / 2: About today's lesson...\n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
			text.close()
		if temp == 1:
			if club == 1:
				with open('dayone.txt') as text:
					txtp.lines(131,1135)
					text.close()
					time.sleep(longdial)
			if club == 2:
				with open('dayone.txt') as text:
					txtp.lines(138,140)
					text.close()
					time.sleep(longdial)
			if club == 0:
				with open('dayone.txt') as text:
					txtp.lines(143,150)
					text.close()
					time.sleep(longdial)
		if temp == 2:
			with open('dayone.txt') as text:
				txtp.lines(153,157)
				text.close()
				time.sleep(longdial)
			with open('dayone.txt') as text:
				txtp.lines(160,163)
				text.close()
		time.sleep(longdial)
		with open('dayone.txt') as text:
			txtp.lines(166,169)
			text.close()
			time.sleep(longdial)
		
	if called == 2:
		relate.thorneplus()
		with open('dayone.txt') as text:
			txtp.lines(174,176)
			text.close()
		with open('dayone.txt') as text:
			txtp.question(2,"1: About the clubs... / 2: About today's lesson...\n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
			text.close()
		if temp == 1:
			if club == 1:
				with open('dayone.txt') as text:
					txtp.lines(184,186)
					text.close()
					time.sleep(longdial)
			if club == 2:
				with open('dayone.txt') as text:
					txtp.lines(179,181)
					text.close()
					time.sleep(longdial)
			if club == 0:
				with open('dayone.txt') as text:
					txtp.lines(189,193)
					text.close()
					time.sleep(longdial)
		if temp == 2:
			with open('dayone.txt') as text:
				txtp.lines(196,199)

		time.sleep(longdial)
		if thorne >= 6:
			with open('dayone.txt') as text:
				txtp.lines(204,206)
				text.close()
		else:
			with open('dayone.txt') as text:
				txtp.lines(209,211)
				text.close

	if called == 3:
		with open('dayone.txt') as text:
			txtp.lines(214,216)
		
	with open('dayone.txt') as text:
		txtp.lines(219,221)
		text.close()
	
	time.sleep(longdial)
	checkpoint = 5
	savenow = 1
	while savenow != "done":
		savenow = input("Do you want to save? (y/n)\n")
		if savenow == "y" or savenow == "Y":
			data.save()
			savenow == "done"
			break
		elif savenow == "n" or savenow == "N":
			savenow == "done"
			break
		elif savenow != "n" and savenow != "N" and savenow != "y" and savenow != "Y" and savenow != "done":
			print("Hey! That's an invalid input!")
			print("")

#DAY TWO STARTS HERE
datalen = 5

if checkpoint == 5:	
	checkpoint = 11

if checkpoint == 11:
	speak.daytwo(2,6)
	speak.twoquestion(2,"1: Run up to her / 2: Keep walking\n",9,13,18,20,0,0,1,0,0,1,0,0)
	if temp == 1:
		relate.tohruplus()

	time.sleep(longdial)
	checkpoint = 12

if checkpoint == 12:
	speak.daytwo(22,31)
	speak.twoquestion(2,"1: Yes, I do / 2: No, I dont\n",34,39,42,46,0,0,1,2,0,2,2,1)
	if temp == 1:
		relate.abbyplus()
	if temp == 2:
		relate.abbyminus()
		quickdial = 2

if quickdial == 2:
	quickdial = 0
	speak.twoquestion(2,"1: Yes, I do / 2: No, I dont\n",58,60,49,51,0,0,0,0,0,0,0,0)
	if temp == 2:
		Abby = 2

time.sleep(longdial)






	

	
			