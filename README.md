
# Table of Contents

# Overview
This is a fairly simple implementation of a raspberry pi using a light sensor to control an LED strip. The LED strip is for porch lights on my townhouse.

# Technical Description
This uses a Raspberry Pi 3b to control a WS2812b LED strip. The LED strip is strung along the top edge of the porch. Each LED strip
is enclosed in an aluminum trough, or strip, and covered with a plastic diffuser. At each end is a power connection for a 5v power
supply and ground.  At one end is a separate 5v power connection, a ground connection, and a control connection which are all
attached to the Raspberry Pi. The separate power supply is needed because the there are approximately 510 pixel lights to be driven.
THe power supply, a power strip, and the Raspberry Pi are all housed in a junction box.  

# High Level Diagram

# Pictures 

# Parts List
[Light detector](https://a.co/d/iatWxzP)<br>
[junction box](https://www.amazon.com/dp/B07FFMW98K?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_Q53R1K17GV35AD7ETD8T)<br>
[light rails](https://www.amazon.com/dp/B07F923CXW?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_M3PXQB7NWN6M433SQ13D)<br>
[modular light connectors](https://www.amazon.com/dp/B01DC0KIT2?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_7FPAXEZCGPNJF75B87AH)<br>
[power supply](https://www.amazon.com/dp/B07TSKK4FR?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_C5H0VB2ZD7X5N9FWS5ZP)<br>
[power strip](https://www.amazon.com/dp/B0B38J2RCW?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_NGQSWW4XAKX024N8B75Q)<br>
[raspberry pi 3b](https://a.co/d/4W5xzi1)<br>
[raspberry pi 3b case](https://a.co/d/iEvAVKc)<br>
[modular power connectors](https://www.amazon.com/dp/B07RW6XVWZ?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_FFTEP0FKJS06ZBFZYE9B)<br>
[crimping tool](https://www.amazon.com/dp/B07GFLWKTT?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_CJ3GNW5Q23350F62M5Q7)<br>
[cable glands](https://a.co/d/7p3MsaF)<br>
[3 conductor wire](https://www.amazon.com/dp/B06Y4716V7?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_BY7KKMJT11VS7TR2KW9B)<br>
[shrink tubing wire connectors](https://www.amazon.com/dp/B09FLZQQ95?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_VAFF6WAG78XBAE2WKR9X)<br>
[usb to mini usb connector](https://www.amazon.com/dp/B004GETLY2?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_S4YZF2V6R8KAVAPN4BF1)<br>
[ws2812b led strips](https://www.amazon.com/dp/B01CDTEID0?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_XNF847VSW59MR645S7A1)<br>
soldering iron + solder OR [strip joiners](https://www.amazon.com/dp/B09L117LB5?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_00Q135WVJKDME1CT3KP9)<br>
[wire channels](https://www.amazon.com/dp/B09M8M7NST?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_13G2RZVQ06KH456VK7W4) (for the floor)<br>
[small hobby box](https://www.amazon.com/dp/B07ZRBND1L?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_RJV7A9WXKJSVNYJR8R9G)<br>
[screws](https://www.amazon.com/dp/B09955X4K1?_encoding=UTF8&psc=1&ref_=cm_sw_r_cp_ud_dp_1616D3FTKE2ZM7T3154G)<br>
drill with phillips head drill bit <br>
ladder<br>
tape measure<br>
[cable ties](https://a.co/d/6m9v6Om)<br>


# Assembly Notes

# FAQ
Q. Isn't a Raspberry Pi overkill for this application?<br>
A. Yes and no.  It is possible to do this sort of thing with a cheaper ESP32 device, that's true.  But on the other hand, 
the Raspberry Pi has a full-featured operating system. That allows me to SSH into it and make changes very easily. In addition,
I'm considering making this whole configuration an Internet of Things (IoT) application with controls on Amazon Web Services (AWS).
Doing that will require something more powerful - like a Raspberry Pi. 
<br><br>
Q. How long did it take to put this all together?<br>
A. About 2 days.  It took a while to hang all the LED strip lights 
<br><br>

