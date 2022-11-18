# Vend-O-Matic Installation Steps 🎰 🪙🪙

This project uses Python ![Python-Symbol](https://user-images.githubusercontent.com/81569328/202470670-a8a90c3e-2099-4f23-adf2-7a7fde37f4ea.png) and SQLite ![sqlite](https://user-images.githubusercontent.com/81569328/202470834-58f744d6-3592-43ab-9ed2-98bac31b7e17.png)


## Visual Studio Code

Visit the [Visual Studio Code](https://code.visualstudio.com/) website to download and install the code editor.

## Python on Mac 🐍 💻

Install the XCode Command Line tools with the following command in your terminal.

```sh![sqlite](https://user-images.githubusercontent.com/81569328/202470807-2965fb8f-a8a1-4280-8ff2-fee443a325f7.png)

xcode-select --install
```

## Install Homebrew, Pyenv, and Python

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

pyenv is a tool for managing multiple Python versions.
```bash
brew install pyenv
```
```bash
pyenv install 3.9.13
```
```bash
pyenv global 3.9.13
```

## Install Pipenv

This tool changes the scope of the current pip command to work on the current user account's local python package install location, rather than the system-wide package install location, which is the default.
```sh
pip3 install --user pipenv
```

## Visual Studio Code Extensions

Install these extensions to get VS Code set up. You can also search for these extensions in the "Extensions" tab in VS Code and install them there.

* [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
* [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack)
* [SQLTools](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)
* [SQLTools: SQLite Driver](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools-driver-sqlite)

## Getting the code 0️⃣1️⃣1️⃣0️⃣1️⃣0️⃣0️⃣0️⃣ 0️⃣1️⃣1️⃣0️⃣1️⃣0️⃣0️⃣1️⃣
In your terminal of choice and run the following commands.
```bash
git clone https://github.com/calebwagner/Vend-O-Matic.git
```
```bash
cd Vend-O-Matic/
```
Start a virtual environment.
```bash
pipenv shell
```
```bash
code .
```

## Keyboard Shortcut : Optional

Here's a keyboard shortcut so that you can run a query without needing to use your mouse to click on an icon every time.

1. Cmd+Shift+P if you are on Mac.
1. Type in "shortcut" in the search bar.
1. Choose **Keyboard Shortcuts** from the results.
1. In the search bar for shortcuts, type in "sqltoolrun".
1. Double click the **SQLTools Connection: Run Current Query** option.
1. Hold down the Command key and tap R twice if you are on Mac
1. Then press enter to save the shortcut.

## Continuation of Keyboard Shortcut 
1. Copy the `CREATE TABLE` SQL commands below and paste it into the `vending.sql` file.
1. Highlight all of the text.
1. Press `Cmd+R+R` if you are on Mac. You will then be prompted to choose a connection.
1.  Choose "Python Vending".
1. A new tab will open in VS Code and you should see this message in it - **Query returned 0 rows**. That means it worked.

## Add some data to the database
Now that we're here in VS Code lets start vending. In the `vend-o-matic/vending.sql` sql file hightlight the CREATE TABLE statments and click "Run on active connection" then hightlight the "INSERT INTO" statements and click "Run on active connection" so we can start with some data.

![Screen Shot 2022-11-16 at 6 16 03 PM](https://user-images.githubusercontent.com/81569328/202322973-b101d06a-9e37-436c-81dd-85d3361a3d29.png)

Then start up the server by clicking the "Run and Debug" tab then play.

![Screen Shot 2022-11-16 at 6 18 08 PM](https://user-images.githubusercontent.com/81569328/202323418-2f768918-5c7f-4a52-a7fd-19cb8192a0d3.png)

Now you're good to go.

## ERD
Before we go any further here's the ERD. Since the requirements say we'll have 5 of each 3 beverages I have the SodaType as the primary key and soda_type_id on the Soda table as the foreign key.
<img width="811" alt="Screen Shot 2022-11-16 at 6 26 59 PM" src="https://user-images.githubusercontent.com/81569328/202324270-87d5dcbb-7ce8-4012-b621-ef39f1012a59.png">

## Now Postman time 🌐
The port will be running on ...
```bash
http://localhost:8000/
```
The base url will get you all coins available.
Here are some other handy endpoints to test with ...
```bash
http://localhost:8000/inventory
```
SodaType with id 1 ...
```bash
http://localhost:8000/inventory/1
```
SodaType with id ...
```bash
http://localhost:8000/inventory/2
```
SodaType with id 3 ...
```bash
http://localhost:8000/inventory/3
```

## Screen Recording

<a href="https://www.loom.com/share/a7b21a3e844f4479b3083f04558d7ad3">
    <p>Vend-O-Matic Postman Video</p>
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/a7b21a3e844f4479b3083f04558d7ad3-with-play.gif">
</a>

https://www.loom.com/share/a7b21a3e844f4479b3083f04558d7ad3
