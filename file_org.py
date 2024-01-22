import os 
import shutil
document_extensions = [
        "doc",
        "docx",
        "txt",
        "pdf",
        "rtf",
        "odt",
        "csv",
        "xlsx",
        "xls",
        "pptx",
        "ppt",
        "odp",
        "html",
]

video_extensions = [
        "mp4",
        "avi",
        "mkv",
        "mov",
        "wmv",
        "flv",
        "webm",
        "m4v",
        "mpeg",
        "mpg",
        "3gp",
        "3g2",
]

music_extensions = [
        "mp3",
        "wav",
        "ogg",
        "flac",
        "aac",
        "wma",
        "m4a",
        "alac",
        "aiff",
        "mid",
        "midi",
]

picture_extensions = [
        "jpg",
        "jpeg",
        "png",
        "gif",
        "bmp",
        "tiff",
        "webp",
        "svg",
        "ico",
        "jfif",
        "heif",
        "raw",
]

executable_extensions = [
        "exe",
        "dmg",
        "app",
        "apk",
        "msi",
        "bat",
        "sh",
]

try:
    os.mkdir("python files")
except:
    pass
try:
    os.mkdir("document")
except:
    pass
try:
    os.mkdir("video")
except:
    pass
try:
    os.mkdir("picture")
except:
    pass
try:
    os.mkdir("executable")
except:
    pass
try:
    os.mkdir("others")
except:
    pass

x = os.getcwd()
# print(x)
os.chdir(x)
file_list = os.listdir(x)
# print(file_list)
for n in file_list:
    if n != "file_org.py":

        extensions = n.split(".")[-1]
        # print(extensions)
        if extensions in document_extensions:
            try:
                shutil.move(x+ "\\"+ n, x+"\\"+"document"+"\\"+n)
            except:
                pass
        elif extensions in video_extensions:
            try:    
                shutil.move(x+ "\\"+ n, x+"\\"+"video"+"\\"+n)
            except:
                pass
        elif extensions in picture_extensions:
            try:
                shutil.move(x+ "\\"+ n, x+"\\"+"picture"+"\\"+n)
            except:
                pass
        elif extensions in executable_extensions:
            try:

                shutil.move(x+ "\\"+ n, x+"\\"+"executable"+"\\"+n)
            except:
                pass
        else:
            try:
                shutil.move(x+ "\\"+ n, x+"\\"+"others"+"\\"+n)
            except:
                print("lassi teri mkc")

