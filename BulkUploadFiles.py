# pip install pydrive
# issue with pydrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

google_auth = GoogleAuth()
drive_app = GoogleDrive(google_auth)

# Make sure the desired files are in the root directory
upload_list = ['test.png', 'test.jpg', 'test.csv']

for file_to_upload in upload_list:
    file = drive_app.CreateFile({'parents': [{'id': 'Folder ID from Google Drive'}]})
    # navigate to Google drive folder and get the ID from the URL
    file.SetContentFile(file_to_upload)
    file.Upload()
