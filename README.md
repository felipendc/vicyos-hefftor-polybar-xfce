![logo](https://raw.githubusercontent.com/adi1090x/polybar-themes/master/previews/logo.png) <br />
Down below you will find a modified version of the Polybar baked-in [Arcolinux-Hefftor-HLWM](https://www.youtube.com/watch?v=iwWSqCDeWgk).<br /> 

**If you want to try it out and don't know how to install it...** In this [video](https://www.youtube.com/watch?v=zfLYqie-q7A&list=PLEHnzNeoCcNxPukIVaMPCO_QRxZtYPvD3&index=4) I show step-by-step how to install the polybar on your Xfce. <br />

------
<video src="https://www.youtube.com/watch?v=zfLYqie-q7A&list=PLEHnzNeoCcNxPukIVaMPCO_QRxZtYPvD3&index=4" width="320" height="200" controls preload></video>

------

***Warning:*** This Polybar just gives support to Xfce. I don't know if it will work on KDE. (You can try it, by your own risk!)
<br />

------

**The begining...** You may be thinking: Hm... Cool, but... why Xfce?<br />

This is the question, this is why! Let me think where to start from....<br />

I've never seen any Polybar been used on an Xfce, so far. Then, I thought: why not? Why not to bring this beaulty to Xfce?<br />
Because most of the time it's usual to see it with [Tiling Window Manager](https://www.youtube.com/watch?v=Lj1IfdKY0CU), such as:<br /> 

<pre>Herbstluftwm (HLWM), Bspwm, Awesome, i3, XMonad... Just to name a few.</pre>

I just wanted something different! So, I came up with this idea, to try to adapt a Polybar to Xfce.<br />

That was very tiring, by the way... but after a long and hard work, I made it!<br />
Now, I will try to show you, what I've made, and how you can modify it, to help you to suit your needs!<br /> 
<br>

**Aditional information:**<br /> 

For a better experience, I do recomend you to try the "Vicyos-Hefftor-Polybar" together with [Arcolinux Hefftor Edition Xfce](https://www.youtube.com/watch?v=xRMeoQZFB3E).


**I don't know if you have ever listened to these songs... So, [check](https://www.youtube.com/watch?v=o3hf6lgC3-Q&t) them [out](https://www.youtube.com/watch?v=d1NSgR4svTg&t)...** <br />
![Demo](https://i.imgur.com/VEt6nrp.png)

------
<br> 
<br> 

**Let's start talking about the space between the "Polybar" and a "Window"!**<br /> 

Hey, boy... I told you, I wanted something different! Most of the time, when a user maximaze a window, it gets lined up with the "taskbar". I think, this small detail, gave the Polybar a better looking!

![Demo](https://i.imgur.com/ywnwnGG.png)
<br>

------
<br> 
<br> 

**How can I change the size of the space between the "Polybar" and the "Window"?**<br /> 

It's very simple. You just need to edit the line:<br />

<pre>border-bottom-size =</pre>

The default is:<br />

<pre>border-bottom-size = :6</pre>

Change it to your needs.<br />

![Demo](https://i.imgur.com/9Yd82PO.png)

<br>
<br>

**Border bottom size  set with 12**<br />

In this second picture, I had set it with: "12", just to show you how the space between the "Polybar" and the "Window" would feel like.<br />

<pre>border-bottom-size = 12</pre>

![Demo](https://i.imgur.com/dmJTGFC.png)

------
<br> 
<br> 

**There is also a space between the "top of the screen" and the "Polybar"**<br />

If you also want to change the size between the "top of the screen" and the "Polybar, you just need to change the line:

<pre>offset-y = </pre>

The default is:<br />

<pre>offset-y = :4</pre>

Change it to your needs.<br />

![Demo](https://i.imgur.com/0d3FxHD.png)

------

<br> 
<br> 

***Border right and left resized to get more room*** <br />

As you know, my laptop has a "14.0-inch display".<br />
So, I had to resized the Polybar borders to get more space.<br /> 

In this Polybar version I've set the the default to: 16 for each side.<br /> 
You can play around with the numbers, to fit your needs.<br />

![Demo](https://i.imgur.com/fKaxJ9w.png)

------
<br> 
<br> 

**The "Start Button" is in the building!!!**   What a minute... what is it and why is it in the center?<br />

Hey, relax... I can explan it.<br />
 
It's pretty simple. This button "fires up" the Whisker-Menu.<br />
I think that, this was the perfect position to place it. **"And you will understand why it's in the center"** pretty soon...<br />
And before you ask me: Why does it have two fire icons? It's to fire up the Whisker-Menu, and it gives the Polybar a nice look and feel.<br />

![Demo](https://i.imgur.com/2gP1vOy.png)

##

![Demo](https://i.imgur.com/EPXGQkP.png)

------
<br> 
<br> 

**Am I the only one who noticed that the "System-Tray" isn't on the Polybar?** So, where's it, though?<br />

Well, that's another reason why the "Start-Button" is in the center of the Polybar. The "System-Tray" is already difined on the "xfce-taskbar" by default. If I try to enable it on the Polybar, it won't work.<br />

But, don't worry! I made a package with my xfce-taskbar presets. In the video where I show you how to install the Polybar, I show how to restore all of my xfce settings.<br />

And you will get an xfce-taskbar equal to the picture below:<br />

![Demo](https://i.imgur.com/h5ifkYr.png)

------
<br> 
<br> 

***Now, let's talk a little bit about this CPU-GRAPH. And, Nope. It's not a "Sound Spectrum". Yes! you were wrong. Hahahaha I was too, when I saw it for the first time.***<br />

The screenshot down below, shows us the Cpu-Graph module. I took this screenshot just to show you that if you want to increase the velocity of the interval between the bars updates, you just need to chenge the line:<br /> 

<pre>interval =</pre> 

The default is:<br /> 

<pre>interval = 0.08</pre> 

Change it to your needs.<br />

![Demo](https://i.imgur.com/7g2TNcr.png)

------
<br> 
<br> 

***The Xwindows is "still" in the building !!! Here is why...***<br />

It reminds me of the "global menu" from "Ubuntu 16.04" and "Mac O.S". Even though "Xwindows" doesn't act the same here. Hahaha. But I like it.<br />

![Demo](https://i.imgur.com/VGz3pID.png)

------
<br> 
<br> 

***Weather Module, and why it's very import to bring it up***<br />

This is the part where you will learn how to do your modifications!<br /> 
I decided to take this screenshot, to make it easy for you to understand.<br />
As my laptop has a very small screen. I modified the weather code, so that the weather icone would fit the screen.<br />

The line: 34, is the default configuration. And I commented using the "#". The default line prints the Weather result in Celsius, (°C) and with informatition if the sky is cloudy.<br />

e.g:<br /> 


<pre>Cloudy sky, 23°C  
Clean sky, 30°C</pre>

The line: 42, is my modified version, where it just prints out the Weather results in Celsius, (°C) with no string (Letters information).<br />

e.g:<br /> 

<pre>30°C</pre> 

As in the screenshot down below:<br />

![Demo](https://i.imgur.com/ETF2tEO.png)

<br>
<br>

## Weather Module - Additional Information!

To switch to your weather "city or location", you just need to edit the file "weather.py" at: <br />

<pre>/home/user/.config/polybar/scripts/</pre>

or<br />

<pre> nano ~/.config/polybar/scripts/weather.py</pre>

![Demo](https://i.imgur.com/oGj7B9Z.png)

------
<br> 
<br> 

**Date and Clock Modules are separated from each other and got new icons!**<br />

In this Polybar version for Xfce, I seperated the "Date" from the "Clock" module. I also added especific icon for each one.<br /> It gave them a better feel.<br />

![Demo](https://i.imgur.com/TJySv5M.png)

##

![Demo](https://i.imgur.com/nN2WOFM.png)


------
<br> 
<br> 

**MPD module is in the building!!!**<br />

If you like use [mpd](https://www.youtube.com/watch?v=NNNl7p9LiKw), you can enable it manually. It's not enabled on the Polybar by default.<br />

![Demo](https://i.imgur.com/YJhcKZH.png)

------
<br> 
<br> 

**CPU THERMAL SENSOR PATH** How can I get it?<br />

If you are having problems with the "CPU Thermal Sensor Module" not showing on your Polybar, you will need to give the Polybar the exactly "path" (location) of your CPU Thermal Sensor.<br /> 

To solve it, you just need to watch my [video](https://www.youtube.com/watch?v=arD0JUP0pi0&list=PLEHnzNeoCcNxPukIVaMPCO_QRxZtYPvD3&index=2), where I show you how to do it.<br />  

![Demo](https://i.imgur.com/QNCmLEW.png)

------
<br> 
<br> 

***Pavucontrol is also in the building, in this version!!!*** <br />

I got very happy when I managed to create this module made it work on my last [Tiling Window Manager polybar](https://github.com/felipendc/vicyos-hefftor-polybar), so, I decided to bring it to this Xfce version,<br />

![Demo](https://i.imgur.com/a4MUJZD.png)

------
<br> 
<br> 

**A better way to know when to update the programs and packages!**<br />

I was looking foward to bring this module from [vicyos-red-dark-polybar](https://github.com/felipendc/vicyos-red-dark-polybar) to this "Xfce Polybar" version!<br />

I also adapted its module to work in this version. Oh god! that was very, very hard and tiring. <br />
But, thanks God! I managed to make it functional in this version. <br />

Whenever a new "update" is available, you just need to click on the "Box Icon" on the Polybar and a terminal window will pop up asking for your password to update all of the outdated packages!<br />

When the update installation finish, the terminal window will close it down. <br />
 
<br>

**Warning:** <br />

I've adapted it to work on in Arch based distros. <br />
But, don't worry, in the picture below, I show you what to do if you are running Ubuntu or any other Distro based on Ubuntu or Debian.<br />

![Demo](https://i.imgur.com/P7E3rIv.png)

##

![Demo](https://i.imgur.com/V2mqa7m.png)

------
<br> 
<br> 

**How to auto-start the this Polybar together with Xfce**<br />

That was the most difficult part of this Polybar developement.<br />

Whenever I rebooted the computer the Polybar didn't autostart with the System...<br />
 
But after a long 3 days of trials and errors and a "Solo Brainstorm" (Solo = Alone) Hahaha... I finally managed to create this script and adapt it to work with this Polybar.<br />

Yes! I took three days to make it funcional. Hahahahah. Because I hadn't find any clue on the internet. So, I decided to mashup (tailor it) [Erick's](https://www.youtube.com/watch?v=HOc8ZAGyJPU) video tutorial to this polybar. And here we are!<br />

Don't forget to move or copy it to your "autostart" folder:<br />

<pre>/home/user/.config/autostart/</pre>

Doing this, this Polybar will autostart with the Operating System!<br />

![Demo](https://i.imgur.com/1xm6vOl.png)

------
<br> 
<br> 

### Special Thanks to:

[Felipe Ndc (Vicyos)](https://www.youtube.com/channel/UCHgDwde2kTdKI53LRm3pTtQ/videos) Yeah. It's me.<br />
[adi1090x](https://github.com/adi1090x/polybar-themes)<br />
[Erick Doubis](https://www.youtube.com/user/maclover696)<br />
[Brad Heffernan](https://www.youtube.com/user/shamrock677)<br />
[Marcos Oliveira](https://terminalroot.com.br/2019/07/uma-colecao-de-temas-prontos-para-seu-polybar.html)<br />
[ChmOd](https://discordapp.com/invite/R2amEEz) in ArcoLinux-Group on Discord<br />



##
