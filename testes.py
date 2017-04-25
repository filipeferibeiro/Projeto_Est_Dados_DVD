file = open('teste.txt', 'w')
file.write('hahaha\n')
file.write('hehehe\n')
file.write('hihihi')
file.close()

file = open('teste.txt', 'r')
for i in file:
    print(i)
file2 = open('chachacha.txt', 'a')
file2.write('bummmm')
file2.close()
