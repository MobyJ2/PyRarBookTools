import sys, os

ext2remove = ".rar"
#suffix2remove= ".part" #A implementer le retrait des .part1,.part10, ect...

def main():
    if len(sys.argv) > 1:
	#
        curArg = sys.argv[1]
        if os.path.isabs(curArg) and curArg[-len(ext2remove):] == ext2remove:
        	curArg = '.'.join(curArg.split('.')[:-1])

        fileName = os.path.basename(curArg)
        basename = fileName.split(sep='.',maxsplit=1)[0]

        if not os.path.exists(basename):
        	os.mkdir(basename)
        	os.chdir(basename)
        	imgPath  = basename+".jpg"
        	descPath = basename+".txt"
        	touch(imgPath)
        	touch(descPath)
        	print(" "*4+">>> SUCCESSFULLY CREATED.<<<")
        	os.chdir("..")
        else:
        	print("/!\\ the folder "+basename+" already exist. Do nothing.")
        	print(" "*4+" \\-> already exist. Do nothing.")
        	#os.system("PAUSE")
    else:
        print("No params in args...")
        #os.system("PAUSE")
    pass


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


if __name__ == '__main__':
    sys.argv = ["this.app",\
                "D:\\_todo\\_Temp\\TstFilename.part1.rar",\
				"D:\\_todo\\_Temp\\TstFilename.part2.rar",\
				"D:\\_todo\\_Temp\\TstFilename.bug.part1.rar"]
    main()
