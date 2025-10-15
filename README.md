# TelegramBotIPUpdate

## The Problem
Im using OpenVPN on a Raspi to get to my Homenetwork. However, once in a while my public IP changes, and i cant do anything about it (my provider doesnt have a static Option).
As long with the changing IP Adress, i also loose access to my home network. This doesnt even happen regulary, it happens completly at random and usually when i need my home network the most.

## The Solution
A programm on my VPN Raspi, that checks daily wether my IP changed or not. If it did, it tells a Telegram Bot to send me a message with the new IP. This way, ican easily change it wherever i am.

## How it works
One Programm will visit "whatsmyip.com" and will retrieve the current IP. It will then check wether theres a .txt file with a IP, if not, it will make one and send a message. If a file with IP exists, it will compare the IPs, and if they differ, it will overwrite the IP and send a message via Telegram.
