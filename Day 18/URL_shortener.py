class URL_shortener:
    url_dict = {}
    base_url = "http://short.url/"

    def add_url(self, original_url):
        if original_url not in self.url_dict:
            l1 = len(self.url_dict)
            self.url_dict[original_url] = self.base_url + str(l1 + 1)
            return self.url_dict[original_url]
        else:
            print("URL already exists")
            return self.url_dict[original_url]

    def view_urls(self):
        print("__________________________________________________________________")
        # print(self.url_dict)
        for i in self.url_dict:
            print(f"\'{i}\': \'{self.url_dict[i]}\'")
        print("------------------------------------------------------------------")


if __name__ == '__main__':

    url = URL_shortener()
    url1 = url.add_url('https://www.example.com')
    url.view_urls()
    url2 = url.add_url('https://www.python.com')
    url.view_urls()
    url3 = url.add_url('https://www.pandas.com')
    url.view_urls()

    print(url.add_url('https://www.example.com'))
