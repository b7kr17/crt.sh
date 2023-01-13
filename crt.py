import requests
import re
import time

def bunner():
	print("""
	            _         _     
	   ___ _ __| |_   ___| |__  
	  / __| '__| __| / __| '_ \ 
	 | (__| |  | |_ _\__ \ | | |
	  \___|_|   \__(_)___/_| |_|
  	
	 [+] by AbuBaker Al Nour - twitter : @b7kr17
	""")
def request(org):
	url = "https://crt.sh/?"
	params = {"q":f"{org}"}
	response = requests.get(url,params=params)
	if response.status_code == 200:
		response = response.text
		domains = re.findall(r"<TD>[a-zA-Z0-9_\.\*-]+<\/TD>",response)
		if re.match(r"(\w+)\.(\w+)",org) is not None:
			for item in domains:
				domain = item.replace("<TD>"," ").replace("</TD>"," ").replace("*."," ").strip()
				print(domain)
		elif re.match(r"[a-zA-Z\.\+]+",org) is not None :
			for item in domains:
				domain = item.replace("<TD>"," ").replace("</TD>"," ").replace("*."," ").strip()
				if re.match(r"((^(\w+)\.(\w{2,3})\.(\w{2})$)|(^(\w+)\.(\w+)$))",domain) is not None:
					print(domain)
				else:
					pass
				cc = re.search(r"((\b\.(\w+)\.(\w{2,3})\.(\w{2})$)|(\b\.(\w{5,})\.(\w+)$))",domain)
				if cc is not None:
					print(cc.group(0).replace(".","",1))
				else:
					continue
		else:
			pass
	else:
		print("time out")
bunner()
 

x = input("Enter domain :")
request(x)


