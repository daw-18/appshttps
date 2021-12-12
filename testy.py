import main

main.dirapp()
print(main.path('test\\test.txt').decode('UTF-8')+": wirtual")
print(main.path('bbb.txt').decode('UTF-8')+": static")
print(main.path('plik1\\ooo.txt').decode('UTF-8')+": static folder")
print(main.path('kot.yu').decode('UTF-8')+": not folder")
print(main.path('.txt').decode('UTF-8')+": not name")
print(main.path('nii.').decode('UTF-8')+": not file extension")
print(main.path('').decode('UTF-8')+": index http")

#abgerit