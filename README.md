# BeeHive

Given the following (i) Raspberry Pi (ii) Wi-Fi dongle (iii) infrared Raspberry Pi campera and (iv) bee hive housing box - make a live-streaming bee hive box for Kendal's Bees that consumes minimal power and can sustain weather conditions of being on top of the Redwood City Library during the seasons.

# Table of Contents

 I. Find the IP address of your Raspberry Pi.
 
 II. SSH into your Raspberry Pi from your personal computer terminal (headless control).
 
 III. Connecting the Raspberry Pi to the internet with the WPA configuration scripts.
 
 IV. Additional resources for modifying (iii).
 
 V. What to do after you make significant changes to your Raspberry Pi's settings.

# RPI IP Address

Finding the IP address of your Raspberry Pi seems like a daunting task but it is actually quite simple. This can simply be done by opening the terminal application in your Raspberry Pi GUI and typing **hostname -I** after the command prompt which looks like this **pi@raspberrypi:~$**. Be sure to take note of this as it is a critical piece of information to have on hand when you want to make changes to your RPI when you're not physically present next to it.

# SSH From Mac/Ubuntu Terminal

Simply type the following command from your local directory **user:~ user$ ssh pi@localhost**

If you get any other output then the following: **pi@raspberrypi:~$** copy and paste the error code into your favorite search engine and dig through a couple of StackOverflow articles to find the solution. 

# Setting Up Wi-Fi with WPA Configuration files

There are two main files that control the internet connection on the Raspberry Pi: (i) **/etc/wpa_supplicant/wpa_supplicant.conf** and (ii)  **/etc/network/interfaces**. They can both be accessed using *vi* or *nano* to edit the text files. If you want to make your life harder then it needs to be, use *vi*. 
The *.conf* file is the most important. Fill out the appropriate configuration details according to the in line comments. When you are finished *Write Out* and *Exit* the files.

# Additional WPA Configuration Resources

Check out this link for more information on setting up the WPA configuration files. Depending on the network security (usually WPA or WPA2) you'll need to change these settings around as you change the location of the BeeHive Box.

Link: http://bit.ly/2zYjPlD

# After Significant Changes

I know I'm being kind of vague when I say significant changes but when you make significant changes to the Raspberry Pi's advanced settings (overclocking the CPU, changing wireless networks, wiping code off of it for a new project, etc.) it's good to get into the habit of rebooting the RPI to get a fresh start so to speak at debugging issues. 

Type the following command to reboot your Raspberry Pi: **sudo reboot**

For more advanced restart/shutdown procedures append the aforementioned command with the **--help** flag to find out more information. 

# Start/Stop RPi Livestreaming

To start the livestreaming enter the following commands after successfully SSH-ing into the RPi: **docker start cam**

To end the livestreaming enter the following commands: **docker stop cam**
