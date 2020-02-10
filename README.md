# switch_connect NODE



## Package

---

### 	1) ioutil

- Serial Input / Output 
- Serial Process

### 	2) manages

- Ros Manager
- Data Conversion (packet -> topic)



## PORT 설정

---

~~~ 
$ cd /etc/udev/rules.d
$ sudo vi leonardo.rules
(아래 복사)
SUBSYSTEMS=="usb", KERNEL=="ttyACM[0-9]*", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="8036", MODE="0666", SYMLINK+="leonardo"

(usb 재 연결 후 확인)
$ ls -l /dev/leonardo 
~~~









