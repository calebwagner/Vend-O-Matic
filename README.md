# Vend-O-Matic

## Visual Studio Code

Visit the [Visual Studio Code](https://code.visualstudio.com/) website to download and install the code editor.
## Python on Mac

First, install the XCode Command Line tools with the following command in your terminal.

```sh
xcode-select --install
```

### Install Pyenv and Python
pyenv is a tool for managing multiple Python versions.
```bash
brew install pyenv
pyenv install 3.9.13
pyenv global 3.9.13
```

## Add the SQLTools SQLite extension![Screen Shot 2022-11-16 at 6 07 10 PM](https://user-images.githubusercontent.com/81569328/202322155-d1ac74ee-79d3-4ce0-aaf1-cc21db01124a.png)

## Add some data to the database
In the `vend-o-matic/vending.sql` sql file hightlight the CREATE TABLE statments and click "Run on active connection" then hightlight the "INSERT INTO" statements and click "Run on active connection".

![Screen Shot 2022-11-16 at 6 16 03 PM](https://user-images.githubusercontent.com/81569328/202322973-b101d06a-9e37-436c-81dd-85d3361a3d29.png)

Then start up the server by clicking the "Run and Debug" tab then play.

![Screen Shot 2022-11-16 at 6 18 08 PM](https://user-images.githubusercontent.com/81569328/202323418-2f768918-5c7f-4a52-a7fd-19cb8192a0d3.png)
Now you're good to go.

## ERD
Before we go any further here's the ERD. Since the requirements say we'll have 5 of each 3 beverages I have the SodaType as the primary key and soda_type_id on the Soda table as the foreign key.
<img width="811" alt="Screen Shot 2022-11-16 at 6 26 59 PM" src="https://user-images.githubusercontent.com/81569328/202324270-87d5dcbb-7ce8-4012-b621-ef39f1012a59.png">

## Now Postman time
The port will be running on ...
```bash
http://localhost:8000/
```
The base url will get you all coins available.
Here are some other handy endpoints to test with ...
```bash
http://localhost:8000/inventory
```
Coins with id 1 ...
```bash
http://localhost:8000/inventory/1
```
Coins with id 2
```bash
http://localhost:8000/inventory/2
```
Coins with id 3
```bash
http://localhost:8000/inventory/3
```
