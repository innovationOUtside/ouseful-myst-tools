from traitlets import default
from traitlets.config import Config

from nbconvert.exporters.templateexporter import TemplateExporter

# from jinja2 import Environment, FileSystemLoader
# from pathlib import Path
import os

# import json
# import pkg_resources


class MystTemplateExporter(TemplateExporter):
    export_from_notebook = "MyST (ouseful)"
    output_mimetype = "text/markdown"

    def _file_extension_default(self):
        return ".md"
    
    def _template_name_default(self):
        return "myst"