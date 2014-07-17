import urllib
import urllib2
import os
import re
import threading

username = raw_input("Username : ")

#Coded by B3mB4m
#b3mb4m@gmail.com

def pipl():

	url = "https://pipl.com/search/?q="
	uagent= {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)'}

	request = urllib2.Request(url+username, headers=uagent)
	send = urllib2.urlopen(request)
	data = send.read()
	comp = re.compile("&U=\S+&P=")
	baglantilar = comp.findall(data)

	empty = []

	for i in baglantilar:
		i = i.replace("&U=", "").replace("&P=", "")
		try:
			text = urllib.unquote(i.encode('ascii')).decode('utf-8')
			if username.lower() in text or username in text:
				empty.append(text)
				#print text
			else:
				pass
		except:
			pass	

	print "\nUser Profile Loading ..\n"
	for i in set(empty):
		print i

	print "\nUser Videos Loading ..\n"
	for i in set(empty2):
		print i	

pipl = threading.Thread(name='pipl', target=pipl)
pipl.run()

