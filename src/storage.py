import datetime, os, shutil

class init(object):
  
    def __init__(self, directory):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def store(self, file_path):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        target_fir = os.path.join(self.directory, date)
        if not os.path.exists(target_fir):
            os.makedirs(target_fir)

        shutil.move(file_path, target_fir)

        return os.path.join(target_fir, os.path.basename(file_path))
