

# def fun(a,b):
#     res=a+b-2*(a&b)
#     return res
# def calculate_score(arr):
#     ans=0
#     n=len(arr)
#     for i in range(0,n-2):
#         for j in range(i+1,n-1):
#             for k in range(j+1,n):
#                 ans+=fun(arr[i],fun(arr[j],arr[k]))
#     return ans
# # Example array
# arr = [1, 2, 4]

# # Compute the score
# result = calculate_score(arr)
# print("Score:", result)
        

from collections import defaultdict

def fun(a, b):
    return a + b - 2 * (a & b)

def calculate_score(arr):
    N = len(arr)
    score = 0

    # Precompute fun(x, y) for all pairs (x, y) in arr
    precomputed = defaultdict(dict)
    for j in range(N):
        for k in range(j + 1, N):
            precomputed[j][k] = fun(arr[j], arr[k])
            print(precomputed)
    

    # Compute score using precomputed values
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                score += fun(arr[i], precomputed[j][k])
                print(score)

    return score

# Example usage
arr = [1, 1, 2, 3]
result = calculate_score(arr)
print("Optimized Score:", result)
