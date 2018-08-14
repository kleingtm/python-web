# python-web

Flask RESTful Plus: https://flask-restplus.readthedocs.io/en/stable/quickstart.html#

## Getting up and running on OSX
1. Have x-code installed. (for GCC)
2. Install Homebrew
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew upgrade
```

3. Export Homebrew PATH in `~/.profile`: 
```
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

4. Install python (version 3 by default)
```
brew install python
```

5. Export python PATH in `~/.bash_profile`. Make sure there aren't any other PATH settings there.
```
export PATH=/usr/local/opt/python/libexec/bin:~/Library/Python/3.7/bin:$PATH
```

6. Run the following in the terminal:
```
source ~/.bash_profile
```

7. Restart terminal. Check versions
```
python --version
> Python 3.7.0
pip --version
> pip 18.0 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```

8. Install pipenv with pip (pip3 should have been installed as part of installing python)
```
pip install --user pipenv
```

9. Enter the virtualenv, and install dependencies:
```
pipenv shell
pipenv install
```

10. Run the app:
```
python src/app.py
```


### Adding dependencies with pipenv
```
pipenv install <package-name>
```


