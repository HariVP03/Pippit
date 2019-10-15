from bs4 import BeautifulSoup
import urllib.request
import tkinter as tk


def remove_space(x):

    return '%20'.join(x.split())

def remove_space_dash(x):

    return '-'.join(x.split())


# Includes: Amazon(IN), Flipkart, Snapdeal, OLX, Ebay(IN), ShopClues, PaytmMall
def amazon_price(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://www.amazon.in/s?k={item_name_spaced}&ref=nb_sb_noss_2'
    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_price = soup.find('span', class_='a-price-whole')

    try:
        return ''.join(list(item_price))
    except:
        return 'Item Not Found... :('

def amazon_pname(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://www.amazon.in/s?k={item_name_spaced}&ref=nb_sb_noss_2'
    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_pname = soup.find('span', class_='a-size-medium a-color-base a-text-normal')
    try:
        return ''.join(list(item_pname))

    except:
        return 'Item Not Found... :('


def flipkart_price(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://www.flipkart.com/search?q={item_name_spaced}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_price = soup.find('div', class_='_1vC4OE _2rQ-NK')

    try:
        return ''.join(list(item_price))
    except:
        return 'Item Not Found... :('


def flipkart_pname(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://www.flipkart.com/search?q={item_name_spaced}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_pname = soup.find('div', class_='_3wU53n')
    try:
        return ''.join(list(item_pname))
    except:
        return 'Item Not Found... :('


def snapdeal_price(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://www.snapdeal.com/search?keyword={item_name_spaced}&santizedKeyword={item_name_spaced}&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'

    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_pname = soup.find('span', class_='lfloat product-price')
    try:
        return ''.join(list(item_pname))
    except:
        return 'Item Not Found... :('


def snapdeal_pname(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://www.snapdeal.com/search?keyword={item_name_spaced}&santizedKeyword={item_name_spaced}&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'

    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_pname = soup.find('p', class_='product-title')

    try:
        return ''.join(list(item_pname))
    except:
        return 'Item Not Found... :('


def ebayin_price(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={item_name_spaced}&_sacat=0'

    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_pname = soup.find('span', class_='s-item__price')

    try:
        return ''.join(list(item_pname))
    except:
        return 'Item Not Found... :('


def ebayin_pname(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={item_name_spaced}&_sacat=0'

    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_pname = soup.find('h3', class_='s-item__title')

    try:
        return item_pname.get_text('', strip=True)
    except:
        return 'Item Not Found... :('


def sclues_price(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://www.shopclues.com/search?q={item_name_spaced}x&sc_z=&z=1&count=10'

    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_pname = soup.find('span', class_='p_price')

    try:
        return ''.join(list(item_pname))
    except:
        return 'Item Not Found... :('

def sclues_pname(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://www.shopclues.com/search?q={item_name_spaced}x&sc_z=&z=1&count=10'

    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_pname = soup.find('h2')

    try:
        return ''.join(list(item_pname))
    except:
        return 'Item Not Found... :('

def ptm_price(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://paytmmall.com/shop/search?q={item_name_spaced}&from=organic&child_site_id=6&site_id=2&category=66781&brand=1707'

    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_pname = soup.find('div', class_='_1kMS')

    try:
        return item_pname.get_text('', strip=True)
    except:
        return 'Item Not Found... :('


def ptm_pname(item_name):

    item_name_spaced = remove_space(item_name)

    url = f'https://paytmmall.com/shop/search?q={item_name_spaced}&from=organic&child_site_id=6&site_id=2&category=66781&brand=1707'

    response = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    )

    page = urllib.request.urlopen(response)
    soup = BeautifulSoup(page, features='html.parser')
    item_pname = soup.find('div', class_='_2apC')

    try:
        return item_pname.get_text('', strip=True)
    except:
        return 'Item Not Found... :('

def compld(item_name):

    label_amazon_name['text'] = amazon_pname(item_name)
    label_amazon_price['text'] = amazon_price(item_name)

    label_flipkart_name['text'] = flipkart_pname(item_name)
    label_flipkart_price['text'] = flipkart_price(item_name)

    label_snapdeal_name['text'] = snapdeal_pname(item_name)
    label_snapdeal_price['text'] = snapdeal_price(item_name)

    label_ebay_name['text'] = ebayin_pname(item_name)
    label_ebay_price['text'] = ebayin_price(item_name)

    label_sclues_name['text'] = sclues_pname(item_name)
    label_sclues_price['text'] = sclues_price(item_name)

    label_ptm_name['text'] = ptm_pname(item_name)
    label_ptm_price['text'] = ptm_price(item_name)

# Graphical User Interface:

# Initialisations
root = tk.Tk()

root.state('zoomed')
root.title('PippitV2')

canvas = tk.Canvas()
canvas.place(relheight=1, relwidth=1)

# Setting

menu = tk.Menu(root)

sub = tk.Menu(menu, tearoff=0)

menu.add_cascade(label='Settings', menu=sub)
sub.add_command(label='Statistics')

root.config(menu=menu)

# Amazon

label_amazon = tk.Label(canvas, text='Amazon', font=('Roboto', 20))
label_amazon.place(relheight=0.125, relwidth=0.1, relx=0, rely=0.125)

label_amazon_name = tk.Label(canvas)
label_amazon_name.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.125)

label_amazon_price = tk.Label(canvas)
label_amazon_price.place(relheight=0.125, relwidth=0.1, relx=0.9, rely=0.125)

# Flipkart

label_flipkart = tk.Label(canvas, text='Flipkart', font=('Roboto', 20))
label_flipkart.place(relheight=0.125, relwidth=0.1, relx=0, rely=0.25)

label_flipkart_name = tk.Label(canvas)
label_flipkart_name.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.25)

label_flipkart_price = tk.Label(canvas)
label_flipkart_price.place(relheight=0.125, relwidth=0.1, relx=0.9, rely=0.25)

# Snapdeal

label_snapdeal = tk.Label(canvas, text='Snapdeal', font=('Roboto', 20))
label_snapdeal.place(relheight=0.125, relwidth=0.1, relx=0, rely=0.375)

label_snapdeal_name = tk.Label(canvas)
label_snapdeal_name.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.375)

label_snapdeal_price = tk.Label(canvas)
label_snapdeal_price.place(relheight=0.125, relwidth=0.1, relx=0.9, rely=0.375)

# Ebay(in)

label_ebay = tk.Label(canvas, text='Ebay(in)', font=('Roboto', 20))
label_ebay.place(relheight=0.125, relwidth=0.1, relx=0, rely=0.625)

label_ebay_name = tk.Label(canvas)
label_ebay_name.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.625)

label_ebay_price = tk.Label(canvas)
label_ebay_price.place(relheight=0.125, relwidth=0.1, relx=0.9, rely=0.625)

# Shopclues

label_sclues = tk.Label(canvas, text='ShopClues', font=('Roboto', 20))
label_sclues.place(relheight=0.125, relwidth=0.1, relx=0, rely=0.75)

label_sclues_name = tk.Label(canvas)
label_sclues_name.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.75)

label_sclues_price = tk.Label(canvas)
label_sclues_price.place(relheight=0.125, relwidth=0.1, relx=0.9, rely=0.75)

# PayTM

label_ptm = tk.Label(canvas, text='PayTM', font=('Roboto', 20))
label_ptm.place(relheight=0.125, relwidth=0.1, relx=0, rely=0.875)

label_ptm_name = tk.Label(canvas)
label_ptm_name.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.875)

label_ptm_price = tk.Label(canvas)
label_ptm_price.place(relheight=0.125, relwidth=0.1, relx=0.9, rely=0.875)

# Search

search_entry = tk.Entry(root, font=('Roboto', 20))
search_entry.place(relheight=0.05, relwidth=0.6, relx=0.15, rely=0)

search_button = tk.Button(root, text='Search', font=('Roboto', 10), command=(lambda: compld(search_entry.get())))
search_button.place(relheight=0.05, relwidth=0.05, relx=0.75, rely=0)

root.mainloop()
