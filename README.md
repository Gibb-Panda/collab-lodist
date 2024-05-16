# Collab Lodist
This platform has been developed to enable comprehensive and efficient management of logisitic, disposition and more. Collab Lodist stands out with its clear structure and intuitive user interface, allowing users to effectively organize and manage their work processes.

## Technologies
### Django
"Collab Lodist" was developed using the Django technology. Django is a popular web framework that is widely used for building high-quality web applications quickly and efficiently. It provides a powerful and secure infrastructure for developing complex applications, and it is known for its scalability and flexibility. With Django, developers can easily create web applications with clean and maintainable code, making it a popular choice for building web applications. The use of Django in the development of "Collab Lodist" ensures that the app is reliable, secure, and easy to maintain.

### Black
Black is an automated code formatter for Python that aims to improve code quality and consistency in Python projects. With its straightforward and immutable formatting, Black ensures that code style is consistent within a project, increasing code readability and maintainability. Using Black in a project like Collab Lodist helps keep the Python code clean and consistent, which contributes to development efficiency in the long term.

### isort
isort is a Python utility used to sort and clean the import statements in files. It automates the tedious and often error-prone manual organization of imports, making the code clearer and easier to understand. Integrating isort into the Collab Lodist development process ensures that all Python files have a consistent import structure, promoting code quality and team collaboration.

### flake8
flake8 is a powerful linting tool for Python that identifies programming errors, style errors, and suspicious constructs. It helps developers adapt their code to the PEP 8 style guidelines, thereby promoting adherence to best practices in Python development. The use of flake8 in the "Collab Lodist" project helps developers write clean and error-free code that is easy to maintain and update.

### Pillow
Pillow is a modern and powerful image editing library in Python. It extends the functionality of the outdated PIL library (Python Imaging Library) and offers a wide range of tools for editing and manipulating images. Using Pillow in "Collab Lodist" allows image editing functions to be easily integrated into the app, be it for uploading user images, creating thumbnails, or other image-related functions.

### djlint
djlint is a tool for analyzing and cleaning HTML and template code, specifically for use with Django templates. It helps find and fix errors and inconsistencies in template files and helps improve the quality and readability of template code. Integrating djlint into the development of "Collab Lodist" ensures that the templates are clean, error-free and easily maintainable, which forms a solid foundation for the application's user interface.

## Installation
### MacOS
#### Clone Project
##### Using SSH
1. Open your command prompt or terminal.
2. Generate an SSH key by typing the command `ssh-keygen -t rsa` and following the prompts.
3. Log in to your GitHub account and navigate to the project you want to clone.
4. Click on the "Clone or download" button and select "Use SSH" in the top right corner of the pop-up.
5. Copy the SSH URL provided.
6. In the command prompt or terminal, navigate to the directory where you want to clone the project.
7. Type the command `git clone git@github.com:Gibb-Panda/collab-lodist-backend.git` and press Enter.
8. Wait for the project to be cloned.

#### Using HTTPS
1. Open your command prompt or terminal.
2. Log in to your GitHub account and navigate to the project you want to clone.
3. Click on the "Clone or download" button and select "Use HTTPS" in the top right corner of the pop-up.
4. Copy the HTTPS URL provided.
5. In the command prompt or terminal, navigate to the directory where you want to clone the project.
6. Type the command `git clone https://github.com/Gibb-Panda/collab-lodist-backend.git` and press Enter.
7. Wait for the project to be cloned.


#### Pyenv
1. Install Pyenv via Homebrew by running the following command in your terminal: `brew install pyenv`
2. Once Pyenv is installed, you can install the desired version of Python. For Django 4.1.7, we recommend using Python 3.11.2 To install this version, run the following command: `pyenv install 3.11.2`.
((Warning: It's global, not in a virtual environment. Not recommend).)
3. To install virtualenv, you can use the following command if you are using macOS and Homebrew: `brew install pyenv-virtualenv`.  This will install pyenv-virtualenv, which is a plugin for pyenv that provides support for creating and managing virtual environment.
4. Once Python is installed, you can create a new virtual environment based on Python 3.11.2. To do this, run the following command in the project: `pyenv virtualenv 3.11.2 venv`.
5. Now navigate to your Django project directory and activate the newly created virtual environment. To do this, run the following commands: `cd (Your Path)/django/project` and `source (your path)/django/project/venv/bin/activte`. This will activate your existing virtual environment.

## API URLs
- [./signup](http://localhost:8000/signup)
- [./login](http://localhost:8000/login)
- [./logout](http://localhost:8000/logout)
- [./system/users](http://localhost:8000/system/users)
- [./system/users/1](http://localhost:8000/system/users/1)
- [./system/roles](http://localhost:8000/system/roles)
- [./system/roles/1](http://localhost:8000/system/roles/1)
- [./system/permissions](http://localhost:8000/system/permissions)
- [./system/permissions/1](http://localhost:8000/system/permissions/1)
- [./logistics/commodities](http://localhost:8000/logistics/commodities)
- [./logistics/commodities/1](http://localhost:8000/logistics/commodities/1)
- [./logistics/storage_conditions](http://localhost:8000/logistics/storage_conditions)
- [./logistics/storage_conditions/1](http://localhost:8000/logistics/storage_conditions/1)
- [./logistics/warehouses](http://localhost:8000/logistics/warehouses)
- [./logistics/warehouses/1](http://localhost:8000/logistics/warehouses/1)
- [./logistics/good_hazard_class](http://localhost:8000/logistics/good_hazard_class)
- [./logistics/good_hazard_class/1](http://localhost:8000/logistics/good_hazard_class/1)

## Roles and their permissions

The command `python manage.py setup` configures the database, which creates all roles and their permissions.

| Roles                     | Permissions                                                                                               |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| **Root**                  | `*`                                                                                                       |
| **Administrator**         | `system.*`, `logistic.*`, `disposition.*`                                                                 |
| **Dispatcher**            | `disposition.*`, `logistic.commodity.update`, `logistic.warehouse.update`, `logistic.good_hazard_class.update`, `logistic.storage_condition.update` |
| **Logistician**           | `logistic.commodity.*`, `logistic.*`                                                                      |
| **Vehicle Manager**       | `disposition.vehicle.read`, `disposition.vehicle.update`                                                  |
| **Road Transport Specialist** | `disposition.tour.read.assigned`, `disposition.tour.update.assigned`                                        |

## Existing Permissions
| Value                                | Description                                                                                      |
|--------------------------------------|--------------------------------------------------------------------------------------------------|
| `*`                                  | All rights                                                                                       |
| `system.*`                           | All rights in user management                                                                    |
| `system.role.*`                      | All CRUD rights for roles                                                                        |
| `system.role.create`                 | Can create roles                                                                                 |
| `system.role.read`                   | Can view all existing roles, including details                                                   |
| `system.role.update`                 | Can update roles                                                                                 |
| `system.role.delete`                 | Can delete roles                                                                                 |
| `system.permission.*`                | All CRUD rights for permissions                                                                  |
| `system.permission.create`           | Can create permissions                                                                           |
| `system.permission.read`             | Can view all existing permissions, including details                                             |
| `system.permission.update`           | Can update permissions                                                                           |
| `system.permission.delete`           | Can delete permissions                                                                           |
| `logistic.*`                         | All logistics-related rights                                                                     |
| `logistic.commodity.*`               | All CRUD rights for commodities                                                                  |
| `logistic.commodity.create`          | Can create commodities                                                                           |
| `logistic.commodity.read`            | Can view all commodities, including details                                                      |
| `logistic.commodity.update`          | Can update commodities                                                                           |
| `logistic.commodity.delete`          | Can delete commodities                                                                           |
| `logistic.warehouse.*`               | All CRUD rights for warehouses                                                                   |
| `logistic.warehouse.create`          | Can create warehouses                                                                            |
| `logistic.warehouse.read`            | Can view all warehouses, including details                                                       |
| `logistic.warehouse.update`          | Can update warehouses                                                                            |
| `logistic.warehouse.delete`          | Can delete warehouses                                                                            |
| `logistic.good_hazard_class.*`       | All CRUD rights for good hazard classes                                                          |
| `logistic.good_hazard_class.create`  | Can create good hazard classes                                                                   |
| `logistic.good_hazard_class.read`    | Can view all good hazard classes, including details                                              |
| `logistic.good_hazard_class.update`  | Can update good hazard classes                                                                   |
| `logistic.good_hazard_class.delete`  | Can delete good hazard classes                                                                   |
| `logistic.storage_condition.*`       | All CRUD rights for storage conditions                                                           |
| `logistic.storage_condition.create`  | Can create storage conditions                                                                    |
| `logistic.storage_condition.read`    | Can view all storage conditions, including details                                               |
| `logistic.storage_condition.update`  | Can update storage conditions                                                                    |
| `logistic.storage_condition.delete`  | Can delete storage conditions                                                                    |
| `disposition.*`                      | All disposition-related rights                                                                   |
| `disposition.tour.*`                 | All CRUD rights for tours                                                                        |
| `disposition.tour.create`            | Can create tours                                                                                 |
| `disposition.tour.read.other`        | Can view all tours, including details                                                            |
| `disposition.tour.read.assigned`     | Can view only assigned tours, including details                                                  |
| `disposition.tour.update.other`      | Can update all tours                                                                             |
| `disposition.tour.update.assigned`   | Can update only assigned tours                                                                   |
| `disposition.tour.delete`            | Can delete tours                                                                                 |
| `disposition.vehicle.*`              | All CRUD rights for vehicles                                                                     |
| `disposition.vehicle.create`         | Can create vehicles                                                                              |
| `disposition.vehicle.read`           | Can view all vehicles, including details                                                         |
| `disposition.vehicle.update`         | Can update vehicles                                                                              |
| `disposition.vehicle.delete`         | Can delete vehicles                                                                              |
