import logging
import re
import sys
from bs4 import BeautifulSoup
from queue import Queue
import urllib
from urllib import parse, request
from queue import PriorityQueue

logging.basicConfig(level=logging.DEBUG, filename='output.log', filemode='w')
visitlog = logging.getLogger('visited')
extractlog = logging.getLogger('extracted')


def parse_links(root, html):
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            text = link.string
            if not text:
                text = ''
            text = re.sub('\s+', ' ', text).strip()
            yield (parse.urljoin(root, link.get('href')), text)


def relevance(link):
    c = 0
    for i in link:
        c += 1
    page_rank = c
    return page_rank

def parse_links_sorted(root, html):
    # TODO: implement
    links = parse_links(root,html)
    priority = PriorityQueue()
    for i in links:
        priority.put((relevance(i[0]),i[0]))
    priority_list = []
    while not priority.empty():
        priority_list.append(priority.get()[1])
    return priority_list
    # return [root, html]


def get_links(url):
    #res = request.urlopen(url)
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    res = request.urlopen(req)
    # print(f'Normal: {list(parse_links(url, res.read()))}')
    # return list(parse_links(url, res.read()))
    # print(f"Priority: {parse_links_sorted(url, res.read())}")
    return (parse_links_sorted(url, res.read()))


def get_nonlocal_links(url):
    '''Get a list of links on the page specificed by the url,
    but only keep non-local links and non self-references.
    Return a list of (link, title) pairs, just like get_links()'''
    links = get_links(url)
    filtered = []
    return filtered


def crawl(root, wanted_content=[], within_domain=True):
    '''Crawl the url specified by `root`.
    `wanted_content` is a list of content types to crawl
    `within_domain` specifies whether the crawler should limit itself to the domain of `root`
    '''
    queue = Queue()
    queue.put(root)
    visited = []
    extracted = []
    root_domain = parse.urlparse(root).hostname
    domain_parts = root_domain.split('.')
    if domain_parts[0] == 'www':
        root_domain = '.'.join(domain_parts[1:])

    while not queue.empty():
        url = queue.get()
        try:
            req = request.urlopen(url)
            html = req.read()
            visited.append(url)
            visitlog.debug(url)

            for ex in extract_information(url, html):
                extracted.append(ex)
                extractlog.debug(ex)

            for link, title in parse_links(url, html):
                link_domain = parse.urlparse(link).hostname
                domain_parts = link_domain.split('.')
                if domain_parts[0] == 'www':
                    link_domain = '.'.join(domain_parts[1:])
                if within_domain and link_domain != root_domain:
                    continue
                queue.put(link)

        except Exception as e:
            print(e, url)
    return visited, extracted


def extract_information(address, html):
    '''Extract contact information from html, returning a list of (url, category, content) pairs,
    where category is one of PHONE, ADDRESS, EMAIL'''

    # TODO: implement
    results = []
    for match in re.findall('\d\d\d-\d\d\d-\d\d\d\d', str(html)):
        results.append((address, 'PHONE', match))
    for match in re.findall(r'\b\w+,\s\w+\s\d{5}\b', str(html)):
        results.append((address, 'ADDRESS', match))
    for match in re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(html)):
        results.append((address, 'EMAIL', match))
    return results


def writelines(filename, data):
    with open(filename, 'w') as fout:
        for d in data:
            print(d, file=fout)


def main():
    # site = sys.argv[1]
    site = 'https://www.cs.jhu.edu/~yarowsky/cs466.html'

    links = get_links(site)
    writelines('links.txt', links)

    nonlocal_links = get_nonlocal_links(site)
    writelines('nonlocal.txt', nonlocal_links)

    visited, extracted = crawl(site)
    writelines('visited.txt', visited)
    writelines('extracted.txt', extracted)


if __name__ == '__main__':
    main()