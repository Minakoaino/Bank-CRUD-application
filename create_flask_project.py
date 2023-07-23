import os
import shutil

# Create the project directory
project_dir = "bank-management-app"
os.mkdir(project_dir)

# Create the app directory
app_dir = os.path.join(project_dir, "app")
os.mkdir(app_dir)

# Create the __init__.py file
init_file = os.path.join(app_dir, "__init__.py")
with open(init_file, "w") as file:
    file.write("from flask import Flask\n\napp = Flask(__name__)\n")

# Create the routes.py file
routes_file = os.path.join(app_dir, "routes.py")
with open(routes_file, "w") as file:
    file.write("from app import app\n\n@app.route('/')\ndef index():\n    return 'Hello, World!'\n")

# Create the models.py file
models_file = os.path.join(app_dir, "models.py")
with open(models_file, "w") as file:
    file.write("from app import db\n\n# Define your models here\n")

# Create the run.py file
run_file = os.path.join(project_dir, "run.py")
with open(run_file, "w") as file:
    file.write("from app import app\n\nif __name__ == '__main__':\n    app.run(debug=True)\n")

# Create the README.md file
readme_file = os.path.join(project_dir, "README.md")
with open(readme_file, "w") as file:
    file.write("# Bank Management App\n\nThis is a Flask application for managing banks.\n\n## Installation\n\n1. Clone the repository.\n2. Install the required dependencies.\n3. Run the `run.py` script to start the application.\n")

# Create the templates directory
templates_dir = os.path.join(app_dir, "templates")
os.mkdir(templates_dir)

# Create the HTML templates
create_bank_template = os.path.join(templates_dir, "create_bank.html")
view_bank_template = os.path.join(templates_dir, "view_bank.html")
update_bank_template = os.path.join(templates_dir, "update_bank.html")
list_banks_template = os.path.join(templates_dir, "list_banks.html")

with open(create_bank_template, "w") as file:
    file.write("<h1>Create Bank</h1>\n<!-- Add your HTML form here -->\n")

with open(view_bank_template, "w") as file:
    file.write("<h1>View Bank</h1>\n<!-- Add your HTML template here -->\n")

with open(update_bank_template, "w") as file:
    file.write("<h1>Update Bank</h1>\n<!-- Add your HTML form here -->\n")

with open(list_banks_template, "w") as file:
    file.write("<h1>List Banks</h1>\n<!-- Add your HTML template here -->\n")

# Create the static/css directory
static_dir = os.path.join(app_dir, "static")
os.makedirs(static_dir)
css_dir = os.path.join(static_dir, "css")
os.makedirs(css_dir)

# Copy the styles.css file to static/css directory
styles_src = "path/to/styles.css"  # Specify the source path of styles.css
styles_dest = os.path.join(css_dir, "styles.css")
shutil.copy(styles_src, styles_dest)
