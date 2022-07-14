from bs4 import BeautifulSoup
import requests
import translators as ts

if __name__ == '__main__':
    url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
    page = requests.get(url).text
    page_s = BeautifulSoup(page, 'html.parser')
    titles = page_s.select('.gallery h3.title')
    films = []

    for title in titles:
        text = title.getText()
        number, trash, film = text.partition(' ')
        new_dict = {
            'number': number,
            'film': film
        }
        films.append(new_dict)
    films = films[::-1]
    with open('./movies.txt', 'w') as file:
        for film_dict in films:
            film_name_translate = ts.google(film_dict['film'], to_language='uk')
            row = f"{film_dict['number']} {film_dict['film']} | {film_name_translate}\n"
            file.write(row)
