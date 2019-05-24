from scrapy.extensions.httpcache import FilesystemCacheStorage
from scrapy.spiderloader import SpiderLoader
from scrapy.utils.project import get_project_settings


SETTINGS = get_project_settings()
STORAGE = FilesystemCacheStorage(SETTINGS)
SPIDER_LOADER = SpiderLoader.from_settings(SETTINGS)
SPIDER_CLASS = SPIDER_LOADER.load('ksdata')
SPIDER = SPIDER_CLASS(file='../sample.csv')

def get_busted_caches():
    for request in SPIDER.start_requests():
        meta = STORAGE._read_meta(SPIDER, request)
        if meta['status'] in SETTINGS['HTTPCACHE_IGNORE_HTTP_CODES']:
            yield STORAGE._get_request_path(SPIDER, request)

if __name__ == "__main__":
    import shutil

    for path in get_busted_caches():
        shutil.rmtree(path)
