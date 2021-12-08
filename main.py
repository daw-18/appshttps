import os


fail_permissions={}
globpath={}
wglobpath={}
sqlglbpatch={}
ftpglobpatch={}
wirtual_path_name='wirtual.config'#deleit

#def pathsplit():
#def path_add_wirtual():

def writewpath(fails):
	if 'p' in fail_permissions[fails]:
		with open('wp\\'+fails,'r') as f:
			ret=f.read()
		return ret


def writepath(fails,data):
	if 'g' in fail_permissions[fails]:

		with open('ws\\'+data,'r') as f:
			ret=f.read()
		return ret

def dirapp_permissions(fail_permissions):#swap config fail
	for i in globpath:
		for z in globpath[i]:
			fail_permissions[z]='g'
	for i in wglobpath:
		for z in wglobpath[i]:
			fail_permissions[z]='p'

def dirapp_ospath(globpath):
	for dirapp in os.walk(os.getcwd()):
		l=len(os.getcwd())+1#+\
		globpath[dirapp[0][l:]]=dirapp[2] #patch=[fails]

def dirapp_wpath(wglobwpath):
	with open(wirtual_path_name,'r') as f: #error invalid file
		f=f.read()
		f=f.split('\t')
		for i in f:
			if(len(i)==0):continue
			i=i.split('\n')
			wglobpath[i[0]]=[fail for fail in i[2].split(',')]

def dirapp():
	global globpath
	global wglobpath
	global fail_permissions

	#arrays wirtaldate=[]

	os.chdir('ws')
	dirapp_ospath(globpath)

	os.chdir('..')
	dirapp_wpath(wglobpath)

	dirapp_permissions(fail_permissions)

def path(data):
	path,fails=os.path.split(data)#pathsplit(data)

	if (path in globpath ) and (fails in globpath[path]):
		return writepath(fails,data)
	elif (path in wglobpath) and (fails in wglobpath[path]):
		return writewpath(fails)
	else:return globpath
	



def main():

	#socet
	#funkcja
	dirapp()#os
	print(path('test\\test.txt'))

if __name__ == '__main__':
	main()
	#try erros,reset aplication endsocket