## About our project

This is a primitive implementation of the Arduino catapult, with limited extensibility. Those who are in search for better code are advised elsewhere.

However, we are thrilled to share with all others some techniques to deploy OpenCV on a Raspberry Pi. It involves the following steps (works on gen 3 and newer RPIs):

1. Install Ubuntu Server for ARM64.
2. `sudo apt install xubuntu-desktop`. This is a prerequisite for OpenCV to work.
3. `sudo apt install build-essential pip3 python3-opencv`
4. `sudo pip3 install numpy`. Wait about an hour for your Pi to download and compile-install this package.

You are good to go after these steps. Ubuntu is highly preferable to Raspbian, as the former is better maintained. It however requires at least some knowledge on Unix commands.
