import re
import collections
from gtts import gTTS
import string

file = open('input.txt', 'rb')

output_folder = "output/"

pattern = re.compile("([\d]+[.])+")

bigger_temp = []

temp = []

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_')
    return filename

def is_number(input):
	return bool(pattern.match(input))

# count = 0
for line in file:
	if line.rstrip():
		item = line.rstrip()
		if is_number(item):
			bigger_temp.append(temp)
			temp = []
			# count += 1
			temp.append((int)(item.rstrip(".")))
		else:
			temp.append(item)
	# if count == 4:
	# 	break

del bigger_temp[0]

dict_ = {}


for item in bigger_temp:
	string_ = ""
	name = format_filename(item[1])
	item[1] += ",   ,"
	for i in item:
		if type(i) is not int:
			string_ += str(i)
	print string_
	tts = gTTS(text=string_, lang='en')
	tts.save(output_folder+name+".mp3")



# od = collections.OrderedDict(sorted(dict_.items()))

# print od
'''
Data quality tests


for item in bigger_temp:
	if len(item) == 0:
		print item

for item in bigger_temp:
	if len(item) == 1:
		print item

for item in bigger_temp:
	if len(item) > 3:
		print item



for item in bigger_temp:
	if len(item) > 3:
		count = 0
		for i in item:
			if type(i) is not int:
				if i.startswith("("):
					count += 1
		if count > 1:
			print item

'''