#!/usr/bin/python




import subprocess 
#from vncdotool import api

subprocess.call(["virt-install --virt-type=kvm --name slinux7 --memory 1024 --vcpus 1 --os-variant=rhel7 --cdrom /tmp/SL-7.2-DVD-x86_64-2016-02-02.iso --network network=default,model=virtio --graphics vnc,port=5907 --disk path=/var/lib/libvirt/images/slinux7.img,size=8,bus=virtio"])

# client = api.connect('localhost::5906', password=None)
