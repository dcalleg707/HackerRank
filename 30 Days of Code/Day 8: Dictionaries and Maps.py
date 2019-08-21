n = int(input())
agenda = {}
for i in range(n):
    x = list(input().split(" "))
    agenda[x[0]]=x[1]
a = True
while a:
    try:
        nombre=input()
    except EOFError :
        break
    if nombre in agenda:
        print(nombre+"="+agenda[nombre])
    else:
        print("Not found")
