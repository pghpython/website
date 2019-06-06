# pghpython website


## Stack

This site is built using [Pelican](https://docs.getpelican.com/en/stable/), a static site generation framework.


## Developing

1. Clone this repository and change to the newly created directory:

    ```shell
    $ git clone git@github.com:pghpython/website.git  # or over HTTPS if you prefer
    $ cd website/
    ```

1. Create and activate a virtual environment for working on this project.
   You can use whichever tool you like (I use `pyenv`/`pyenv-virtualenv` myself, but the built-in `venv` works fine):

    ```shell
    $ python3 -m venv .venv/
    $ source .venv/bin/activate
    ```

1. Install the dependencies:

    ```shell
    (.venv) $ pip install -r requirements.txt
    ```

1. Build and serve a local copy of the content:

    ```shell
    (.venv) $ pelican content
    Done: Processed 0 articles, 0 drafts, 1 page, 0 hidden pages and 0 draft pages in 0.14 seconds.
    (.venv) $ pelican --listen
    ```

    The site should now be available [on your local host](http://localhost:8000).

    You can also use `make` if you prefer (you can just type `make` to see all the available options):

    ```shell
    (.venv) $ make html
    (.venv) $ make serve
    ```
