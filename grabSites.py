#!/usr/bin/python
import requests, sys
import time

def grab():
	print "Mister Spy Grabber"
	print "Sites Grabber From Ips"
	Files = open(sys.argv[1])
	for i in Files.readlines():
		site = i.strip()
		try:
			site = site.strip()
			ch = requests.get('http://api.hackertarget.com/reverseiplookup/?q='+site)
			if '.' in ch.content:
				print ch.content
				open('sites.txt', 'a').write(ch.content)
				time.sleep(5)
	
			else:
				print "[!] => "+site+'  Problem '
		except:
			pass		
grab()