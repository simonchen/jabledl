import argparse


COWSAY = \
'''
  ____________
< I Love Jable >
  ------------
         \   ^__^
          \  (oo)\_______
             (__)\       )\\/\\
                 ||----w |
                 ||     ||

'''


HELP = \
'''Usage: jabledl [OPTION]... [URL]...

Download a video from jable.tv.

With no OPTION and URL, default is interactive mode.

Options:
    -h, --help  display this help and exit
    -i, --input input the URL, and change into non-interactive mode
    -f, --file HTML file, the file name will be as final video file name too.

Examples:
    jabledl
    jabledl -h
    jabledl -i https://jable.tv/videos/CAR-NUMBER/
\n
'''


def parse_args():
    print(COWSAY)

    parser = argparse.ArgumentParser(usage           = argparse.SUPPRESS,
                                     description     = HELP,
                                     add_help        = False,
                                     formatter_class = argparse.RawTextHelpFormatter)

    parser.add_argument('-h', '--help', action = 'help', help = argparse.SUPPRESS)
    parser.add_argument('-i', '--input', help = argparse.SUPPRESS)
    parser.add_argument('-f', '--file', help = argparse.SUPPRESS)
    args = parser.parse_args()

    if args.file : return args.file

    if args.input : print('Enter a Jable video url : ' + args.input) ; return args.input
    else          : return input('Enter a Jable video url : ')
