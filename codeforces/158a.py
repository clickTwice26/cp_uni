n, k = list(map(int, input().split(" ")))
scores = list(map(int, input().split(" ")))
ntest, ktest = n, k
scores_test = scores
# 5 5 -> Failed test cases
# 1 1 1 1 1
# k is the place what should be the benchmark result to qualify for the
#next round
# ntest, ktest = [4, 2]
# scores_test = [0, 0, 0, 0]
qualified = []
# print(f"K position: {scores_test[ktest-1]}")
for i in scores_test:
    if i >= scores_test[ktest-1] and i != 0:
        qualified.append(i)

print(len(qualified))

