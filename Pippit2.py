from bs4 import BeautifulSoup
import urllib.request
import tkinter as tk
import tkinter.messagebox
import io
from matplotlib import pyplot as plt


def remove_space(x):

    return '%20'.join(x.split())


def remove_space_dash(x):

    return '-'.join(x.split())


def get_int(s):
    a = []
    for i in range(len(s)):

        if s[i].isdigit() or (s[i] == '.' and (s[i-1] != 's' and i != 0)):
            a.append(s[i])
    a = ''.join(a)

    x = float(a)
    return int(x)


# Includes: Amazon(IN), Flipkart, Snapdeal, Ebay(IN), ShopClues, PaytmMall
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


def find(l,s):

    for i in range(len(l)):

        if l[i]==s:
            return i

    else:
        return False


def show_stats_amzn(item_name):

    try:
        with open('Previous Searches.txt', 'r') as file:

            text = file.read()
            removed_symbs = ''.join(text).split()

        item_tofind = remove_space_dash(item_name)
        item_index = find(removed_symbs, item_tofind)

        prv_amzn = removed_symbs[item_index+1]
        new_amzn = amazon_price(item_name)

        x = [0, 10]
        y = [int(prv_amzn), get_int(new_amzn)]

        plt.plot(x, y)
        plt.show()
    except:
        tkinter.messagebox.showinfo('Error', 'No previous history of search found.')


def show_stats_flpk(item_name):

    try:
        with open('Previous Searches.txt', 'r') as file:

            text = file.read()
            removed_symbs = ''.join(text).split()

        item_tofind = remove_space_dash(item_name)
        item_index = find(removed_symbs, item_tofind)

        prv_flpk = removed_symbs[item_index+2]
        new_flpk = flipkart_price(item_name)

        x = [0, 10]
        y = [int(prv_flpk), get_int(new_flpk)]

        plt.plot(x, y)
        plt.show()
    except:
        tkinter.messagebox.showinfo('Error', 'No previous history of search found.')


def show_stats_sndp(item_name):

    try:
        with open('Previous Searches.txt', 'r') as file:

            text = file.read()
            removed_symbs = ''.join(text).split()

        item_tofind = remove_space_dash(item_name)
        item_index = find(removed_symbs, item_tofind)

        prv_sndp = removed_symbs[item_index+3]
        new_sndp = snapdeal_price(item_name)

        x = [0, 10]
        y = [int(prv_sndp), get_int(new_sndp)]

        plt.plot(x, y)
        plt.show()
    except:
        tkinter.messagebox.showinfo('Error', 'No previous history of search found.')


def show_stats_ebay(item_name):

    try:
        with open('Previous Searches.txt', 'r') as file:

            text = file.read()
            removed_symbs = ''.join(text).split()

        item_tofind = remove_space_dash(item_name)
        item_index = find(removed_symbs, item_tofind)

        prv_ebay = removed_symbs[item_index+4]
        new_ebay = ebayin_price(item_name)

        x = [0, 10]
        y = [int(prv_ebay), get_int(new_ebay)]

        plt.plot(x, y)
        plt.show()
    except:
        tkinter.messagebox.showinfo('Error', 'No previous history of search found.')


def show_stats_sclues(item_name):

    try:
        with open('Previous Searches.txt', 'r') as file:

            text = file.read()
            removed_symbs = ''.join(text).split()

        item_tofind = remove_space_dash(item_name)
        item_index = find(removed_symbs, item_tofind)

        prv_sclues = removed_symbs[item_index+5]
        new_sclues = sclues_price(item_name)

        x = [0, 10]
        y = [int(prv_sclues), get_int(new_sclues)]

        plt.plot(x, y)
        plt.show()
    except:
        tkinter.messagebox.showinfo('Error', 'No previous history of search found.')


def show_stats_ptm(item_name):

    try:
        with open('Previous Searches.txt', 'r') as file:

            text = file.read()
            removed_symbs = ''.join(text).split()

        item_tofind = remove_space_dash(item_name)
        item_index = find(removed_symbs, item_tofind)

        prv_ptm = removed_symbs[item_index+6]
        new_ptm = ptm_price(item_name)

        x = [0, 10]
        y = [int(prv_ptm), get_int(new_ptm)]

        plt.plot(x, y)
        plt.show()
    except:
        tkinter.messagebox.showinfo('Error', 'No previous history of search found.')


def previous_searches():

    with open('Previous Searches.txt', 'r') as file:
        text = file.read()
        removed_symbs = ''.join(text).split()
        removed_symbs = '\t'.join(removed_symbs)

    label_hist = tk.Label(text=removed_symbs)
    label_hist.place(relheight=1, relwidth=1, relx=0, rely=0)

    back = tk.Button(label_hist, text='Back', command= lambda: label_hist.destroy())
    back.place(relheight=0.05, relwidth=0.05, relx=0, rely=0)


def compld(item_name):

    label_amazon_name['text'] = amazon_pname(item_name)
    amzn_price = label_amazon_price['text'] = amazon_price(item_name)

    label_flipkart_name['text'] = flipkart_pname(item_name)
    flpk_price = label_flipkart_price['text'] = flipkart_price(item_name)

    label_snapdeal_name['text'] = snapdeal_pname(item_name)
    snd_price = label_snapdeal_price['text'] = snapdeal_price(item_name)

    label_ebay_name['text'] = ebayin_pname(item_name)
    ebay_price = label_ebay_price['text'] = ebayin_price(item_name)

    label_sclues_name['text'] = sclues_pname(item_name)
    scl_price = label_sclues_price['text'] = sclues_price(item_name)

    label_ptm_name['text'] = ptm_pname(item_name)
    paytm_price = label_ptm_price['text'] = ptm_price(item_name)

    # Storing Search

    with io.open('Previous Searches.txt', 'a', encoding='utf-8') as file:

        file.write('\n')
        file.write(remove_space_dash(item_name))
        file.write(f" \n{get_int(amzn_price)} \t")
        file.write(f" \n{get_int(flpk_price)} \t")
        file.write(f" \n{get_int(snd_price)} \t")
        file.write(f" \n{get_int(ebay_price)} \t")
        file.write(f" \n{get_int(scl_price)} \t")
        file.write(f" \n{get_int(paytm_price)} \t")
        file.write('\n')

        print(amzn_price)
        print(flpk_price)
        print(snd_price)
        print(ebay_price)
        print(scl_price)
        print(paytm_price)



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
sub.add_command(label='Statistics of Previous Prices on Amazon', command=(lambda: show_stats_amzn(search_entry.get())))
sub.add_command(label='Statistics of Previous Prices on Flipkart', command=(lambda: show_stats_flpk(search_entry.get())))
sub.add_command(label='Statistics of Previous Prices on Snapdeal', command=(lambda: show_stats_sndp(search_entry.get())))
sub.add_command(label='Statistics of Previous Prices on Ebay', command=(lambda: show_stats_ebay(search_entry.get())))
sub.add_command(label='Statistics of Previous Prices on ShopClues', command=(lambda: show_stats_sclues(search_entry.get())))
sub.add_command(label='Statistics of Previous Prices on PayTM', command=(lambda: show_stats_ptm(search_entry.get())))

sub2 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Others', menu=sub2)
sub2.add_command(label='Previous Searches', command=previous_searches)
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
