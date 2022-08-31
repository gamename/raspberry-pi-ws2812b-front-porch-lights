# Table of Contents
  - [Overview](#overview)
  - [Technical Description](#technical-description)
  - [High Level Diagram](#high-level-diagram)
  - [Pictures](#pictures)
  - [Parts List](#parts-list)
  - [Assembly Notes](#assembly-notes)
  - [FAQ](#faq)
<br><br>
# Overview
This is a fairly simple implementation of a raspberry pi using a light sensor to control an LED strip. The LED strip is for porch lights 
on my townhouse.

<br><br>
# Technical Description
This uses a Raspberry Pi (RPi) 3b to control a WS2812b LED strip. The LED strip is strung along the top edge of the porch. Each LED strip
is enclosed in an aluminum rail and covered with a plastic diffuser (see "light rails" in parts list below). 

Even though the LED strip is connected to the RPi for power and control, it cannot supply enough amperage to drive the whole strip. So,
there is an additional external power supply connected at both ends. 

The external power supply, a surge protector, and the RPi are all housed in a junction box. The light sensor is connected to the RPi too,
but is housed externally in a small hobby box. 

<br><br>
# High Level Diagram

<br><br>
# Pictures

<br><br>
# Parts List
1. [Light detector](https://a.co/d/iatWxzP)<br>
2. [junction box](https://www.amazon.com/dp/B07FFMW98K?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_Q53R1K17GV35AD7ETD8T)<br>
3. [light rails](https://www.amazon.com/dp/B07F923CXW?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_M3PXQB7NWN6M433SQ13D)<br>
4. [modular light connectors](https://www.amazon.com/dp/B01DC0KIT2?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_7FPAXEZCGPNJF75B87AH)<br>
5. [power supply](https://www.amazon.com/dp/B07TSKK4FR?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_C5H0VB2ZD7X5N9FWS5ZP)<br>
6. [power strip](https://www.amazon.com/dp/B0B38J2RCW?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_NGQSWW4XAKX024N8B75Q)<br>
7. [raspberry pi 3b](https://a.co/d/4W5xzi1)<br>
8. [raspberry pi 3b case](https://a.co/d/iEvAVKc)<br>
9. [modular power connectors](https://www.amazon.com/dp/B07RW6XVWZ?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_FFTEP0FKJS06ZBFZYE9B)<br>
10. [crimping tool](https://www.amazon.com/dp/B07GFLWKTT?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_CJ3GNW5Q23350F62M5Q7)<br>
11. [cable glands](https://a.co/d/7p3MsaF)<br>
12. [3 conductor wire](https://www.amazon.com/dp/B06Y4716V7?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_BY7KKMJT11VS7TR2KW9B)<br>
13. [shrink tubing wire connectors](https://www.amazon.com/dp/B09FLZQQ95?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_VAFF6WAG78XBAE2WKR9X)<br>
14. [usb to mini usb connector](https://www.amazon.com/dp/B004GETLY2?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_S4YZF2V6R8KAVAPN4BF1)<br>
15. [ws2812b led strips](https://www.amazon.com/dp/B01CDTEID0?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_XNF847VSW59MR645S7A1)<br>
16. soldering iron + solder OR [strip joiners](https://www.amazon.com/dp/B09L117LB5?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_00Q135WVJKDME1CT3KP9)<br>
17. [wire channels](https://www.amazon.com/dp/B09M8M7NST?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_13G2RZVQ06KH456VK7W4) (for the floor)<br>
18. [small hobby box](https://www.amazon.com/dp/B07ZRBND1L?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_RJV7A9WXKJSVNYJR8R9G)<br>
19. [screws](https://www.amazon.com/dp/B09955X4K1?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_1616D3FTKE2ZM7T3154G)<br>
20. drill with phillips head drill bit <br>
21. ladder<br>
22. tape measure<br>
23. [cable ties](https://a.co/d/6m9v6Om)<br>
24. [cable hiders](https://a.co/d/gkcMCfV) (wall)
25. [cable hiders](https://a.co/d/eZ0RxNR) (floor)
26. [casters](https://a.co/d/86DZQPY) (for junction box)

<br><br>
# Assembly Notes
1. The LED strip length needed was about 28 feet.  So I had to join 2 strips together. In my case, I simply soldered the 2 strips together
[using this technique](https://youtu.be/RFv19s15RuM).  But I added the "strip joiners" (above in parts list) in case someone wanted to avoid soldering.<br>
2. I had to cut the power cord on the surge protector, run it into the junction box via a small hole, then reattach it afterwards.<br>

<br><br>
# FAQ
Q. Isn't a Raspberry Pi overkill for this application?<br>
A. Yes and no.  It is possible to do this sort of thing with a cheaper ESP32 device, that's true.  But on the other hand, 
the Raspberry Pi has a full-featured operating system. That allows me to SSH into it and make changes very easily. In addition,
I'm considering making this whole configuration an Internet of Things (IoT) application with controls on Amazon Web Services (AWS).
Doing that will require something more powerful - like a Raspberry Pi. 
<br><br>
Q. How long did it take to put this all together?<br>
A. At least 1 day.  It took a while to hang all the LED strip lights 
<br><br>

