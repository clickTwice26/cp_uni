word_count = int(input())
word_list = []
for i in range(word_count):
	word_list.append(input())
for i in word_list:
	if len(i) > 10:
		print(i[0]+str(len(i)-2)+i[len(i)-1])
	else:
		print(i)
		

