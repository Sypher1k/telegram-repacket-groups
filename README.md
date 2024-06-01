# Running Python App with Virtual Environment and Publishing Using PyInstaller
https://github.com/Sypher1k/telegram-repacket-groups/tree/main
In this guide, we'll walk through the steps to run a Python application with a required virtual environment and how to publish it using PyInstaller.

## Step 1: Clone the Repository

Clone the repository from GitHub:
```sh
git clone https://github.com/Sypher1k/telegram-repacket-groups.git

cd telegram-repacket-groups
```
## Step 2: Create and Activate Virtual Environment
Create a virtual environment:

```python -m venv venv```

Activate the virtual environment:

```source venv/bin/activate   #On Windows use `venv\Scripts\activate```

## Step 3: Install Dependencies
Install dependencies from the requirements.txt file:

```pip install -r requirements.txt```

## Step 4: Run the Application
Run the Python application:

```python app.py```
## Step 5: Publishing Using PyInstaller
Install PyInstaller:

```pip install pyinstaller```
Generate the executable using PyInstaller:

```pyinstaller --onefile app.py```
This command will generate a single executable file in the dist directory.

PyInstaller Command Options:
* --onefile: Pack everything into a single executable.
## Conclusion
Following these steps, you can easily run a Python application with required virtual environment and publish it as an executable using PyInstaller.

For more information on PyInstaller, refer to the PyInstaller Documentation.
