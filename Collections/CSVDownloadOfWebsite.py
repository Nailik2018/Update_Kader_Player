# -*- coding: utf-8 -*-
import urllib3

class CSVDownloadOFWebsite():

    def __init__(self, url):
        self.url = url

    def download(self):
        http = urllib3.PoolManager()
        request = http.request('GET', self.url)
        if request.status == 200:
            data = request.data
            return data
        else:
            exit("Der Requeststatus hat den Status" + str(request.status) + " und wurde abgebrochen!")
