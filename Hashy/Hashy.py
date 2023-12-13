#!/usr/bin/python
# -- coding: utf-8 --

try:
    import os,sys,requests,argparse
    from huepy import *
except:
      print('''\033[91m
        +-----------------------------------------------------+
        |                * Missing Modules *                |
        +-----------------------------------------------------+
        | requests, sys, os, argparse and huepy are required. |
        |      Check if any one of them are missing.          |
        |    try --> pip install -r requirements.txt          |
        +-----------------------------------------------------+
     ''')
      exit()
    
os.system('cls')

parser = argparse.ArgumentParser()
parser.add_argument('-p', help='Hash which needs to be decoded.', dest='passw')
args = parser.parse_args()

print(green(''' 
 _     _ ___ ___ _     _ _   _
 |__| |_| |__ |_|   \/  
 |     | |     | __| |     |    |    \n'''))

if not len(sys.argv) > 1:
    hashvalue = input(info("Enter your hash.\n> "))
else:
    hashvalue = args.passw

if len(hashvalue) == 32:
    print (info('Hash Function : MD5'))
    hashtype = 'md5'
elif len(hashvalue) == 40:
    print (info('Hash Function : SHA-1'))
    hashtype = 'sha1'
elif len(hashvalue) == 64:
    print (info('Hash Function : SHA-256'))
    hashtype = 'sha256'
elif len(hashvalue) == 96:
    print (info('Hash Function : SHA-384'))
    hashtype = 'sha384'
elif len(hashvalue) == 128:
    print (info('Hash Function : SHA-512'))
    hashtype = 'sha512'
else:
    print (bad('Unidentified Hash Function!'))
    exit(1)

	
def md5crack(hashvalue):
	r = requests.get('http://www.nitrxgen.net/md5db/' + hashvalue).text
	print(good('Password is >>> ' + green(r)))
	
def decrypter(hashvalue, hashtype):
    r = requests.get(
        'https://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=cybercroc@protonmail.com&code=c5ddc9bbd5b07c45' % (hashvalue, hashtype)).text
    if len(r) != 0:
        print(good('Password is >>> ' + green(r)))
    else:
        print(bad('Hash was not found in the database.'))
        return False

if hashtype == 'sha1' or 'sha256' or 'sha384' or 'sha512':
    decrypter(hashvalue, hashtype)
elif hashtype == 'md5':
	md5crack()
else:
    exit()