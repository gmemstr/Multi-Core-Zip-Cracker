import zipfile
import multiprocessing
from multiprocessing import Pool
import ctypes
import time
import os
isCracked = False
CoreUsing = 0


def CrackZipFile(password2):
    zipfilename = 'zip.zip'

    dictionary = 'dictionary.txt'


    password = password2

    zip_file = zipfile.ZipFile("zip.zip")

    try:

        zip_file.extractall(pwd=password)


        password = 'Password found: %s' % password

        print("Password Cracked : " + password)

    except:

        pass



def main():
    global isCracked

    global CoreUsing

    num_cores = multiprocessing.cpu_count()

    isCracked = False

    CoreUsing = 0

    start_time = time.time()

    print('Core number : ' + str(num_cores))

    with open("passwords.txt", 'r') as f:

        passwordlist = f.read().split("\n")

    pool = Pool(processes=(num_cores - 2))


    k = pool.map(CrackZipFile, passwordlist)

if __name__ == '__main__':
    main()
