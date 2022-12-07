import scraper_helper as sh
BOT_NAME = 'amazonScrapy'

SPIDER_MODULES = ['amazonScrapy.spiders']
NEWSPIDER_MODULE = 'amazonScrapy.spiders'
ROBOTSTXT_OBEY = False
AUTOTHROTTLE_ENABLED = True

DEFAULT_REQUEST_HEADERS = sh.get_dict(
    '''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: es-ES,es;q=0.9
cache-control: max-age=0
cookie: session-id=139-2249452-2467929; session-id-time=2082787201l; i18n-prefs=USD; lc-main=es_US; sp-cdn="L5Z9:BO"; csm-hit=tb:s-YAMGN50X7SS0FFNA9BK4|1670426557621&t:1670426558280&adb:adblk_no; ubid-main=133-4464731-7021356; session-token="69/zxuOiDvFdg8cgR8AlnUdIT+qHErkFOFjxwH1kxaoJpawg7mEPGpjyOaLJlPACu06zVigiDhp5J9qgtG5mIl1UW0q0d/NVh5TESZGzvDZJPq76vmaOcWXiEnbXUptD93L/k+VKqykBQ0NH4qA12WQWLZj8zlTyhv3A9XcvY5TP30Bc7KPOVJRTCNjtLr1xrHFWgr2XhmFlRQHZNKn1pCSj6cxxm6sZpaHVUaj3OF4="
device-memory: 8
downlink: 3.35
dpr: 1.25
ect: 4g
rtt: 150
sec-ch-device-memory: 8
sec-ch-dpr: 1.25
sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-ch-viewport-width: 1024
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
'''
)


REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
