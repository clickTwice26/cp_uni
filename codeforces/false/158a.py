# Rejected this solution: I missed the question at the first
n, k = map(int, input().split(" "))
all_scores = list(map(int, input().split(" ")))
scores = all_scores

qualified = []
for i in scores:
    if i > k:
        qualified.append(i)

# print(qualified)
if len(qualified) < 1:
    # print("All ares donkey")
    # max_numbers_in_the_scores = max(qualified)
    # print(list(map(str, scores)).sort())
    scores.sort()
    max_error_in_donkeys = scores[-1]
    scores.pop(len(scores)-1)
    # print(f"MAX: {max_error_in_donkeys}")
    if max_error_in_donkeys != 0:
        qualified.append(max_error_in_donkeys)
    
        for i in scores:
            if i == max_error_in_donkeys:
                qualified.append(i)

print(len(qualified))

"""
# FAILED TEST CASE#6
# Input
    17 14
    16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
# Output
     2
# Answer
    14
# Checker Log
    wrong answer 1st numbers differ - expected: '14', found: '2'
"""
