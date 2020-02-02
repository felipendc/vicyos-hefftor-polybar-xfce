![logo](https://raw.githubusercontent.com/adi1090x/polybar-themes/master/previews/logo.png) <br />
Down below you will find a modified version of the Polybar baked-in [Arcolinux-Hefftor-HLWM](https://www.youtube.com/watch?v=iwWSqCDeWgk).<br /> 

**If you want to try it out and don't know how to install it...** In this [video](https://www.youtube.com/watch?v=Q2IhW4iGwGY&list=PLEHnzNeoCcNxPukIVaMPCO_QRxZtYPvD3), I show step-by-step how to install the polybar. <br />

------

***Warning:*** This Polybar just gives support to Herbstluftwm (HLWM) and BSPWM. And I have just tested in Herbstluftwm, so far, due to lack of time.
<br />

------


**I know you also want to listen to this song... Hey, [Don't](https://www.youtube.com/watch?v=wVd0s7scl5U) tell [anybody](https://www.youtube.com/watch?v=hQ4r_kcvClE)...** <br />

![Demo-Pip](https://i.imgur.com/WHWA6ZE.jpg)

------


**This is the very new modified version of this Polybar. It might seem kind of bloated but, dont't worry. It's just my Laptop screen.**<br />

In this version, I customized it to suit my daily needs. And I'm also been a good guy to my younger brother and for some newbies. Why?<br /> 
Look at those "Terminal, File Manager, Chromium Browser and Pavucontrol". It will give them a hand. And the newbies I mean: "My Mom & Sister".<br /> 

![Demo](https://i.imgur.com/ns7i3tR.jpg)

------


***Oh, boy... Is the System-Tray back??? This is awesome! But, what about the Workspaces???***<br />

Well, I was obligated to change the position of the Workspaces from the center to the left side. Why?<br />
It's simple...<br />

1 - I'm very dependent on the System-tray (Sys-tray), in my daily usage, I use some apps that are just available on the System-tray.<br />
2 - I use my laptop most of the time, and everywhere I go, I bring it with me.<br />
3 - Wifi Icon. When the Sys-tray is enable, I don't need to use some lines of code to connect to the internet.<br />
4 - Oh, boy, image my sister or my mom, trying to use: 

<pre>nmcli d wifi list</pre> 
and<br /> 
<pre>nmcli d wifi xxxx password xxxx</pre> 

(Yeah, I know, I have commom sense).<br />

5 - Just to wrap up about the Sys-Tray subject... I could've put it on the left or right side of the Polybar. But, it got all weird, due to the lack of "Sys-Tray-Radius" support to get the rounded borders.<br />  

I don't know if you noticed but, I also changed the Workspace Icon with a circle, rounded with dots. I wanned something diffent and cool.<br />

PS: Yep! The Volume Bar Icone was downsized...<br />

![Demo](https://i.imgur.com/1Yp2CWl.jpg)

------


***Now, let's talk a little bit about this CPU-GRAPH. And, Nope. It's not a "Sound Spectrum". Yes! you were wrong. Hahahaha I was too, when I saw it for the first time.***<br />

The screenshot down below, shows us the Cpu-Graph module. I took this screenshot just to show you that if you want to increase the velocity of the interval between the bars updates, you just need to chenge the line:<br /> 

<pre>interval =</pre> 

The default is:<br /> 

<pre>interval = 0.08</pre> 

Change it to your needs.<br />

![Demo](https://i.imgur.com/8z7bifV.jpg)

------


***The Xwindows is in the building this time!!! Here is why...***<br />

It's very complicated when you are on a "frame in HLWM" and you don't have any idea about what's the active windows name.<br />

So, that's why it's back. And I like it.<br />

![Demo](https://i.imgur.com/XUq7Vq7.jpg)

------


***Weather Module, and why it's very import to bring it up***<br />

This is the part where you will learn how to do your modifications!<br /> 
I decided to take this screenshot, to make it easy for you to understand.<br />
As my laptop has a very small screen. I modified the weather code, so that the weather icone would fit the screen.<br />

The line: 34, is the default configuration. And I commented using the "#". The default line prints the Weather result in Celsius, (°C) and with informatition if the sky is cloudy.<br />

e.g:<br /> 


<pre>Cloudy sky, 23°C  
Clean sky, 30°C</pre>

The line: 38, is my modified version, where it just prints out the Weather results in Celsius, (°C) with no string (Letters information).<br />

e.g:<br /> 

<pre>30°C</pre> 

As in the screenshot down below.<br />

## Additional Information!

To switch to your weather "city or location", you just need to edit the file "weather.py" at: <br />

<pre>/home/user/.config/polybar/scripts/</pre>

or<br />

<pre> nano ~/.config/polybar/scripts/weather.py</pre>


![Demo](https://i.imgur.com/rvHFbNd.jpg)

------


***Border right and left resized to get more room*** <br />

As you know, my laptop has a "14.0-inch display".<br />
So, I had to resized the Polybar borders to get more space.<br /> 

In this Polybar version I've set the the default to: 16 for each side.<br /> 
You can play around with the numbers, to fit your needs.<br />

![Demo](https://i.imgur.com/Aane1MZ.jpg)

------


***Here you can play around with the position of the modules...*** <br />

Make your self at home! Feel free to make them sit your needs!<br />

![Demo](https://i.imgur.com/nSLWsXH.jpg)

------


***Pavucontrol is now in the building!!!*** <br />

I got very happy when I managed to create this module made it work on the polybar. Why?<br />
I think, I've forgot to mention that I also have a Desktop and this module is very handy, when it comes to switch between audio-output.<br />

The reason I made a module for pavucontrol is because the system-tray doesn't have its option.<br />
And I'm constantly switching the audio-output from Headset to the speakers. And as I said, I'm not the only one who uses the computer.<br />

![Demo](https://i.imgur.com/rgUo5ci.jpg)

------


***Different color for the Polybar modules***<br />

Most of the modules on the Polybar has a diffrent icon and underline-format color, for a better looking.<br />
![Demo](https://i.imgur.com/LeTMgC3.jpg)

------


***Power Menu Not being overlayed anymore... Unless you have a smaller display than my 14 inch display laptop. Hahaha***<br />

Now, in this Polybar with both borders sized to 16, when you click on the Power Menu, its not overlayed due to lack of space.<br />
If you are still getting problems with it getting overlayed, you will just need to downsize it.<br />

![Demo](https://i.imgur.com/eQa4iBV.jpg)

------


***Is the Browser Icone not working?***<br />

Calm down, relax... Don't panic!<br />

In order to use that 'Browser Icon' on the Polybar, don't forget to install 'Chromium'.<br />

##

If you are using any Distro based on Arch Linux, like me... use this command:<br />
<pre>trizen -S chromium</pre>

##

If you are using any Distro based on Ubuntu Linux, use this command:<br />
<pre>sudo apt-get install chromium-browser</pre>

##

If you are using any Distro based on Fedora Linux, use this command:<br />
<pre>sudo dnf install chromium</pre>



![Demo](https://i.imgur.com/RAdf6lZ.jpg)

------



***Hey, bruh, what if I don't want to use Chromium Browser? <br />***

Well, It's pretty simple. You just need to go to:<br />

<pre> cd ~/.config/polybar/config</pre>

------



## // IMPORTANT NOTE: 
### Now, if you decide to remove the System-Tray... You will need to follow these steps down below to connect to any Wifi networks. 

 ***Oh, God! How can I connect to a wifi connection? Where's the wifi icon? <br />***



Relax, You just need to open your lovely "Terminal" and type: <br />

<pre>nmcli d wifi list</pre>

This command above will list all the wifi connections available. So, you just need to copy the name of the wifi you want to connect. You will find it under 
*SSID* row. <br />


Then, use this command:<br />

<pre>nmcli d wifi connect YYYYY password XXXXX</pre>

Instead of YYYYY you will put the name of the Wifi. Or in other words: "Wifi ID"<br />
Instead of XXXXX you will put the Wifi password<br />

------


***Now, take a look at the screenshot down below and see how it's done:***

![Demo](https://i.imgur.com/0PiJS3n.jpg) <br />

This step-by-step to connect to your wifi, was only possible thanks to [Brad Heffernan](https://www.youtube.com/watch?v=SXZYJ4fa0C0&t=159s)

------

### Special Thanks to:
[Erick Doubis](https://www.youtube.com/user/maclover696)<br />
[Brad Heffernan](https://www.youtube.com/user/shamrock677)<br />
[Marcos Oliveira](https://terminalroot.com.br/2019/07/uma-colecao-de-temas-prontos-para-seu-polybar.html)<br />
[Felipe Ndc (Vicyos)](https://www.youtube.com/channel/UCHgDwde2kTdKI53LRm3pTtQ/videos) Yeah. It's me.<br />
[ChmOd](https://discordapp.com/invite/R2amEEz) in ArcoLinux-Group on Discord<br />

------
