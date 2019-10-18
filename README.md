# UploadToDropboxAndRemoveFromRaspberryPi
 This script uploads image files to dropbox and removes them from raspberry pi

## Prereq

This python script requires dropbox uploader bash.

See the following:

https://github.com/andreafabrizi/Dropbox-Uploader

## Info

I have webcams that can detect motion and send the image to an FTP server.

I've setup the raspberry pi as an FTP server (within my network only. It is not exposed to internet)

A cron job runs the script every minute to look for new files and upload to dropbox

## Cron setup

I setup the following in crontab

```
crontab -e
```

```
* * * * * python /home/userfolder/FTP_folder/manage_files.py
```