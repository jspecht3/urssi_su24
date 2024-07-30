import sys

n = len(sys.argv)
print("# arguments passed:", n)

print("\nname:", sys.argv[0])

print("\narguemnts passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
