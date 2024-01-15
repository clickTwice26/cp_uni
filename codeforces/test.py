n,k = 5, 5
scores= [1, 1, 1, 1, 1]
print(scores)

qualified = []
for i in scores:
    if i > k:
        qualified.append(i)

print(qualified)
if len(qualified) < 1:
    print("All ares donkey")
    # max_numbers_in_the_scores = max(qualified)
    # print(list(map(str, scores)).sort())
    scores.sort()
    max_error_in_donkeys = scores[-1]
    scores.pop(len(scores)-1)
    print(f"MAX: {max_error_in_donkeys}")
    if max_error_in_donkeys != 0:
        qualified.append(max_error_in_donkeys)
    
    for i in scores:
        if i == max_error_in_donkeys:
            qualified.append(i)

print(len(qualified))
