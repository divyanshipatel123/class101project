import dropbox
import os

class TransferData():
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(root,fileName)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open (local_path,'rb') as f:
                    dbx.files_upload(f.read() , dropbox_path , mode = dropbox.files.WriteMode.overwrite)

def main():
    access_token = 'sl.BBpVzfI2KCv9GICm8ar4ogZ5kLgZgWVCUVCOwIcj1VguRkYk3_2ob4MpXtssG6nkoFyAV1IpOudZfD9zpFYbj5apFNJNqZIm_pu-FziMoMvCyPVqIKkxuvb-tDTqxKJxljzTEVNHTXNX'
    transferData = TransferData(access_token)

    file_from = input('Enter Folder path to be uploaded : ')
    file_to = '/test/' 

    transferData.upload_files(file_from, file_to)
    print("file has been uploaded successfully!!")


main()
