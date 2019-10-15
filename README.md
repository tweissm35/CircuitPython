# Projects
Here are all the projects I've done so far. I'm probably working on one now!:squirrel: 
## Fade
This project was relatively staightforward, only requiring that we get an led to fade on and off. The difficulty came in using a different language and editor than normal. Also, duty cycles were completely new and took me a little bit to grasp. The only wiring this project needed was one led.
<br><img src="media/fade.jpg" width="300">
## Servo
This project was also fairly straight forward for me. The goal was to have a servo that can be controlled with two wires using capacitive touch. Using pulseio for pwm also took me a bit, but I got the servos working and also got the capacitive touch working. You can control the servo just by grabbing the end of a wire. Cool!
<img src="media/servo.jpg" width="300">
## LCD screen
I had a bit of trouble with this one. The goal was to make the screen display a number that would count up if a switch was one way and down if it was the other. I had trouble clearing the screen after the number increased or decreased. This meant that I would have left over negative signs or zeros that shouldn't have been there. The problem turned out to be that I wasn't printing enough spaces.
## Distance Sensor
I had a tough time with this one. The goal was to have the metro's onboard led change color according to the distance an ultrasonic sensor was reading. I decided to use hue, saturation, value instead of RGB and it took me a while to find a suitable library. After that I needed some functions that I didn't have and needed to make myself. Another problem I had was that the colors were opposite to what I wanted, for example, I wanted it red when it was close and green when it was far away, but it was the opposite. All I had to do was switch the distance values inside my map function.
<img src="media/ultrasonicsensor.jpg" width="300">
## RGB Class
This one was tricky. The goal was to create a class with a few functions and make two different RGB leds make some pretty colors. The first mistake I made was I forgot that they were common cathode instead of common anode leds. That was an easy fix that took me a while to figure out. After that I was able to get it working pretty easily.
<img src="media/rgb.jpg" width="300">
## Fancy LED
This one wasn't too bad. The goal was to create class that makes leds light up in patterns. I was on this assignment and I couldn't figure out why none of my LEDs were turning on. The answer was that I forgot the .value after the led I wanted, something that is very basic for digitalio.
<br><img src="media/fancyLED.jpg" width="300">