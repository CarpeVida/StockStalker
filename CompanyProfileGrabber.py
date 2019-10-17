import html
import requests
from bs4 import BeautifulSoup

def boolify(s):
    if s == 'True':
        return True
    if s == 'False':
        return False
    raise ValueError("huh?")

def autoconvert(s):
    for fn in (boolify, int, float):
        try:
            return fn(s)
        except ValueError:
            pass
    return s


def extract_key(key, json_text):
    m = re.search(r"\"%s\":[\"]?([^\"\{\}]+)[\"]?" % (key,), json_text)
    if m:
        # Ugly, yes.
        return autoconvert(html.unescape(m.group(1)).replace("\\u002F", "/").strip(","))
    else:
        return None


def company_info(symbol):
    """
        Fetch info from yahoo finance for a company.
    """
    page = requests.get(f"https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}")
    soup = BeautifulSoup(page.content, 'html.parser')
    script = soup.find("script", text=re.compile("address1"))
    json_text = script.text
    key_set = ['website',
               'address1',
               'address2',
               'city'
               'state',
               'country',
               'zip',
               'phone',
               'longBusinessSummary',
               'sector',
               'industry',
               'fullTimeEmployees',
               'longBusinessSummary']
    return {k: extract_key(k, json_text) for k in key_set}
