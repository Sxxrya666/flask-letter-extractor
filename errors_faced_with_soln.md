1. Route Methods: Specify methods=['GET', 'POST'] when form submission is involved, other 405 error will come. 
2. Template Inheritance: Use `{% extends 'base.html' %}` when using template, extend the base template without forgeting to add strings around it
3. use "--ignore-installed" and "--force-reinstall" if ipynb kernel is not installed. eg: `pip install ipkernel --forced-install --ignore-installed`
Try basic solutions first (like pip install package)
If that fails, try slightly more aggressive options (--force-reinstall)
Finally, try the most aggressive options (--ignore-installed)

4. use the check if namespace is eq to dunder main for modularity and run the app. 

