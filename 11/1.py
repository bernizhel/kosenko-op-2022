# -*- coding: utf-8 -*-

import json
import os
import re
from threading import Thread
from tkinter import *
from tkinter import messagebox
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup
from loguru import logger


def threaded(f):
    def _(*k, **kw):
        thread = Thread(target = f, args = k, kwargs = kw)
        thread.start()
        return thread

    return _


def generate_saved_repo_path(url):
    splitted_parts = list(map(str, urlparse(url).path.split('/')))
    filename = splitted_parts[-2] + '__' + splitted_parts[-1]
    filename += '.json'

    return os.path.realpath(os.path.join(__file__, '..', filename))


KEYS = ['company', 'created_at', 'email', 'id', 'name', 'url']


def extract_keys(data, keys):
    return dict((key, data[key]) for key in keys if key in data)


def get_data(url):
    global KEYS

    logger.debug(f'Fetching the data of {url}...')

    response = httpx.get(url)
    data = response.json()
    data = extract_keys(data, KEYS)

    logger.debug(f'Got {url} successfully.')

    return data


def save_data(data, filepath):
    with open(filepath, 'w') as data_file:
        json.dump(data, data_file, indent = 2)


BASE_URL = 'https://habr.com/ru/post/453444/'

GITHUB_URL_REGEXP = r'(https://)(github.com/)([-\w._]+/[-\w._]+/?)'


def convert_www_to_api(github_url):
    global GITHUB_URL_REGEXP

    return re.sub(GITHUB_URL_REGEXP, r'\1api.\2repos/\3', github_url)


def get_repos():
    global BASE_URL
    global GITHUB_URL_REGEXP

    repos = []

    soup = BeautifulSoup(httpx.get(BASE_URL).text, 'lxml')

    for link in soup.find_all():
        condition = link is not None and 'href' in link.attrs and \
                    re.fullmatch(GITHUB_URL_REGEXP, link.get('href')) and \
                    link.get('href') not in repos

        if condition:
            repos.append(link.get('href'))

    for i in range(len(repos)):
        repos[i] = convert_www_to_api(repos[i])

    logger.debug(f'Found the following amount of repo links: {len(repos)}.')

    return repos


def fetch_repo(entry):
    @threaded
    def _():
        repos = get_repos()

        url = repos[int(entry.get())]

        filepath = generate_saved_repo_path(url)

        data = get_data(url)

        save_data(data, filepath)

        messagebox.showinfo(title = 'Success',
                            message = 'Saved the data into ' + filepath)

    return _


def initialize_app():
    main_window = Tk()
    main_window.minsize(400, 50)
    main_window.title('Retrieve the repo\'s data')

    main_window.grid_rowconfigure(0, weight = 1)
    main_window.grid_rowconfigure(1, weight = 1)
    main_window.grid_rowconfigure(2, weight = 1)
    main_window.grid_columnconfigure(0, weight = 1)

    label_number = Label(
        text = 'Enter # number of repo that you want to fetch:')
    label_number.grid(row = 0, column = 0)

    entry_number = Entry(main_window, width = 6)
    entry_number.grid(row = 1, column = 0)

    button_get = Button(
        text = 'Get it',
        command = fetch_repo(entry_number)
    )
    button_get.grid(row = 2, column = 0)

    main_window.mainloop()


def main():
    initialize_app()


if __name__ == '__main__':
    main()
