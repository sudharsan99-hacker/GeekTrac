import requests
from bs4 import BeautifulSoup
from lxml import etree

from codechef.db import save_stat, user_to_platform_uname

platform = 'codechef'
#base_url = 'https://www.codechef.com'
base_url = 'https://www.codechef.com/users/'

bsformat = 'html.parser'


def scrap_now(user):
    if not user:
        return {}

    p_uname = user_to_platform_uname(user)
    if not p_uname:
        return {}
    
    if not p_uname:
        return dict()
    
    query_url = base_url + p_uname

    page = requests.get(query_url)
    soup = BeautifulSoup(page.text, bsformat)
    dom = etree.HTML(str(soup))

    username = dom.xpath('/html/body/main/div/div/div/div/div/section[1]/ul/li[1]/span/span[2]')
    if not username or len(username) != 1:
        return {
            'error': 'username not found'
        }
    uname = dom.xpath('/html/body/main/div/div/div/div/div/header/h1')
    if not uname or len(uname) != 1:
        return {
            'error': 'username not found'
        }

    userattrs = dict()
    userattrs['username'] = username[0].text
    userattrs['rating'] = rating(dom)
    userattrs['stars'] = stars(dom)
    userattrs['rank'] = rank(dom)
    userattrs['contest_count'] = contest_count(dom)
    userattrs['contests'] = get_contests(dom)

    save_stat(p_uname, userattrs)

    return userattrs


def rating(dom):
    rating = dom.xpath('/html/body/main/div/div/div/aside/div[1]/div/div[1]/div[1]')
    rating = rating[0].text

    return rating

def stars(dom):
    stars = dom.xpath('/html/body/main/div/div/div/aside/div[1]/div/div[1]/div[3]')
    stars = len(stars[0].getchildren())
    return stars

def rank(dom):
    global_rank = dom.xpath('/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[1]/a/strong')
    country_rank = dom.xpath('/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[2]/a/strong')
    
    return {
        'global_rank': global_rank[0].text,
        'country_rank': country_rank[0].text,
    }

def contest_count(dom):
    nctst = dom.xpath('/html/body/main/div/div/div/div/div/section[3]/div[1]/div/b')
    return nctst[0].text

def get_contests(dom):
    contests = dom.xpath('/html/body/main/div/div/div/div/div/section[6]')
    contests = list(filter(lambda x: x.tag == 'div', contests[0]))
    
    def get_contest_detail(contest):
        title = contest.getchildren()[0].getchildren()[0].text.strip()
        problems = contest.getchildren()[1].getchildren()[0].getchildren()
        
        def get_problem_detail(problem):
            return problem.text
        
        return {
            'title': title,
            'problems': list(map(get_problem_detail, problems)),
        }

    return list(map(get_contest_detail, contests))