# ESP8266 [Single Core](#single-core) MicroController
## Event Sourcing & Object Oriented Design with MicroPython

## Prerequisite
  - [MicroPython](#install-micropython)
  - Visual Studio Code
  - PyMakr (VScode Extension)

### Install MicroPython

[Getting Started](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html)

[Firmware](https://micropython.org/download/ESP8266_GENERIC/)

[Firmware Source on GitHub](https://github.com/micropython/micropython/tree/master/ports/esp8266/boards/ESP8266_GENERIC)

```sh
$ pip install esptool
$ esptool.py --port /dev/ttyUSB0 erase_flash
$ esptool.py --port /dev/ttyUSB0 write_flash -fs 4MB -fm dout 0x0 ./ESP8266_GENERIC-20231005-v1.21.0.bin
```


## Use Case

For decades, Wake-On-LAN has been a reliable method for remotely activating devices by broadcasting a magic packet within a Local Area Network (LAN). However, its limitation to LAN networks poses a challenge. The objective is to extend this capability to Wide Area Networks (WAN) while maintaining a close-knit and secure environment.

### Goal

Developing an Object-Oriented Programming (OOP) and Event Handling system for a resource-constrained microcontroller demands a meticulous and efficient design. The objective is to strike a balance between resource optimization and code flexibility, ensuring adaptability for significant alterations or feature expansions in the future.

### Technical Description

At a high level, the microcontroller follows a design where it subscribes to an [MQTT](#mqtt) server and awaits messages upon establishing a WiFi connection. Each incoming `message` is encapsulated in an envelope containing a `type` and `payload`. The system selectively processes only recognized message types, treating others as NOOP (No Operation).

## Appendix

### MQTT
MQTT, which stands for Message Queuing Telemetry Transport, is a lightweight and open-source messaging protocol designed for small sensors and mobile devices with high-latency or unreliable networks. It was developed by IBM in the late 1990s and has since become a widely adopted standard in the field of the Internet of Things (IoT) and other scenarios where efficient and reliable communication is essential.

### Single Core
The ESP8266 is a single-core microcontroller, and it doesn't natively support multi-threading in the traditional sense of having multiple independent threads of execution running simultaneously. However, you can achieve a form of multitasking or concurrency by using cooperative multitasking or task scheduling.

## Hardware

#### Specs
|Technical Details||
|-|-|
|Firmware| MicroPython (custom installed)|
|Model|NodeMCU 12F|
|Processor|ESP8266 (Tensilica L106 32-bit RISC)|
|Clock Speed| 80MHz|
|Flash Memory| 4 MB|
|Data RAM|96kb|
|WiFi|802.11 b/g/n|
|Operating Voltage| 3.3V|
|USB to Serial Interface| [CH340G](https://static.efetividade.net/img/ch340g-datasheet-34852.pdf)|
|LxBxH |58 x 31 x 13 mm|

#### Sources
[Purchase](https://www.az-delivery.de/en/products/nodemcu-lolin-v3-modul-mit-esp8266?_pos=1&_sid=cca405331&_ss=r) (not sponserd)

[Quick Guide EBOOK](./NodeMCU_Lua_V3_Lolin_English.pdf)

[Datasheet](./NodeMCU_Lua_Lolin_V3_Modul_mit_ESP8266_12E_Datasheet.pdf)

[Pinout Diagram](./NodeMCU_Lua_Lolin_V3_Pinout_Diagram.pdf)

[Schematics](./NodeMCU_Lua_Lolin_V3_Schematics.pdf)
