import zipfile
from multiprocessing import Pool
import time
import os


def InitAttack(options):
    pool = Pool(processes=(options.cores))

    process = pool.map(IterArgs, [options])


def IterArgs(opt):
    ExecAttack(opt)


def ExecAttack(options):
    with open(options.dictfile) as f:
        passwords = f.read().split("\n")

    if os.path.isfile(options.zipfile):
        z = zipfile.ZipFile(options.zipfile)

        for p in passwords:
            at = p.encode(encoding="UTF-8")
            z.extractall(path=options.zipfile + "_cracked", pwd=at)
    else:
        print("Can't find zip file :(")
        exit()
