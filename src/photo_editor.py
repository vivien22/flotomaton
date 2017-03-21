import os

def resize(image_in, size):   
    # extract file name without extension
    image_out = '.'.join(image_in.split('.')[:-1])
    # then add resized string
    image_out = image_out + "_resized.jpg"
    os.system("convert " + image_in + " -resize " + str(size) + "@ " + image_out)
    return image_out

def montage(image_1, image_2, image_3, image_4, photo_montage_name):
    os.system("montage " + 
              resize(image_1, 640*480) + " " + 
              resize(image_2, 640*480) + " " + 
              resize(image_3, 640*480) + " " + 
              resize(image_4, 640*480) + 
              " -tile 2x2 -geometry +10+10 " + 
              photo_montage_name)

if __name__ == "__main__":
    montage('/home/pi/flotomaton/capt0000.jpg',
            '/home/pi/flotomaton/capt0001.jpg',
            '/home/pi/flotomaton/capt0002.jpg',
            '/home/pi/flotomaton/capt0003.jpg',
            '../montage.jpg')
