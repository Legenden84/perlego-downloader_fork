# Perlego PDF Downloader
Download books from Perlego.com in PDF format.

## Installation

Quick installation guide for **Windows** users:

Grab the download for the `installer.exe`  `file by pressing the download button located at the top right to download the exe & execute it

The command prompt that appears in the background is for diagnostic purposes and you shouldn't worry much about it (unless if you encounter an error)

The exe file was complied using `PyInstaller` and you can view the source code over at the installer folder

It is still strongly recommeneded to download Python 3.10.11 (at a maximum) and to follow the manual instructions after this

Install Python 3 and run:

  >$ pip3 install -r requirements.txt

## Configuration
Please watch the [demonstration video](https://youtu.be/X4msqCulOYk).

You'll need to find the *authToken*, *bookId* and *reCaptchaToken* analyzing the browser/websocket traffic and replace the constants in downloader.py.

## Run!
>$ python3 downloader.py

# Changes
I found some error due to different packages. Ive have pip freezed all of the packages i got this to work with. Also, add your token id's in the seperate token_list.py.

# DISCLAIMER:
The code is not intended for piracy or unlawful re-sharing purposes. You can only download the books you have purchased for the sole purpose of personal use. I do not take responsibility for illegal use of the software.
