# Graph My OSRS Stats!
A very crudge and simple way to graph your Old School RuneScape experience.

![example screenshot](/screenshots/example.png?raw=true)

> Are you someone who is interested in this program, but not sure where to being in its use and installation? Then please, **send me a message!** I can create an automatic, non-developer friendly installation and uninstallation script.

## How to Install
> Instructions are optimally for **Linux** (Debian distros), but MacOS will most likely work too. Sorry, Windows users.

1. Ensure tkinter is installed on your local machine. For Linux distros, use `sudo apt-get install python3-tk`. For other operating systems, refer to https://tkdocs.com/tutorial/install.html
1. Instantiate a new virtual environment with `virtualenv ./env/`, or use a package of your choosing.
1. Activate your virtual environment with `source ./env/bin/activate`
1. Install dependencies `pip3 install -r requirements.txt`. *Be sure your environment is activated!*

## How to Use -
1. Insert the desired username to graph into name.txt
1. Start the program with `bash run.sh`