from bs4 import BeautifulSoup as bs
import requests
import re
import csv
import pathlib
import pandas

BASE_DIR = pathlib.Path(__file__).parent


global_url = ["https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"]
list_letters = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Э','Ю','Я']
dict_quan = {}
# Так как после русского алфавита на сайте начинается английский,
#  чтобы закончить подставляем английскую букву "А" 
stop_letter = "А" 

new_dict = {'beasts':[]}
for i in list_letters:
    new_dict['beasts'].append({'letter': i, 'quantity': 0})


def main(url):
    if url != "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту":
        raise ValueError("Указан неверный URL")
    response = requests.get(url=url)
    result = response.text

    soup = bs(result, 'html.parser')

    #get links for parsing
    main_link = "https://ru.wikipedia.org/"
    all_links = []
    try:
        for i in soup.find_all('a'):
            if i.find(string="Следующая страница"):
                links = i  
    except:
        print("Error")
    all_links.append(main_link+links['href'])
    

    divs = soup.find_all('div', class_='mw-content-ltr')
    for div in divs:
        for letter in list_letters:
            new_i = div.find('h3', string=letter)
            if new_i:
                all_li = div.find_all('li')
                
                for j in all_li:
                    titles = []
                    a = j.find('a')
                    if "title" in a.attrs.keys():
                        # Заканчиваем работу если начнется стоп-буква
                        if re.search(f"^{stop_letter}", a['title']):
                            index_count = 0
                            for k,v in dict_quan.items():
                                new_dict['beasts'][index_count]["letter"] = k
                                new_dict['beasts'][index_count]["quantity"] = v
                                index_count += 1
                            save_in_file_csv(new_dict['beasts'])
                            read_csv_pandas()
                            print("END")
                            return "END"
                        if a['title'] not in titles and re.search(f"^{letter}", a['title']):
                            titles.append(a['title'])
                        if letter in dict_quan:
                            dict_quan[letter] += len(titles)
                        else:
                            dict_quan[letter] = len(titles)

    
    print(dict_quan)
    global_url.append(all_links[0])
    ## создаем рекурсию
    return main(all_links[0]) 

def save_in_file_csv(data: dict):
    filename = f"{BASE_DIR}/beasts.csv"
    columns = ['letter', 'quantity']
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def read_csv_pandas():
    df = pandas.read_csv(f"{BASE_DIR}/beasts.csv")
    print(df)

if __name__ == "__main__":
    
    main(global_url[0])
    


   
