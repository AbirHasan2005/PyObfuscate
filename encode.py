# (c) HTR-TECH@GitHub

import os
import sys
import zlib
import time
import base64
import marshal
import py_compile


class Colors(object):
    # Copied from https://github.com/AbirHasan2005/Image-Exif
    """Coloring Strings"""
    st = "\033[1;"  # Bold Style
    RED___ = f"{st}31;40m"
    GREEN_ = f"{st}32;40m"
    YELLOW = f"{st}33;40m"
    BLUE__ = f"{st}34;40m"
    PURPLE = f"{st}35;40m"
    CYAN__ = f"{st}36;40m"
    WHITE_ = f"{st}37;40m"


if sys.version_info[0] != 3:
    sys.exit("\n{}[{}-{}]{} Your Python Version is not Supported!".format(
        Colors.GREEN_,
        Colors.YELLOW,
        Colors.GREEN_,
        Colors.RED___
    ))


# Encoding
zlb = lambda in_: zlib.compress(in_)
b16 = lambda in_: base64.b16encode(in_)
b32 = lambda in_: base64.b32encode(in_)
b64 = lambda in_: base64.b64encode(in_)
mar = lambda in_: marshal.dumps(compile(in_,'<x>','exec'))

# Note at Top
note = """
##########################################
# !! This is Obfuscated Python Script !! #
#                                        #
#    AbirHasan2005/PyObfuscate@GitHub    #
##########################################


"""


def banner():
    """Program Banner"""
    print(f'{Colors.GREEN_}'
          ' ╔═════════════════════════════════╗\n'
          ' ║          PyObfuscate            ║\n'
          ' ║  Simple Python Code Obfuscator  ║\n'
          ' ║  Author: Tahmid Rayat           ║\n'
          ' ║  Github: HTR-TECH@GitHub        ║\n'
          ' ╚═════════════════════════════════╝\n')


def menu():
    """Program Menu"""
    __menu = f"""
{Colors.GREEN_} [{Colors.YELLOW}01{Colors.GREEN_}] Encode Marshal
{Colors.GREEN_} [{Colors.YELLOW}02{Colors.GREEN_}] Encode Zlib
{Colors.GREEN_} [{Colors.YELLOW}03{Colors.GREEN_}] Encode Base16
{Colors.GREEN_} [{Colors.YELLOW}04{Colors.GREEN_}] Encode Base32
{Colors.GREEN_} [{Colors.YELLOW}05{Colors.GREEN_}] Encode Base64
{Colors.GREEN_} [{Colors.YELLOW}06{Colors.GREEN_}] Encode Zlib, Base16
{Colors.GREEN_} [{Colors.YELLOW}07{Colors.GREEN_}] Encode Zlib, Base32
{Colors.GREEN_} [{Colors.YELLOW}08{Colors.GREEN_}] Encode Zlib, Base64
{Colors.GREEN_} [{Colors.YELLOW}09{Colors.GREEN_}] Encode Marshal, Zlib
{Colors.GREEN_} [{Colors.YELLOW}10{Colors.GREEN_}] Encode Marshal, Base16
{Colors.GREEN_} [{Colors.YELLOW}11{Colors.GREEN_}] Encode Marshal, Base32
{Colors.GREEN_} [{Colors.YELLOW}12{Colors.GREEN_}] Encode Marshal, Base64
{Colors.GREEN_} [{Colors.YELLOW}13{Colors.GREEN_}] Encode Marshal, Zlib, B16
{Colors.GREEN_} [{Colors.YELLOW}14{Colors.GREEN_}] Encode Marshal, Zlib, B32
{Colors.GREEN_} [{Colors.YELLOW}15{Colors.GREEN_}] Encode Marshal, Zlib, B64
{Colors.GREEN_} [{Colors.YELLOW}16{Colors.GREEN_}] {Colors.PURPLE}Special Encode
{Colors.GREEN_} [{Colors.YELLOW}17{Colors.GREEN_}] {Colors.RED___}Exit
"""
    print(__menu)


def datas(z):
    for x in ['Byte','KB','MB','GB']:
        if z < 1024.0:
            return "%3.1f %s" % (z, x)
        z /= 1024.0


class FileSize:
    """Gets the File Size"""
    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(f"{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}] Encoded File Size: %s\n" % datas(dts))


def encoder(option, data, output):
    """Encode Menu"""
    loop = int(input(f"{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}] Encode Count: {Colors.BLUE__}"))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit(f"\n{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}]{Colors.RED___} Invalid Option!")
    
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError: " + str(s))

    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()


def special_encoder(data, output):
    """Special Encode"""
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output, output)


def main_menu():
    try:
        print("\033c")
        banner()
        menu()
        try:
            option = int(input(f"{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}] Option: {Colors.BLUE__}"))
        except ValueError:
            sys.exit(f"\n{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}]{Colors.RED___} Invalid Option!")
        
        if option > 0 and option <= 17:
            if option == 17:
                sys.exit(f"\n{Colors.GREEN_} Exiting ...")
            print("\033c")
            banner()
        else:
            sys.exit(f'\n{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}]{Colors.RED___} Invalid Option!')
        try:
            file = str(input(f"{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}] File Path: {Colors.BLUE__}"))
            data = open(file).read()
        except IOError:
            sys.exit(f"\n{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}]{Colors.RED___} File Not Found!")
        new_file_name = str(input(f"{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}] ({Colors.CYAN__}Optional{Colors.GREEN_}) New File Name: {Colors.BLUE__}"))
        output = new_file_name if new_file_name else file.lower().replace('.py', '') + '_encrypted.py'
        if option == 16:
            special_encoder(data, output)
        else:
            encoder(option, data, output)
        print(f"\n{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}] Successfully Encrypted %s" % file)
        print(f"{Colors.GREEN_} [{Colors.YELLOW}-{Colors.GREEN_}] Saved as %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()


if __name__ == "__main__":
    main_menu()
