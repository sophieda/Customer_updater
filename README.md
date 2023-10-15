# Customer & Purchase updater

## Context
This is a repository to complete a small exercise on software building with python.
The instructions are provided at the root of the project under the name "Python exam - Customers & Purchases.pdf".

## Notes
I made this project with the idea of overengineering it, as if it was made to be modified and enhanced in the future.
In reality the solution could be done in one single python script but I believe it was not the correct choice for this exercise.

## Installation
Have a python interpretor on python 3.7 or above and run from the root of the project
```
pip install -r requirements.txt
```

## Usage
Run from the root of the project
```
python src/main.py cli
```
or
```
python src/main.py gui
```
Then chose the .csv files to load on the application, one for the customer's data, and one for
the purchase's data, then press run.
Input format for cli version (on windows) should look like ```C://Users/JohnDoe/Desktop/and/so/on```