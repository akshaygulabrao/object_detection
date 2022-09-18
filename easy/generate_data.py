import csv
import cv2
import numpy as np

img = np.ones((512,512))
rect = np.random.randint(0,412,(2,2))

with open('easy.csv','w+') as csvfile:
    fieldnames = ['fname','xmin','xmax','ymin','ymax','classid']
    writer = csv.DictWriter(f=csvfile, fieldnames=fieldnames,)
    writer.writeheader()
    for x, y in rect:
        height = 100
        img[x:x + height, y:y + height] = height
        writer.writerow({'fname': 'easy.jpg', 'xmin':x, 'xmax': x + height,
                         'ymin': y, 'ymax': y + height, 'classid':1})
cv2.imwrite('easy.jpg',img)



