from collections import deque

dados = input()
splitdados = dados.split()
stack = deque(splitdados)
print(stack)


for palavra in range(len(stack)):
    for letra in stack[palavra]:
        if letra == "a":
            print(stack[palavra])
            break
        else:
            pass