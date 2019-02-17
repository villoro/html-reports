""" Reports module """

import os

import easydev
from jinja2 import Template
from markdown import markdown
from bs4 import BeautifulSoup


def read_template(uri):
    """ Loads a jinja2 template """

    with open(uri, "r") as file:
        return Template(file.read())


def transform_markdown(text):
    """ auxiliar function to transform markdown to html """

    return markdown(text, extensions=["fenced_code", "codehilite"])


class Report:
    """ html report class """

    def __init__(self, title="Report", scripts=[], raw_scripts=[], styles={}):

        # Main arguments
        self.args = {"title": title}

        # Script resources
        self.scripts = scripts
        self.raw_scripts = raw_scripts

        # Style resources
        self.styles = styles

        # Body
        self.body = []

    def add_script(self, script, raw=False):
        """ Adds a script resource """
        if raw:
            self.raw_scripts.append(script)

        else:
            self.script.append(script)

    def add_style(self, style):
        """ Add a style resource """

        self.styles.append(style)

    def add_markdown(self, text):
        """ Adds raw markdown """

        self.body.append(transform_markdown(text))

    def add_title(self, title, level=1):
        """ Adds a title """

        # Create a title using markdown
        self.add_markdown(f"{'#'*level} {title}")

    def write_report(
        self, template_name="simple", template_path=None, filename="report.html", prettify=True
    ):
        """
            Writes the html report.

            Args:
                template_name:  name of the template to use (only used if template_path is None)
                template_path:  path of the custom template to use
                filename:       output file to write
                prettify:       bool to prettify the output html

            Available templates are:
            * simple
        """

        # If no custom path, use one of the predefined templates
        if template_path is None:
            relative_uri = f"html_reports/templates/{template_name}.html"

            template_uri = os.sep.join(
                [easydev.get_package_location("html_reports")] + relative_uri.split("/")
            )

        # Else, use user template
        else:
            template_uri = template_path

        # Load jinja2 template
        template = read_template(template_uri)

        # Render jinja2 template
        output = template.render(
            body="\n".join(self.body),
            scripts=self.scripts,
            raw_scripts=self.raw_scripts,
            styles=self.styles,
            **self.args,
        )

        # Prettify html file
        if prettify:
            output = BeautifulSoup(output, "html.parser").prettify()

        # Write html file
        with open(filename, "w") as file:
            file.write(output)
