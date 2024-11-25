ol='-'*30
job2=dict()
job22=dict()
job3=dict()
line = ['May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated']
line.append('May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.')
line.append('May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...')
line.append('May 20 11:01:12 PC-00102 PackageKit: daemon start')
line.append('May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...')
line.append('May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00')
line.append('May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"')
line.append('May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device')
line.append('May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio')
line.append('May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.')
line.append('May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.')
out=input('Input number line: ')
j_date_M,j_date_D,j_date_time,j_hostname,j_service,*j_msg=line[int(out)].split()
liter1=['May 26 12:48:18','ideapad','systemd[1]','Finished Message of the Day.']
keys1=['time','pc_name','service_name','message']
key1,key2,key3,key4=keys1
job2[key1]=''.join(j_date_D+' '+j_date_M+' '+j_date_time)
job2[key2],job2[key3],job2[key4]=j_hostname,str(j_service)[:-1],' '.join(j_msg)
job22[j_hostname]=' '.join(j_msg)
job3=dict(zip(keys1,liter1))
job4=[job2,job3]
job5=[set(job2.values())&set(job3.values())]
print(end='\n')
print(f"{ol}job-2{ol}")
print(job2, end='\n\n')
print(f"{ol}job-22{ol}")
print(job22, end='\n\n')
print(f"{ol}job-3{ol}")
print(job3, end='\n\n')
print(f"{ol}job-4{ol}")
print(job4, end='\n\n')
print(f"{ol}job-5{ol}")
print(job5)
#
