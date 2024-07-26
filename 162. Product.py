#  167. Произведение
#  У Васи есть массив A длины N из неотрицательных целых чисел и число M.
#  Необходимо выбрать ровно K элементов массива A, 
#  чтобы их произведение было в точности равно M.

_, M, K = map(int, input().split())
original = list(map(int, input().split()))
N = len(original)
if M > 1:
    A = sorted(original)
    num_zeros = 0
    num_ones = 0
    idx = 0
    for i in range(len(A)):
        if A[i] == 0:
            num_zeros += 1
        elif A[i] == 1:
            num_ones += 1
        else:
            idx = i
            break
    current_result = 1
    ans = []
    i = idx
    ignored_indexes = []
    not_multiplier = set()
    while True:
        if i >= N:
            if len(ans) > 0:
                current_result //= ans[-1][0]
                i = ans[-1][1]
                ans.pop(-1)
                tmp = []
                for j in ignored_indexes:
                    if j < i:
                        tmp.append(j)
                ignored_indexes = tmp

                ignored_indexes.append(i)
            elif len(ans) == 0:
                current_result = 1
                i = idx-1
            
        elif (i not in ignored_indexes) and (i not in not_multiplier):
            if M % A[i] != 0:
                not_multiplier.add(i)
            else:
                if M % (A[i] * current_result) == 0 and len(ans) < K:
                    current_result *= A[i]
                    ans.append((A[i], i))
                    if len(ans) <= K and len(ans) + num_ones >= K and current_result == M:
                        break
                    
        #print()
        #print('i = ' + str(i))
        #print('current_result = ' + str(current_result))
        #print(ans)
        #print(ignored_indexes)
        #print()
        i += 1
    ones_count = K - len(ans)
    i = 0
    while ones_count > 0:
        if original[i] == 1:
            ones_count -= 1
            print(i+1, end=' ')
        i += 1
    ignored_numbers = set()
    for pair in ans:
        for i in range(N):
            if original[i] == pair[0] and i not in ignored_numbers:
                ignored_numbers.add(i)
                print(i+1, end=' ')
                break
elif M == 0:
    zero_idx = N
    for i in range(N):
        if original[i] == 0:
            zero_idx = i
            break
    ans = set()
    i = 0
    while len(ans) != K-1:
        ans.add(i)
        i += 1
    if zero_idx in ans:
        ans.add(i)
    else:
        ans.add(zero_idx)

    for num in ans:
        print(num + 1, end=' ')
elif M == 1:
    counter = 0
    for i in range(N):
        if original[i] == 1 and counter < K:
            print(i + 1, end=' ')
            counter += 1
            if counter == K:
                break