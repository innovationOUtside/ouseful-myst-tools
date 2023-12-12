# ouseful-myst-tools

Tools for working with MyST markdown.

## Exporting Jupyter notebooks to MyST with `nbconvert`

By default, `nbconvert` can convert Jupyter `.ipynb` notebooks to markdown using the commands:

`jupyter nbconvert demo.ipynb --to markdown`
`jupyter nbconvert demo.ipynb --execute --to markdown`

Cell outputs are included in the output markdown. If cell outputs include embedded assets such as images, these are exported into an assets directed and then embedded back into the generated markdown document.

We can extend the markdown template to generate MyST flavoured markdown:

`jupyter nbconvert demo.ipynb --to markdown --template=myst`
`jupyter nbconvert demo.ipynb --execute --to markdown --template=myst`

## Converting Jupyter notebooks to MyST using Jupytext

Jupytext provides a variety of roundtripping conversions between Jupyter notebook

## BUILD and INSTALL

`python3 -m build`

Install as:

`python3 -m pip install .`
