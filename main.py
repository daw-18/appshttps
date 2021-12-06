import os

globpath={}
cwd=''
#def pathsplit():

def dirapp():
	global globpath
	global cwd

	os.chdir('ws')

	for dirapp in os.walk(os.getcwd()):
		globpath[dirapp[0]]=dirapp[2] #plik
	cwd=os.getcwd()
def path(data):
	path,filet=os.path.split(data)#pathsplit(data)
	
	if(path==''):path=cwd
	else:path=cwd+'\\'+path #~+cwd

	if (path in globpath ) and (filet in globpath[path]):return 0
	else:return path in globpath
	



def main():

	#socet
	#funkcja
	dirapp()#os
	print(path('bbb.txt'))

if __name__ == '__main__':
	main()