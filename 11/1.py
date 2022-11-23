# -*- coding: utf-8 -*-

import httpx
from retrying import retry
from loguru import logger

from urllib.parse import urlparse
from threading import Thread
import json
import os

from tkinter import *
from tkinter import messagebox


def tkinter_thread_function(func):
  def _(*k, **kw):
    def __():
      thread = Thread(target=func, args=k, kwargs=kw)
      thread.start()
      return thread

    return __

  return _


def get_path(filename):
  return os.path.realpath(os.path.join(__file__, '..', filename))


def generate_path(url):
  filename = urlparse(url).path.split('/')[-1]
  filename += '.json'
  
  return get_path(filename)


@retry
def get_data(url):
  logger.debug(f'Fetching the data of {url}...')

  response = httpx.get(url)
  data = response.json()

  logger.debug(f'Fetched data of {url} successfully.')

  return data


def save_data(data, filepath):
  with open(filepath, 'w') as data_file:
    json.dump(data, data_file, indent=2)


REPOS = [
  'https://api.github.com/repos/kubernetes/kubernetes',
  'https://api.github.com/repos/apache/spark',
  'https://api.github.com/repos/Microsoft/vscode',
  'https://api.github.com/repos/NixOS/nixpkgs',
  'https://api.github.com/repos/rust-lang/rust',
  'https://api.github.com/repos/firehol/blocklist-ipsets',
  'https://api.github.com/repos/openshift/origin',
  'https://api.github.com/repos/ansible/ansible',
  'https://api.github.com/repos/Automattic/wp-calypso',
  'https://api.github.com/repos/dotnet/corefx',
]


@tkinter_thread_function
def fetch_repo(entry):
  url = REPOS[int(entry.get()[-1])]

  filepath = generate_path(url)

  data = get_data(url)

  save_data(data, filepath)

  messagebox.showinfo(title='Success', message='Saved the data into ' + filepath)


def initialize_app():
  main_window = Tk()
  main_window.minsize(400, 50)
  main_window.title('Retrieve the repo\'s data')
  
  main_window.grid_rowconfigure(0, weight=1)
  main_window.grid_rowconfigure(1, weight=1)
  main_window.grid_rowconfigure(2, weight=1)
  main_window.grid_columnconfigure(0, weight=1)

  label_number = Label(text='Enter your gradebook\'s number:')
  label_number.grid(row=0, column=0)

  entry_number = Entry(main_window, width=6)
  entry_number.grid(row=1, column=0)

  button_get = Button(
    text='Get it',
    command=fetch_repo(entry_number)
  )
  button_get.grid(row=2, column=0)

  main_window.mainloop()


def main():
  initialize_app()


if __name__ == '__main__':
  main()
