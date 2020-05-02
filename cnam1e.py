import sys
import dns
import dns.resolver
import colorama
import time
from colorama import Fore, Style
from requests.exceptions import ConnectionError


sublist=sys.argv[1]
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8']
subfile=open(sublist, 'r')
for sub in subfile:
	try:
		subd=sub.strip()		
		answer=my_resolver.query(sub.strip(), 'CNAME')
		for data in answer:
			print( Fore.WHITE  + "subdomain-> " + (subd))
			print( Fore.RED + str(data) +"\n")
	except :    
   		pass 
   		
subfile.close()

