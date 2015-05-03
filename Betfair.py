import requests
import lxml.html as htmlparser
from _elementtree import ElementTree


class MarathonScraper(object):
    """
    Class is used for scraping Marathon bookie
    First we get all of the links of event-more-view
    Then based on that link we collect all possible odd that can be founded on the site
    This class is based on xpath programing language and requests lib and fast LXML parser
    """
    '''
    Creating the private variables for using in the class
    __id is set of id for event - more -view represents list
    __live_url is url for marathon bookie which is contain live data for events
    __response represents response of marathon server
    _document represents object for parsing with lxml
    '''
    __id = []
    __open_market_url = 'https://www.marathonbet.com/hr/live.htm?openedMarkets='
    __live_url = 'https://www.marathonbet.com/hr/live.htm'
    _document = None
    _response = None

    def __init__(self):
        pass

    def fetch_data(self):
        try:
            self._response = requests.get(self.__live_url)
            self._document = htmlparser.fromstring(self._response.content)
        except IOError as requests_error:

            print requests_error.strerror

    def print_data(self):

        inp = open("Marathonbet.html", 'w+')
        inp.write(str(self._response.content))

    def get_the_id(self):

        div = self._document.xpath('//div[@id="container_EVENTS" and @class="live"]/div[@data-sport-treeid]')
        input_file = open("Marathonbet.html", 'w+')
        for i in div:
            if i.xpath('.//span[@class="nowrap" and contains(.,"Football")] '):
                temp = i.xpath('.//a[@class="event-more-view"]/@treeid')
                input_file.write(htmlparser.tostring(i))

        print temp
        return temp


def main():
    app = MarathonScraper()
    app.fetch_data()
    app.print_data()
    app.get_the_id()


if __name__ == '__main__':
    main()

















