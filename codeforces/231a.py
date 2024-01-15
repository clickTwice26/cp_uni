number_of_line = int(input())
lines = [input() for i in range(number_of_line)]
total_solved_problems = 0
for i in lines:
	sum = 0
	for z in i.split(' '):
		sum+= int(z)
	if sum >= 2:
		total_solved_problems+=1
print(total_solved_problems)


