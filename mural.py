#!/usr/bin/python3

test_cases = int(input())

for case in range(1, test_cases + 1):
    mural_size = int(input())
    initial_state = [int(v) for v in input()]
    score = 0
    # compute # of sections we can paint
    span = (mural_size + 1) // 2
    # find adjacent wall sections with span length with max intial beauty.
    for i in range(0, mural_size - span):
        now = sum(initial_state[i:i + span])
        score = max(now, score)
    print(f'Case #{case}: {score}')


# for case in range(1, test_cases + 1):
#     mural_size = int(input())
#     initial_state = [int(v) for v in input()]
#     score = 0
#     # compute # of sections we can paint
#     span = (mural_size + 1) // 2
#     # find adjacent wall sections with span length with max intial beauty.
#     for i in range(0, 1 + (mural_size - span + 1) // 2):
#         left = sum(initial_state[i:i + span])
#         right = sum(initial_state[mural_size - i - span:mural_size - i])
#         # print(i, ': ', left, right, score)
#         score = max((score, left, right))
#     print(f'Case #{case}: {score}')