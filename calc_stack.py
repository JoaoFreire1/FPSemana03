from collections import deque

dados = input()
splitdados = dados.split()
intstack = [int(i) for i in splitdados]
stack = deque(intstack)
print(stack)

for i in range(len(stack)):
    result = stack.pop() * 2
    print(result)