# Vend-O-Matic

## Python on Mac

First, install the XCode Command Line tools with the following command in your terminal.

```sh
xcode-select --install
```

### Install Pyenv and Python

```bash
brew install pyenv
pyenv install 3.9.13
pyenv global 3.9.13
```

## Install Pipenv
This will help manage 3rd party software later on.
```sh
pip3 install --user pipenv
```
## Add the SQLTools SQLite extension![Screen Shot 2022-11-16 at 6 07 10 PM](https://user-images.githubusercontent.com/81569328/202322155-d1ac74ee-79d3-4ce0-aaf1-cc21db01124a.png)

## Add some data to the database
In the `vend-o-matic/vending.sql` sql file hightlight the CREATE TABLE statments and click "Run on active connection" then hightlight the "INSERT INTO" statements and click "Run on active connection".

![Screen Shot 2022-11-16 at 6 16 03 PM](https://user-images.githubusercontent.com/81569328/202322973-b101d06a-9e37-436c-81dd-85d3361a3d29.png)

Then start up the server by clicking the "Run and Debug" tab then play.

![Screen Shot 2022-11-16 at 6 18 08 PM](https://user-images.githubusercontent.com/81569328/202323418-2f768918-5c7f-4a52-a7fd-19cb8192a0d3.png)

## Go to Postman
The port will be running on ...
```bash
http://localhost:8000/
```
