
Developing
==========

#.  Install `uv <https://docs.astral.sh/uv/>`_.


Setting up your development environment
---------------------------------------
 ::


    # Clone the repository
    git clone https://github.com/marhoy/avgangstider.git
    cd avgangstider

    # Set up development environment
    uv sync


Start a debugging server
------------------------

 ::

    uv run python src/avgangstider/flask_app.py


Run all tests and code checks
-----------------------------

After having made changes: Make sure all tests are still OK, test coverage
is still 100% and that linters and formatters are happy::

    uv run pre-commit run --all-files
    uv run pytest

Build documentation
-------------------

    uv sync --group docs
    uv run make -C docs html

Build new docker image
----------------------

If you want to build your own docker image::

    docker build -t avgangstider .
    docker run -d -p 5000:5000 avgangstider


