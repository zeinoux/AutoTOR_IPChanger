# Auto TOR IPChanger

Change your IP Addresses automatically with tor based project and greatfull interactive CLI interface with Python3. This repo is adopted from [https://github.com/FDX100/Auto_Tor_IP_changer](https://github.com/FDX100/Auto_Tor_IP_changer)


# Installation

 1. Setup TOR in your environment [https://www.torproject.org/docs/tor-doc-unix.html.en](https://www.torproject.org/docs/tor-doc-unix.html.en)
 2. Setup 3rd party Proxy chainer ex: proxychains, pivoxy, etc.
 >- Debian : ***sudo apt-get install proxychains***
 >- CentOS : ***wget -O- https://gist.githubusercontent.com/ifduyue/dea03b4e139c5758ca114770027cf65c/raw/install-_proxychains_-ng.sh | sudo bash -s. set -eu. version=4.14***
 >- ArchLinux : ***sudo pacman -S _proxychains_-ng***
 3. Python3 requests socks module : ***pip3 install requests[socks]***
 

## Using
 - cd AutoTOR_IPChanger/
 - sudo python3 TORChanger.py -h (must root)
 
> 'help' or '--help' returns this help  
'-t' time to change Ip in Sec [type=60]  
'-c' how many time do you want to change your ip [type=1000]  
for infinte ip change type [0]
 - Example : ***sudo python3 TORChanger.  
py -t 10 -c 10***
