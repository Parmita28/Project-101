class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        for root, dirs, files in os.walk(file_from):
         dbx = dropbox.Dropbox(self.access_token)
         relative_path=os.path.relpath(local_path, file_from)
         dropbox_path=os.path.join(file_to, relative-path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BEumgCz06Q5nDGg8hQgeOCOmG8NsNku35YMiwV8y_LKAToveVxTC_8mMPiHXmKpHnBn1aB0ps7eTp8A2fP3B8OPopgQYq5FTW02MphjzZGqwScKm5yNhfDnRkO3NL7uv4XmKffc'
    transferData = TransferData(access_token)

    file_from = input("Enter The File Path to transfer:")
    file_to = input("Enter The Full Path to upload into Dropbox:")

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()            