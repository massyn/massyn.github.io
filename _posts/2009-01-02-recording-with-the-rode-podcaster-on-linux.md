---
layout: post
title:  Recording with the Rode Podcaster on Linux
author: "Phil Massyn"
categories: audio
tags: ["rode podcaster"]
image: podcaster.jpg
---

To record on the [Rode Podcaster](https://www.rode.com/microphones/podcaster) from Linux, simply follow these steps :

# Possibly Update Firmware
If your Podcaster has a serial number less than 7730, then you need to apply Rode's "Vista" [Firmware
Update](http://www.rodemic.com/downloads/podcaster/PodcasterUploader.exe) using Windows.  **Update 2021.11.14 - the download link is no longer valid - a newer file is available [here](https://www.rode.com/download/RODE_Firmware_Updater_Windows.zip).**

# Plug the device in
Once the microphone has been plugged in, you should see the entries on the linux logfile. Issue the dmesg
command to confirm.

## dmesg
```
[259364.405901] usb 1-1.3: USB disconnect, address 3
[263935.850793] usb 1-1.3: new full speed USB device using uhci_hcd and address 4
[263936.275739] usb 1-1.3: configuration #1 chosen from 1 choice
[263936.300492] ALSA /build/buildd/linux-ubuntu-modules-2.6.24-2.6.24/debian/build/build-server/sound/alsa-driver/[263936.310464] ALSA /build/buildd/linux-ubuntu-modules-2.6.24-2.6.24/debian/build/build-server/sound/alsa-driver/[263936.375667] input: RODE MICROPHONESj Rode Podcaster as /devices/pci0000:00/0000:00:1f.2/usb1/1-1/1-1.3/1-1.3:[263936.408705] input,hidraw0: USB HID v1.00 Device [RODE MICROPHONESj Rode Podcaster] on usb-0000:00:1f.2-1.3
```

# Get the card number
ALSA will detect the device, and assign it a card number.

## cat /proc/asound/cards

```
0 [PCI ]: Allegro - ESS Allegro PCI
ESS Allegro PCI at 0x1000, irq 5
1 [UART ]: MPU-401 UART - MPU-401 UART
MPU-401 UART at 0x300, irq 10
2 [Podcaster ]: USB-Audio - Rode Podcaster
RODE MICROPHONESj Rode Podcaster at usb-0000:00:1f.2-1.3, full speed
In this case, the Podcaster is assigned to card number 2.
```

## Turn up the volume

The microphone might be muted. Turn the volume up by issuing this command :

## amixer -c 2 set Mic 32

```
Simple mixer control 'Mic',0
Capabilities: cvolume pswitch pswitch-joined cswitch cswitch-joined
Playback channels: Mono
Capture channels: Mono
Limits: Capture 0 - 32
Mono: Playback [off] Capture 32 [100%] [23.04dB] [on]
```

Note that the -c 2 refers to the 2nd card (as we found in the `/proc/asound/cards` file)

# Record your audio
To record the audio, run the following command. Break it (CTRL-C) when you're done. (Note, that 2,0
refers to card 2, device 0)

## arecord -Dplughw:2,0 -f cd myself.wav

```
Recording WAVE 'myself.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo
Aborted by signal Interrupt...
```

or

## arecord -D hw:2,0 -f S24_3LE -r 48000 myself.wav
```
Recording WAVE 'myself.wav' : Signed 24 bit Little Endian in 3bytes, Rate 48000 Hz, Mono
^CAborted by signal Interrupt...
```

# FAQ

## I don't have permissions to record on the audio device
This can be solved with one of two methods. Add yourself to the audio group (in the example, phil is my
username)

`sudo addgroup phil audio`

The 2nd method is to change the permissions of the `/dev/dsp*` device.

`sudo chmod o=+rw /dev/dsp*`

