import urllib2

class TiebaScrap():
    def __init__(self, baseURL, seeLZ):
        self.baseURL = baseURL
        self.seeLZ = '?seeLZ=' + str(seeLZ)
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        self.header = {'User-Agent': self.user_agent}

    def getPage(self, PageNum):
        try:
            URL = self.baseURL + self.seeLZ + '?pn=' + str(PageNum)
            request = urllib2.Request(URL, headers=self.header)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                print 'Error is ' , e.reason
                return None


baseURL = 'https://tieba.baidu.com/p/3703578145'
tieba_test = TiebaScrap(baseURL, 1)
tieba_test.getPage(1)