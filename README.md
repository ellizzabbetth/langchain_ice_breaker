# Ice Breaker

Installing Python 3.11

pipenv:
https://gist.github.com/monkut/35c2ef098b871144b49f3f9979032cee

linkedin "scrape" to work around proxycurl: https://gist.github.com/ellizzabbetth

pipenv install google-search-results

https://brain2life.hashnode.dev/how-to-install-pyenv-python-version-manager-on-ubuntu-2004
https://k0nze.dev/posts/install-pyenv-venv-vscode/

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

To install dependencies:  pipenv install
ex: pipenv install tweepy

TO RUN on Ubuntu:



0

It looks like your interpreter is not picking up pipenv environment

1) check pipenv --where

2) see if in your settings.json file that your pythonPath variable is set to the location {pipenv --where}/bin/python{some version}

3) run again