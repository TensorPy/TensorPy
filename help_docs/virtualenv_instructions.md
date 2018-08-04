### Virtual Environment Setup Tutorial

First, install virtualenv / virtualenvwrapper:

```bash
python -m pip install virtualenv
python -m pip install virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

If you add ``source /usr/local/bin/virtualenvwrapper.sh`` to your local bash file (``~/.bash_profile`` on Mac, ``~/.bashrc`` on Linux), virtualenvwrapper commands will be available to you whenever you open a new command prompt. You can then use the following commands to make those changes active.

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

```bash
workon tensorpy
```
