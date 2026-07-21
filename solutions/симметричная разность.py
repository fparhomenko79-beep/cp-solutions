n = int(input())
ctom = set(map(int, input().split()))
m = int(input())
strogo = set(map(int, input().split()))

a = ctom ^ strogo
print(len(a))
print(a if len(a) else "")