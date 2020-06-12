import requests
from lxml import etree
import lxml.html
import csv

def parser(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    song_title = tree.xpath('/html/body/div[7]/h1/text()')
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')

    with open('translate.csv', 'w', newline='') as csv_file:
        write = csv.writer(csv_file)
        for i in range(len(text_original)):
            write.writerow(text_original[i])
            write.writerow(text_translate[i])

def main():
    parser('https://www.amalgama-lab.com/songs/j/johnny_cash/hurt.html')

if __name__ == '__main__':
    main()
