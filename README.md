# HTML Reports

Module for creating html reports based on jinja2 templates.

## Usage

First you should create a report. Then you can add content to it. When you have all the content you can render it in a file with the `write_report` function.

For example:

```python
from reports import Report

report = Report()

rep.add_markdown("""
# Hello

Just trying the reports module
""")

rep.write_report()
```

This will create the `report.html` file using the `templates/simple.html` template.

## Installation

	pip install -r requirements.txt

## Authors
* [Arnau Villoro](https://villoro.com)

## License
The content of this repository is licensed under a [MIT](https://opensource.org/licenses/MIT).

## Nomenclature
Branches and commits use some prefixes to keep everything better organized.

### Branches
* **f/:** features
* **r/:** releases
* **h/:** hotfixs

### Commits
* **[NEW]** new features
* **[FIX]** fixes
* **[REF]** refactors
* **[PYL]** [pylint](https://www.pylint.org/) improvements
* **[TST]** tests
