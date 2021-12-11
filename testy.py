import main

main.dirapp()
print(main.path('test\\test.txt')+": wirtual")
print(main.path('bbb.txt')+": static")
print(main.path('plik1\\ooo.txt')+": static folder")
print(main.path('kot.yu')+": not folder")
print(main.path('.txt')+": not name")
print(main.path('nii.')+": not file extension")
#abgerit