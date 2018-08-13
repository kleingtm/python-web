# python-web

Flask RESTful Plus: http://flask-restplus.readthedocs.io/en/stable/



## Getting up and runningon OSX
1. Have x-code installed. (for the GCC)
2. Install Homebrew
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

3. Export Homebrew PATH in `~/.profile`: 
```
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

4. Install python 3
```
$ brew install python
```

5. Export python PATH in `~/.bash_profile`
```
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```

6. Check version
```
$ python --version
> Python 3.7.0
```

7. Install pip with Homebrew
```
$ brew install pip
```

8. Install pipenv with pip
```
$ pip install --user pipenv
```

9. At the project root, install packages:
```
$ pipenv install
```

### Adding dependencies with pipenv
```
$ pipenv install <package-name>
```


