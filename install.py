import os
def install():
	os.system("apt install dirb -y")
	os.system("apt install sslstrip -y")
	os.system("apt install bettercap -y")
	os.system("apt install sslscan -y")
	os.system("apt install crunch -y")
	os.system("apt install tcpdump -y")
	os.system("apt install macchanger -y")
	os.system("apt install wafw00f -y")
	os.system("apt install medusa -y")
	os.system("cd /root && git clone https://github.com/thelinuxchoice/shellphish")
	os.system("cd /root && git clone https://github.com/1N3/BruteX")
	os.system("cd /root/BruteX && ./install.sh")
	os.system("apt update")
	os.system("pip install mechanize json whois python-whois requests bs4 requests[socks] urlparse cookielib") 
	os.system("pip install scapy datetime argparse re threading urllib2 modules builtwith smtplib")
	os.system("pip install whois")
	os.system("pip install builtwith")
	os.system("pip install colorama")
	os.system("pip install dnspython")
	os.system("pip install shodan")
	os.system("apt install python-socks -y")
	os.system("apt install nmap -y")
	os.system("apt install php -y")
	os.system("apt install perl -y")
	os.system("apt install hashcat -y")
	os.system("apt install nc -y")
	os.system("apt install neofetch -y")
	os.system("apt install cupp -y")
	os.system("gem install lolcat")
	os.system("cd /root/ && git clone https://github.com/Und3rf10w/kali-anonsurf")
	os.system("cd /root/kali-anonsurf && ./installer.sh")
	print "\n"
	print """entering big download region prepare you anus
	if your not ready press ctrl C """
	i = raw_input("press ctrl c to stop hit enter to continue")
	os.system("apt install metasploit-framework -y")
	os.system("cd && git clone https://github.com/trustedsec/social-engineer-toolkit")
	os.system("apt install wifite -y")
	os.system("apt install reaver -y")
	os.system("apt install aircrack-ng -y")
	os.system("cd /root/social-engineer-toolkit && pip install -r requirements.txt")
	os.system("python /root/social-engineer-toolkit/setup.py install")
install()
