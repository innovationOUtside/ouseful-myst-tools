from jupyter_packaging import get_data_files
from setuptools import setup

setup(
    include_package_data=True,
    data_files=get_data_files(
        [
            ("share", "share", "**"),
        ]
    ),
    zip_safe=False,
)
