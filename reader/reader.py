import requests
from PIL import Image
import cv2

def reader_png(url, path):
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r:
                f.write(chunk)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        cv2.imshow(path, img)
        cv2.waitKey(0)



def reader_jpg():
    print('Coming soon.')

def reader_pdf():
    print('Coming soon.')


if __name__ == '__main__':
    url = 'https://wmpics.pics/di-4X0Y.jpg'
    path = 'img.png'
    reader_png(url, path)
