# -*- coding: utf-8 -*-
import sys, getopt ## getopt <== added new library
import time
import os
import requests
#os.system("clear") <== commented, it's screw up me @_@

def root_check():
    if not os.getuid()==0:
        print("Need Permission root for running this script!")
        sys.exit(1)
    else:
        os.system("service tor start")

def help_args():
    args = sys.argv[1:]
    i = "normal"
    if args:
        i = str.lower(args[0])
    if i == "help" or i == "-help" or i == "--help" or i == "-h":
        print("""'help' or '--help' returns this help\n'-t' time to change Ip in Sec [type=60]\n'-c' how many time do you want to change your ip [type=1000]\nfor infinite ip change type [0]""")
        
def my_ipaddr(): ## ma_ip() changed to my_ipaddr
    url='http://ipecho.net/plain' ## The url's for get your public ip
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',
                                 https='socks5://127.0.0.1:9050'))
    return get_ip.text


#time.sleep(5)
## MAIN Variable ##

def main(argv):
    try:
      opts, args = getopt.getopt(argv,"ht:c:",["tsec=","count="]) ## declaration for optional line args / Argument parsing
    except getopt.GetoptError:
      help_args()
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h' or opt is None:
         help_args()
         sys.exit()
      elif opt in ("-t", "--tsec"):
         global time_var
         time_var = arg
         
      elif opt in ("-c", "--count"):
         count_var = arg
         if str(count_var) == '0': ## force if conditional in here
             start_c()
             
         else:

            for i in range(int(count_var)):
                    #time.sleep(int(time_var))
                change()

          
def start_c():
     while True:
            try:
                    #time.sleep(int(time_var))
                change()
            except KeyboardInterrupt:
                print('auto tor is closed ')
                quit()
                
def change(): ## this function on the top of line in older version
    os.system("service tor reload")
    for i in range(int(time_var)+1): ## the data function of range() changed to int, which was previously a string
        time.sleep(0.1)
        sys.stdout.write((''*(100-i))+("\r [ %d"%i+"s ] "))
        sys.stdout.flush()
    print ('Your IP has been Changed to : '+str(my_ipaddr()))



if __name__ == "__main__": # It's as if the interpreter inserts this at the top of your module when run as the main program.
    root_check()
    main(sys.argv[1:])

## Argument parsing reference link: https://www.tutorialspoint.com/python/python_command_line_arguments.htm
## The older version https://github.com/FDX100/Auto_Tor_IP_changer
## Sometime unexpected closed when infinite requests (API Url's bug)





