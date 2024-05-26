# Obvious

The Obvious is a Raspberry Pi that runs the dictonary! We made this to act like the [Ovilus](https://www.digitaldowsing.com/) which is used in various ghost hunting shows.  You will need an LED display and buttons. 

* Please note this was written for an older linux kernel.  This may not work due to the kernel update for Raspberry Pi. 

* [Watch it in action](https://www.tiktok.com/@tnohparanormalsociety/video/7148853468009123115?is_from_webapp=1&sender_device=pc&web_id=7373326302117414430)

## Step 1:

Get a Raspberry Pi, LCD Display, and buttons. 

## Step 2:

Put the `randomwords` folder in your home directory. 

Example: `/home/rachael/randomwords/`

## Step 3:

Copy the shell script `rc.local` file to here: `/etc/rc.local`

This is the file that will start up your program when you turn on your Raspberry Pi. It's a linux thing.

## Step 4: 

Copy the shell script `randwords.sh` file to here: `/usr/local/sbin`

This is what the `rc.local` file is looking for. It will run these commands everytime you press the button!

```
cd /home/pi/randomwords/
python3 randomwords.py
```

## Quick Start
![Start up](https://i.imgur.com/fjx8aiI.jpg)
![Clearing Hardware Random Memory](https://i.imgur.com/RblEgYr.jpg)
![Your word is Calendar](https://i.imgur.com/U8vOluu.jpg)
![Click for new word](https://i.imgur.com/JDjqOKD.gif)

The left button in the image will start a new sesson. 


![Shut down](https://i.imgur.com/SkHHBk5.gif)

The far right button will turn off the Raspberry Pi for you. Wait for 15 seconds before unplugging. 


## Accessories

Battery bank. I have an old battery from ThinkGeek that works great! Now it is portable. 
![battery](https://i.imgur.com/Qyyv89l.jpg)