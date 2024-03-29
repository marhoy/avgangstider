
Developing
==========

#.  Install `pyenv <https://github.com/pyenv/pyenv>`_ with some plugins,
    especially `pyenv-virtualenv <https://github.com/pyenv/pyenv-virtualenv>`_
    and `pyenv-which-ext <https://github.com/pyenv/pyenv-which-ext>`_.
    These extensions will be installed automatically if you use the
    `pyenv-installer <https://github.com/pyenv/pyenv-installer>`_
#. Install Poetry


Setting up your development environment
---------------------------------------
 ::

    # Install Python 3.9 and make a new virtual environment
    pyenv install 3.9.7
    pyenv virtualenv 3.9.7 avgangstider

    # Clone the repository
    git clone git@github.com:marhoy/flask-entur-avgangstider.git

    # Activate the virtual environment for this directory
    cd flask-entur-avgangstider
    pyenv local avgangstider 3.9.7

    # Install all requirements (also for development)
    poetry install


Start a debugging server
------------------------

 ::

    python src/avgangstider/flask_app.py


Run all tests and code checks
-----------------------------

After having made changes: Make sure all tests are still OK, test coverage
is still 100% and that flake8, mypy and isort are all happy::

    tox

    [...]
    src/avgangstider/utils.py .                                              [  6%]
    tests/test_classes.py .                                                  [ 12%]
    tests/test_entur_api.py ...                                              [ 31%]
    tests/test_entur_query.py ...                                            [ 50%]
    tests/test_flask_app.py .......                                          [ 93%]
    tests/test_utils.py .                                                    [100%]

    ---------- coverage: platform darwin, python 3.7.4-final-0 -----------
    Name    Stmts   Miss  Cover   Missing
    -------------------------------------
    -------------------------------------
    TOTAL     197      0   100%

    7 files skipped due to complete coverage.


    ============================== 16 passed in 4.39s ==============================

    [...]
    lint run-test: commands[0] | poetry run flake8 src tests
    lint run-test: commands[1] | poetry run isort --check-only src tests
    lint run-test: commands[2] | poetry run mypy src

    [...]
    ___________________________________ summary ____________________________________
    py37: commands succeeded
    py38: commands succeeded
    py39: commands succeeded
    lint: commands succeeded
    docs: commands succeeded
    congratulations :)


Build new docker image
----------------------

If you want to build your own docker image::

    docker build -t avgangstider .
    docker run -d -p 5000:5000 avgangstider


