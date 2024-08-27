<br>

An Experiment

<br>

### Sphinx

Initialise a Sphinx Documentation `docs` directory via:

```bash
mkdir docs && cd docs && sphinx-quickstart
```

Final part alternative

```shell
sphinx-quickstart --ext-autodoc --ext-intersphinx --ext-coverage --ext-mathjax --ext-viewcode --ext-githubpages --extensions=revitron_sphinx_theme --extensions=autodocsumm --extensions=sphinxcontrib.httpdomain --extensions=sphinx.ext.napoleon --extensions=sphinxext.opengraph
```


Build the <abbr title="HyperText Markup Language">HTML</abbr> pages via:

```bash
sphinx-build -E -b html docs/source docs/build/html
```

<br>
<br>

### Remote Development

For further development via a container, the `.devcontainer` directory has

* requirements.txt
* Dockerfile

The requirements file lists the packages/libraries required for development.  An image is built via the command:

```shell
docker build . --file .devcontainer/Dockerfile --tag design
```

Subsequently, a development container is initialised via the command

```shell
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app \
  --mount type=bind,src="$(pwd)",target=/app design
```

Whereby:

* [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the)
* [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di)
* [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your)
* [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s)

<br>
<br>

### Local Development

Alternatively, a local virtual environment can be built via **environment.yml**; **environment.yml** uses the same
**requirements.txt** as [Dockerfile](/.devcontainer/Dockerfile).


<br>
<br>

### References

* [GitHub Raw](https://githubraw.com)

* [Google Hosted Libraries](https://developers.google.com/speed/libraries)

* [`Revitron` Theme](https://github.com/revitron/revitron-sphinx-theme)
* [Requirements File Format](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
* [RST Footnotes](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#footnotes)
* [favicon.io](https://favicon.io)

* [revitron](https://github.com/revitron/revitron)
* [revitron sphinx theme](https://github.com/revitron/revitron-sphinx-theme)
* [read the docs sphinx theme](https://github.com/readthedocs/sphinx_rtd_theme)
  * [source links](https://docs.readthedocs.io/en/stable/guides/edit-source-links-sphinx.html)
  * [configuring](https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html)


* [Theming](https://www.sphinx-doc.org/en/master/usage/theming.html)
* [Sphinx Extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
* [sphinx-contrib](https://github.com/orgs/sphinx-contrib/repositories?type=all)
* [sphinx-quickstart](https://www.sphinx-doc.org/en/master/man/sphinx-quickstart.html)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
