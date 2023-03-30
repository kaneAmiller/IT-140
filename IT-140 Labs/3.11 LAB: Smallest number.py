num_a = int(input())
num_b = int(input())
num_c = int(input())

if num_a < num_b and num_a < num_c:
    print(num_a)
elif num_b < num_a and num_b < num_c:
    print(num_b)
elif num_a == num_b == num_c:
    print(num_a)
elif num_a == num_b or num_a == num_c or num_b == num_c:
    print(min(num_a, num_b, num_c))
else:
    print(num_c)
