from PIL import Image
import glob,os,sys


# fromFile2thumbnails(fileDir = sys.path[0],format ='jpg',size = (128,128)').run()
class fromFile2thumbnails(object):
    def __init__(self, fileDir = sys.path[0], format ='jpg',size = (128,128)):
        self._fileDir = fileDir
        self._size = size
        self._format = format
        self._filePath = os.path.join(fileDir, '*.'+format)
        self._thumbPath = os.path.join(fileDir,'thumb')

    def run(self):
        if not os.path.exists(self._thumbPath):
            os.mkdir(self._thumbPath)
        for infile in glob.glob(self._filePath):
            ext = os.path.splitext(os.path.split(infile)[1])[0]
            fPath = os.path.join(self._thumbPath,ext)
            # print(file)
            im = Image.open(infile)
            # im.show()
            im.thumbnail(self._size)
            im.save(fPath+".t.jpg","JPEG")

        print('缩略图完成')


fromFile2thumbnails(r'D:\Users\y410p\img').run()