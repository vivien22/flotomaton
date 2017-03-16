import os

def montage(image_1, image_2, image_3, image_4, photo_montage_name):
    #os.system("montage *.jpg -tile 2x2 -geometry +10+10 montage.jpg")
    os.system("montage " + image_1 + " " + image_2 + " " + image_3 + " " + image_4 + " -tile 2x2 -geometry +10+10 " + photo_montage_name)
