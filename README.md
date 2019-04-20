# Send Mail using Python
### A GUI Application made using Tkinter in Python 3

#### Main Window
![](images/Screenshot%20from%202019-04-20%2016-03-33.png)
#### Pop UP Window
![](images/Screenshot%20from%202019-04-20%2016-04-49.png)

**Requirements and Dependencies**
* Python3
* smtplib
* sys
* tkinter
* pyinstaller

*All these modules can be downloaded using the `pip install` command.*

**Note: In some of the versions these modules come pre downloaded.**

## How to Use

* First of all clone this repo on your machine using the `git clone` command.

* Next open your mail account and then grant access permission to less secure apps.

* Open the `config.py` file and add your valid mail id and password.

* Leave the Pin variable as it is or add your own pin. This pin will be asked everytime you want to send a mail.

* Open command prompt or terminal and navigate to the cloned folder.

* Run the **mail.py** file using the command `python mail.py` in command prompt or `python3 mail.py` in terminal.

* Add a message and a valid recipient mail id and the pin and click on `Send`.

## Here are the steps to create a .exe file of the program

* Navigate to the cloned folder.

* Run the following command `pyinstaller --onefile mail.py`.

* When the process is completed navigate to the *dist* folder to get the *.exe* file.

## To Dos:

* Write this whole code in OOP model.

* Create a Window that asks user for their mail id, password and pin and saves it to `config.py` file

**Currently works only with G-Mail.** 

**Any issues or bug reports will be highly appreciated**