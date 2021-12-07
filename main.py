import os

globpath={}
cwd=''
wglobpath={}

#def pathsplit():
#def path add wirtual.config (sentence cannot contain \t \n , )

def dirapp_ospath(globpath):
	for dirapp in os.walk(os.getcwd()):
		globpath[dirapp[0]]=dirapp[2] #fail

def dirapp_wpath(wglobwpath):
	with open('wirtual.config','r') as f: #error invalid file
		f=f.read()
		f=f.split('\t')
		for i in f:
			if(len(i)==0):continue
			i=i.split('\n')
			wglobpath[i[0]]=[fail for fail in i[2].split(',')]

def dirapp():
	global globpath
	global cwd
	global wglobpath

	#go to cook
	#arrays os.path=[]
	#arrays wirtaldate=[]

	os.chdir('ws')
	dirapp_ospath(globpath)
	cwd=os.getcwd()#deleit

	os.chdir('..')
	dirapp_wpath(wglobpath)


def path(data):
	path,filet=os.path.split(data)#pathsplit(data)
	
	if(path==''):path=cwd		  #} deleit
	else:path=cwd+'\\'+path #~+cwd }

	if (path in globpath ) and (filet in globpath[path]):return globpath
	else:return path in globpath
	



def main():

	#socet
	#funkcja
	dirapp()#os
	print(path('bbb.txt'))

if __name__ == '__main__':
	main()
	#try erros,reset aplication endsocket