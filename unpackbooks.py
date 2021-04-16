# -*-coding:Latin-1 -*
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      scolle
#
# Created:     21/10/2016
# Copyright:   (c) scolle 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, patoolib, shutil

srcPath = 'D:\\_DownLoads_\\Ripper'

#dstPath = 'D:\\_DownLoads_\\Ripper\\extracted' #SDcard
dstPath = 'F:\\SCo\\_books\\_ToAddInCalibre'
bkpPath = 'D:\\_DownLoads_\\Ripper\\extracted'

def main():
    for u in os.listdir(srcPath):
        if (u.endswith('.rar') or u.endswith('.zip')or u.endswith('.7z')):
            arcName = u.split(sep='.', maxsplit=1)[0]
            outDir= os.path.join(dstPath, arcName)
            if not os.path.exists(outDir):
                os.makedirs(outDir)
                patoolib.extract_archive(u,outdir= outDir,interactive=False)
                #os.rename(os.path.join(srcPath,u), os.path.join(bkpPath,u))
                shutil.move(os.path.join(srcPath,u), os.path.join(bkpPath,u))
            else :
                print (' /!\\ Warning : folder already exist : '+arcName)
    pass

if __name__ == '__main__':
    main()
