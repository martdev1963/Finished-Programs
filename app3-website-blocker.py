# Program Architecture
# Mac and Linux: /etc/hosts
# Windows: c:\windows\Systems32\drivers\etc
# for windows machines...
#hosts_path="c:\windows\Systems32\drivers\etc\hosts"
#hosts_path=r"c:\windows\Systems32\drivers\etc\hosts"   #... using the r flag to tell python you are passing a real string not a /w special char...
# or use this alternate solution:
#hosts_path="c:\\windows\\Systems32\\drivers\\etc\\hosts" #  using two back slashes...
# for mac and linux machines...
# -------------------------------------------------------FOR WINDOWS-------------------------------------------------------------#
# To run your python apps in the background in Windows, you use the pythonw.exe ...instead of the regular python.exe script.     #
# you must change the extention of your python scripts from .py to .pyw                                                          #
# to launch your script now, you simply double click it...you can now see the pythonw script in the task manager list.           #
# You don't see any output nor do you see your script in the task manager, however you do see the pythonw.exe script.            #
# create a task to run your script automatically: Go to task scheduler and under actions Create task.                            #
# Put a name for the task. Select Configure for: ie: Windows 7. Check "Run with highest priviledges"...this will require         #
# administrator rights, otherwise any user can run it. Go to Triggers tab, select New Trigger. In the Begin the task dropdown,   #
# select At startup. Click ok. Go to Actions tab. Create a New Action. In the Action dropdown, choose Start a program.           #
# Point to your program script by browsing to it. Click open. Click ok. Click on Conditions tab. Where it says Power, unclick    #
# 'Start the task only if the computer is on AC power.' Press ok. You should now see your script in the scheduler cue.           #
# your script won't run unless the path to your hosts file is absolute...not a relative path. (The pythonw.exe won't run)        #
#--------------------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------FOR MAC AND LINUX-----------------------------------------------------------#
# Open a terminal shell by right clicking on your script. Type in atom . from the /applications directory. Atom opens...         #
# Change the path in hosts_paths="/etc/hosts" Save the script. To check your hosts file, run sudo nano /etc/hosts                #
# Control x to exit. start your script as administrator with sudo python3 website-blocker.py, Check hosts file again             #
# the websites to be blocked should be there. Open cron table to add your script. in the shell, type crontab .e hit return       #
# This opens the crontab file. This however is the crontab file thats accessible by the normal user. So exit and open as sudo.   #
# sudo crontab .e  notice the .e flag. this will execute your script as an administrator (with high priviledges)                 #
# Because the hosts file is protected by Linux and/or Mac OS. With the crontab file now opened, append the following:            #
# reboot python3 /Documents/mapping/app3-website-blocker.py# then Control x y and enter. If you open crontab without sudo now,   #
# you will see the crontab file version for all users not the sudo crontab file version you just appended to.                    #
# If you point your hosts_paths variable to a relative path instead of an absolute path python will not be able to access that   #
# relative path cuz crontab will execute python from another directory which is different from where the website-blocker         #
# script is located. So its good to work with absolute paths when needing to access files.                                       #
#--------------------------------------------------------------------------------------------------------------------------------#


import time
from datetime import datetime as dt # using the namespace dt for a more concise reference name in the code...s
hosts_paths= "/etc/hosts" # not used in this case.
hosts_temp="hosts_copy.txt" # using this variable instead...
# redirects to hosts machine...
redirect="127.0.0.1"
# websites to block during specific times of the day...
website_list=["www.facebook.com","facebook.com", "www.twitter.com", "twitter.com"]

# datetime.datetime(2018, 7, 10, 15, 59, 21, 697959) date, hour, minutes, seconds, micro seconds...
# can break script with ctrl c for mac...
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16): # checking for working hours...8am to 16:00(4:00pm)

        print("Working Hours... ")
        with open(hosts_temp, 'r+') as file: # r+ allows for reading and appending to a file... the w flag would erase previous data in the file...
            content=file.read()
            #print(content)
            for website in website_list:
                if website in content:
                    pass # this will make python skip to time.sleep(5) line of code...
                else:
                    file.write(redirect +" "+ website+"\n") # write this into the hosts_copy.txt file...
    else:
        with open(hosts_temp, 'r+') as file:
            content=file.readlines() # better than read() in this case cuz it will produce lines instead of just one stream of text...
            # there is now a pointer at the end of the content variable...
            file.seek(0) # pointer is set to first char of the first line in the content variable
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line) # rewrite the content in the host file line by line.
            file.truncate() # truncates everything after last line previously read or written...thus truncating the websites...
        print("Fun Hours... ")
    time.sleep(5)
    print("Five seconds have past... " + str(dt.now().second)) # <----TypeError: must be str, not int due to passing dt.now().second)
    # fixed it with str(dt.now().second))...converted int to string with str()...
