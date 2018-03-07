# coding=utf-8
import requests


import os
import time
import platform
import atexit

# global variable for exit function

class Monitor(object):

    def __init__(self, type = "server"):
        self.fileNumber = 0
        atexit.register(self.exit)
        self.original = ""
        self.destnation = ""
        self.type = type

        self.monitor()

    # print the number of files uplaod in this time, and give a reminder for user that the
    # the file will be deleted after Monday before exit the script.
    # '''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
    # def TimeStampToTime(timestamp):
    #     timeStruct = time.localtime(timestamp)
    #     print(timeStruct.tm_year)
    #     return time.strftime('%Y-%m-%d',timeStruct)


    # def get_FileCreateTime(filePath):
    #     # filePath = unicode(filePath,'utf8')
    #     t = os.path.getctime(filePath)
    #     return TimeStampToTime(t)

    def monitor(self):
        atexit.register(exit)
        if 'windows' in platform.platform().lower():  # windows 系统使用gbk编码
            self.original = os.getcwd()  # 返回当前目录
        else:
            self.original = os.getcwd()  # 返回当前目录

        print(self.original)

        if (self.type != "server"):
            # to check whether the complete upload folder is created or not.
            if os.path.isdir('Uploaded'):
                createTime = self.get_FileCreateTime(self.original + "/Uploaded")
                # currentTime = time.str
                print("2018-03-09" > createTime)
            else:
                os.mkdir('Uploaded')
            self.destnation = self.original + "/Uploaded"

        # if the type is server, we need to get the directory of unclassify file
        else:
            self.original = self.original + "/sample/web/static/upload/unclassify"
            self.destnation = self.original + "/sample/web/static/upload/classify"


        allfile = os.listdir(self.original)
        print('Current Files:', allfile)
        while 1:
            newfile = os.listdir(self.original)
            print("Changes Found")
            time.sleep(15)

            if allfile != newfile:
                print("Changes Found")
                self.upLoadAndMoveFile(allfile, newfile, self.original)
                # print('Current Files:', newfile)
                time.sleep(15)
                # allfile = newfile

    def upload(self, fileName):
        url = "http://129.161.74.122:5000/auto_upload"
        file = open(fileName, 'rb')
        files = {'file': file}
        response = requests.post(url, files=files)
        file.close()
        global FILENUMBER
        FILENUMBER += 1
        # print(response.status_code)
        # print(response.request.body)

    def move(self, fileName, path):
        file = open(fileName, 'rb')
        # print("in auto upload, the type is ",type(file))
        os.rename(path + '/' + fileName, path + "/UpLoaded/" + fileName)
        file.close()
        # os.remove(fileName)

    def upLoadAndMoveFile(self, allfile, newfill, path):
        for new in newfill:
            newFileFlag = True
            for all in allfile:
                if new == all:
                    newFileFlag = False
                    break
            if newFileFlag:
                self.upload(new)
                self.move(new, path)

    def exit(self):
        print("You have upload {:d}".format(self.fileNumber))
        print("Please reminder the file will be deleted when you open this file next time.")


if __name__ == '__main__':

    monitor = Monitor()


