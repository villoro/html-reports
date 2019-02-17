:: create the files
python setup.py sdist bdist_wheel

:: upload to pypi (pip)
python -m twine upload dist/*


:: ------------------------ code to upload to test ----------------------------

:: upload to pypi TEST (pip)
:: python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

:: Check installation from test
:: pip install --index-url https://test.pypi.org/simple/ html-reports
