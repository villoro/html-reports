""" Reports module """

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

    def __init__(self, title="Report"):

        # Main arguments
        self.args = {"title": title}

        # Script resources
        self.scripts = []
        self.raw_scripts = []

        # Style resources
        self.styles = {}

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

    def write_report(self, template="templates/simple.html", filename="report.html", prettify=True):
        """ Writes the html reprot """

        # Load jinja2 template
        template = read_template(template)

        # Render jinja2 template
        output = template.render(
            body="\n".join(self.body),
            scripts=self.scripts,
            raw_scripts=self.raw_scripts,
            styles=self.styles,
            **self.args
        )

        # Prettify html file
        if prettify:
            output = BeautifulSoup(output, "html.parser").prettify()

        # Write html file
        with open(filename, "w") as file:
            file.write(output)
