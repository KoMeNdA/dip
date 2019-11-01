#!/bin/bash
#
echo "Start test:"
#создание виртальной машины 

sudo virt-install \
 --virt-type=kvm \
  --name slinux6 \
  --memory 1024 \
  --vcpus 1 \
  --os-variant=rhel7\
  --hvm \
  --cdrom /home/admin/Документы/virt/SL-7.2-DVD-x86_64-2016-02-02.iso\
  --network network=default,model=virtio \
  --graphics vnc,port=5906\
  --disk path=/var/lib/libvirt/images/slinux6.img,size=8,bus=virtio\
  --noautoconsole
#virsh start slinux5
#установка
vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin1.png
sleep 300 
vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin2.png 
vncdo -s localhost::5906 move 500 660 click 1 type "rus" pause 30 move 500 230 click 1 move 950 750 click 1 capture /home/admin/Документы/scrin/scrin3.png

sleep 120
vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin4.png

vncdo -s localhost::5906 move 1015 600 click 1 capture /home/admin/Документы/scrin/scrin5.png

sleep 3
vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin6.png

vncdo -s localhost::5906 move 450 550 click 1

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin7.png

vncdo -s localhost::5906 move 45 45 click 1

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin8.png

sleep 30
vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin9.png

vncdo -s localhost::5906 move 950 720 click 1

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin10.png

sleep 10

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin11.png

vncdo -s localhost::5906 move 250 180 click 1

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin12.png


sleep 10

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin13.png

vncdo -s localhost::5906 key shift-alt
vncdo -s localhost::5906 move 500 110 click 1 type "root"
vncdo -s localhost::5906 move 500 190 click 1 type "root"

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin14.png

vncdo -s localhost::5906 move 45 45 click 1 pause 3 click 1

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin15.png


sleep 3600 

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin16.png

vncdo -s localhost::5906 move 900 660 click 1
 
vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin17.png


sleep 600

virsh start slinux6

sleep 60

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin18.png

vncdo -s localhost::5906 move 400 320 click 1
vncdo -s localhost::5906 key shift-alt

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin19.png

sleep 5

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin20.png

vncdo -s localhost::5906 move 400 140 click 1 type "admin"

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin21.png

vncdo -s localhost::5906 move 365 275 click 1

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin22.png

vncdo -s localhost::5906 move 45 80 click 1
 
vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin23.png

vncdo -s localhost::5906 move 1000 750 click 1

vncdo -s localhost::5906 capture /home/admin/Документы/scrin/scrin24.png

