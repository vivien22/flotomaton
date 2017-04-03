import os, datetime

def add_suffix(file_name_in, suffix):
    # extract file name without extension
    file_name_out  = '.'.join(file_name_in.split('.')[:-1])
    file_extension = file_name_in.split('.')[-1]
    # then add resized string
    file_name_out = file_name_out + "_" + suffix + "." + file_extension
    return file_name_out

def rename(file_path_in, file_path_out):
    os.rename(file_path_in, file_path_out)
    return file_path_out

def get_time():
    return datetime.datetime.now().strftime('%H:%M:%S')

def get_date():
    return datetime.datetime.now().strftime('%Y-%m-%d')

def add_time_suffix(file_name):
    return add_suffix(file_name, get_time())

def rename_with_time_suffix(file_name):
    return rename(file_name, add_time_suffix(file_name))

if __name__ == "__main__":

    image_name = 'photo_test.png'
    image_name = add_date_suffix(image_name)
    print(image_name)
