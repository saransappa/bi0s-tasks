## Tools

### Jsteg

#### Introduction

Jsteg is a package for hiding data inside jpeg files, a technique known as [steganography](https://en.wikipedia.org/wiki/Steganography). This is accomplished by copying each bit of the data into the least-significant bits of the image. The amount of data that can be hidden depends on the filesize of the jpeg; it takes about 10-14 bytes of jpeg to store each byte of the hidden data.

#### Installation

```
$ sudo wget -O /usr/bin/jsteg https://github.com/lukechampine/jsteg/releases/download/v0.1.0/jsteg-linux-amd64
$ sudo chmod +x /usr/bin/jsteg
$ sudo wget -O /usr/bin/slink https://github.com/lukechampine/jsteg/releases/download/v0.2.0/slink-linux-amd64
$ chmod +x /usr/bin/slink
```

#### Usage

Jsteg tool can be initialised by typing the following command.
```
$ jsteg
```

![Image can't be displayed. Just try typing the above command.](./jsteg.png)

##### Hiding data

Now, lets hide some data using jsteg.
Consider this image of Itachi.

![https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj-wobOlrjhAhXZ8XMBHVwlAyYQjRx6BAgBEAU&url=https%3A%2F%2Fwww.zerochan.net%2F2081648&psig=AOvVaw34K4eMPvnU2fDNf8d2-Iif&ust=1554526995244453](./Itachi.jpg)

Let the name of file to be embedded be 'jsteg.txt'.

The file to be embedded contains the following data.

![Jsteg is used for JPEG steganaography.](./jsteg_txt.png)

Commands to embed a file in the JPEG image is as follows.
```
$ jsteg hide <in.jpg> <secret file name> <out.jpg>
```

![Sorry, image can't be displayed.](./Embed_syntax.png)

Now, the image looks like this.

![Sorry, image can't be displayed.](./Itachi_embedded.jpg)

##### Revealing data

The syntax for revealing data is as follows.
```
$ jsteg reveal <in.jpg> <output file name>
```

![Sorry, image can't be displayed.](./Reveal_syntax.png)

#### Reference

For further reference , click [here](https://godoc.org/github.com/lukechampine/jsteg).
