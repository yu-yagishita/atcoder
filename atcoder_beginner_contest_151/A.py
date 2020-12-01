N = input()
a_to_z = [chr(i) for i in range(97, 97+26)]
for index, item in enumerate(a_to_z):
    if item == N:
        print(a_to_z[index+1])
