# jabledl

jabledl is a video downloader for Jable TV.

## Usage

the parameter -i (--input) is deprecated.
instead, you should use -f (--file) to feed the actual video HTML file (you need to manually save as HTML file from web browser)
```
jabledl -f "/tmp/jable-video.html"
````

## Dependency

jabledl depends on [FFmpeg](https://www.ffmpeg.org/) to convert MPEG2-TS file to MP4.
you have to make sure that ffmpeg is installed before you run jablel
for example on Ubuntu
```
sudo apt install ffmpeg
```

## Install

Clone this repository

```
$ git clone https://github.com/Yooootsuba/jabledl.git
```

Install jabledl

```
$ sudo python3 setup.py install
```

## Usage

Interactive mode

```
$ jabledl
```

Non-interactive mode

```
$ jabledl -i https://jable.tv/videos/CAR-NUMBER/
```

## License

MIT License
