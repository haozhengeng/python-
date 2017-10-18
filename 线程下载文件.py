
import requests
import threading


class downloader(object):
    def __init__(self, url):
        self.url=url
        self.num=8
        self.name=self.url.split('/')[-1]
        r = requests.head(self.url)
        self.total = int(r.headers['Content-Length'])
        print('total is %s' % (self.total))

    def get_range(self):
        ranges=[]
        offset = int(self.total/self.num)
        for i in range(self.num):
            if i == self.num - 1:
                ranges.append((i*offset,''))
            else:
                ranges.append((i*offset,(i+1)*offset))
        return ranges

    def download(self,start,end):
        headers={'Range':'Bytes=%s-%s' % (start,end),'Accept-Encoding':'*'}
        res = requests.get(self.url,headers=headers)
        self.fd.seek(start)
        print(bytes.decode(res.content))
        self.fd.write(res.content.decode("utf-8"))

    def run(self):
        self.fd = open(self.name,'w')
        thread_list = []
        n = 0
        print(self.get_range())
        for ran in self.get_range():
            start,end = ran
            print('thread %d start:%s,end:%s'%(n,start,end))
            n+=1
            thread = threading.Thread(target=self.download,args=(start,end))
            thread.start()
            thread_list.append(thread)

        for i in thread_list:
            i.join()

        print('download %s load success'%(self.name))
        self.fd.close()

if __name__=='__main__':
    # down = downloader('http://192.168.147.128/test.txt')
    down = downloader('http://192.168.147.128/test.txt')
    down.run()

