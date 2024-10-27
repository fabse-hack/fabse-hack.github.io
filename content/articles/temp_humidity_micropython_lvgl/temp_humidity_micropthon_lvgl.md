---
Title: temp_humidity_micropython_lvgl
Description: Temperature and Humidity with MicroPython and LVGL
Date: 2024-10-27
Author: fabse
Tags: Micropython
Category: Projects
Summary: This project demonstrates creating a temperature and humidity display on the ESP32-S2 Mini using MicroPython, LVGL, and Squareline Studio.
featured_image: /articles/temp_humidity_micropython_lvgl/photos/temp_humidity_micropython_lvgl.jpg
---
# Temperature and Humidity with MicroPython and LVGL
  
**Content:**  
- [Temperature and Humidity with MicroPython and LVGL](#temperature-and-humidity-with-micropython-and-lvgl)
- [Hardware](#hardware)
- [Project Description and github repo link](#project-description-and-github-repo-link)


# Hardware
- ILI9341 Display
- Lolin ESP32-S2 Mini
- DHT11 Sensor
- Neopixel LED (P9823)

***You can click on the image to visit the GitHub repository:***
  
![temp_humidity_micropython_lvgl]({static}/articles/temp_humidity_micropython_lvgl/photos/temp_humidity_micropython_lvgl.jpg)(https://github.com/fabse-hack/temp_humidity_micropython_lvgl)
  

# Project Description and github repo link  
In this project, I'll explain how I built a temperature and humidity display using MicroPython and LVGL.

- **Building the Firmware:**  
  I checked out lvgl-micropython from [lvgl-micropython](https://github.com/lvgl/lv_micropython) and built the binary file for the ESP32-S2 Mini with the ILI9341 display. I'm not sharing the exact make command because the code is still under development and there are ongoing changes.

- **Wiring the ESP32-S2 Mini to the ILI9341 and DHT11:**  
  Proper connections were made between the ESP32-S2 Mini and the ILI9341 display, as well as the DHT11 sensor. You can refer to the `main.py` for the pin definitions.

- **Using Squareline Studio:**  
  I downloaded [Squareline Studio](https://squareline.io/). Although it's not recommended by the lvgl_micropython developers due to compatibility issues with the generated code, I used it and customized the code to fit the lvgl_micropython bindings from kdschlosser.

- **Additional Features:**  
  - **German Time:** The `German_time` class handles synchronization with an NTP server, including summer and winter time adjustments, though I'm not yet 100% satisfied with the solution.
  - **MQTT:** The project includes MQTT functionality. If you use Home Assistant, you can send the temperature and humidity measurements via MQTT to your MySQL database.
  - **WiFi Connection:** The code attempts to connect to your defined SSID and password. If unsuccessful, it opens an access point.
  - **Error Exceptions:** I've implemented "try/except" blocks in several places to handle errors, timeouts, or OS errors, and log error messages in the MicroPython REPL.
  - **Automatic Y-Axis Range Adjustments:** The Y-axis range in both diagrams adjusts automatically.
  - **Automatic X-Axis Range:** The X-axis range in both diagrams updates automatically (one step per hour).


[so here is the link to the github repo](https://github.com/fabse-hack/temp_humidity_micropython_lvgl)  

