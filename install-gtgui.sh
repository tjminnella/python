#Building PySide on a Linux System 
#Installing prerequisites

#Install build dependencies:
sudo apt-get install build-essential git cmake libqt4-dev libphonon-dev python2.7-dev libxml2-dev libxslt1-dev qtmobility-dev libqtwebkit-dev

#install latest pip distribution into the Python you installed in the first step: 
#download get-pip.py and run it using the python interpreter of your Python 2.7 
#installation using a command prompt:

wget https://bootstrap.pypa.io/get-pip.py
sudo python2.7 get-pip.py

#Install latest wheel distribution:

sudo pip2.7 install wheel

#pyside isnt installed by default on the raspberry pi, but can be easily installed through the command line by "
sudo apt-get -y install python-pyside

#For python 3, just use this command
sudo apt-get -y install python3-pyside