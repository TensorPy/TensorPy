### Virtual Environment Setup Tutorial

First:

```bash
sudo pip install virtualenv
sudo pip install virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

Next, follow the command depending on the system you're using:

Mac users: ``source ~/.bash_profile``
Linux users: ``source ~/.bashrc``

Finally, activate the virtual environment for TensorPy:

```bash
mkvirtualenv tensorpy
```

If you ever need to leave your virtual environment, use the following command:

```bash
deactivate
```

You can always jump back in later:

(If you're using ``virtualenvwrapper``):
```bash
workon tensorpy
```
