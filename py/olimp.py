import cv2

class Image:
    def __init__(self, w, h):
        self.im = []
        for i in range(0,h):
            line = [0 for i in range(0,w)]
            self.im.append(line)

    def compare(self, secondIm, cmpMat):
        d = []
        for i in range(0, len(self.im)):
            cmpLine = []
            for j in range(0, len(self.im[i])):
                cmpLine.append(cmpMat[self.im[i][j]][secondIm.im[i][j]])
            d.append(cmpLine)
        for i in self.im: print(i)
        print('+'*15)
        for i in secondIm.im: print(i)
        print('+'*15)
        for i in d: print(i)

wnh = raw_input()
wnh = wnh.split(' ')
w = int(wnh[0])
h = int(wnh[1])
im = Image(w, h)
im2 = Image(w, h)
for i in range(0,h):
    im.im[i] = [int(j) for j in raw_input()]
for i in range(0,h):
    im2.im[i] = [int(j) for j in raw_input()]
cmpr = [int(i) for i in raw_input()]
cmpMat = [cmpr[0:2], cmpr[2:4]]
im.compare(im2, cmpMat)
