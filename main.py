import os
import socket


fail_permissions={}
globpath={}
wglobpath={}
orginal_path=['F:\\py\\appshttps\\wp\\','F:\\py\\appshttps\\ws\\']
wirtual_path_name='F:\\py\\appshttps\\wirtual.config'#deleit
start_http='index.txt'
#def pathsplit():
#def path_add_wirtual():

def page_GET(conn,data):
	conn.sendall(b'HTTP/1.1 200 \r\n')
	conn.sendall(bytes("Content-Typle application/binary \r\n",'UTF-8'))#abgreit
	conn.sendall(bytes("Content-Length "+str(len(data))+" \r\n",'UTF-8'))
	conn.sendall(b'Server:apis \r\n')
	conn.sendall(b'\r\n')
	conn.sendall(data)

def recvuntil(sock,txt): #time
	d=b""
	i=0

	while i!=len(txt):
		dnow=sock.recv(1)
		if len(dnow)==0:break#try

		if dnow[0]==txt[i]:i=i+1
		else :i=0
		
		d+=dnow

	return d

def type_request(sock):
	d=recvuntil(sock,b'/')

	if d==b'GET /':
		return d+recvuntil(sock,b'\r\n\r\n')

	elif d==b'POST /' or d==b'PUT /':
		d=d+recvuntil(sock,b'Content-Length:')
		g=sock.recv(3)
		d=d+g
		g=int(g)
		d=d+recvuntil(sock,b'\r\n\r\n')
		d=d+sock.recv(g)
		return d

	else:return 0#try

def socket_konectiwe():#UBGREIT
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(('127.0.0.1',8080))
	s.listen(3)
	while True:
		try:
			conn,addr=s.accept()# data ip
			data=type_request(conn)

			if not data:break#time

			data=data.decode('UTF-8')
			data=data.split(' ')
			data=path(data[1][1:])#deleit /
			page_GET(conn,data)

		finally:
			conn.close()
	return 0

def writepath(fails,data,orgn):
	if 'g' in fail_permissions[fails]:

		with open(orginal_path[orgn]+data,'rb') as f:
			ret=f.read()
		return ret

def dirapp_permissions(fail_permissions):#swap config fail
	for i in globpath:
		for z in globpath[i]:
			fail_permissions[z]='g'
	for i in wglobpath:
		for z in wglobpath[i]:
			fail_permissions[z]='pg'

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

	os.chdir(orginal_path[1])
	dirapp_ospath(globpath)

	dirapp_wpath(wglobpath)

	dirapp_permissions(fail_permissions)

	os.chdir('..')#go to home

def path(data):
	path,fails=os.path.split(data)#pathsplit(data)

	if (len(path)==0) and (len(fails)==0) :
		return writepath(start_http,start_http,0)#???????
	elif (path in globpath ) and (fails in globpath[path]):
		return writepath(fails,data,1)
	elif (path in wglobpath) and (fails in wglobpath[path]):
		return writepath(fails,fails,0)
	else:return b"brak"
	

def main():

	#socet
	#funkcja
	dirapp()#os
	socket_konectiwe()
	#path('test\\test.txt')

if __name__ == '__main__':
	main()
	#try erros,reset aplication endsocket