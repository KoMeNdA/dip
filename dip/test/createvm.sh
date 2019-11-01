#!/bin/bash
#
read name_vm
read way_vm
read port_vm
echo "Start test:"
#создание виртальной машины 

sudo virt-install \
 --virt-type=kvm \
  --name $name_vm \
  --memory 1024 \
  --vcpus 1 \
  --os-variant=rhel7\
  --hvm \
  --cdrom $way_vm\
  --network network=default,model=virtio \
  --graphics vnc,port=$port_vm\
  --disk path=/var/lib/libvirt/images/slinux7.img,size=8,bus=virtio\
  --noautoconsole

