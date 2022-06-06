#!/usr/bin/bash

set -x #echo on

sshfs -o cache=yes -o kernel_cache -o compression=no -o ciphers=aes256-gcm@openssh.com -o reconnect pi@192.168.1.10:/media/pi/4Tb/smb/torrents ~/sshfs/torrents
sshfs -o cache=yes -o kernel_cache -o compression=no -o ciphers=aes256-gcm@openssh.com -o reconnect pi@192.168.1.10:/media/pi/4Tb/smb/share ~/sshfs/share
sshfs -o cache=yes -o kernel_cache -o compression=no -o ciphers=aes256-gcm@openssh.com -o reconnect pi@192.168.1.10:/media/pi/4Tb/smb/Music  ~/sshfs/Music
#sshfs -o cache=yes -o kernel_cache -o compression=no -o ciphers=aes256-gcm@openssh.com -o reconnect pi@192.168.1.10:/media/pi/4Tb/backup  ~/sshfs/backup
#sshfs -o cache=yes -o kernel_cache -o compression=no -o ciphers=aes256-gcm@openssh.com -o reconnect pi@192.168.1.10:/media/pi/4Tb/Photos  ~/sshfs/Photos
