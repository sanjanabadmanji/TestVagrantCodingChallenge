# Progarm for In-memory store for recently played songs

OVERVIEW

Create an in-memory store for recently played songs that can accommodate N songs per user, with a fixed initial capacity. This store must have the capability to store a list of song-user pairs, with each song linked to a user. It should also be able to fetch recently played songs based on the user and eliminate the least recently played songs when the store becomes full.

EXAMPLE

Illustration, when 4 different songs were played by a user & Initial capacity is 3: 
Let's assume that the user has played 3 songs - S1, S2 and S3.
The playlist would look like -> S1,S2,S3
When S4 song is played -> S2,S3,S4 
When S2 song is played -> S3,S4,S2 
When S1 song is played -> S4,S2,S1


# Requirement
1. Download the python: https://www.python.org/downloads/windows/

   Also Set the Python Environmental path in advanced setting of your system : https://www.liquidweb.com/kb/how-do-i-set-system-variable-path-for-python-on-windows/
   
2. Download the Visual Studio Code (VSC) IDE: https://code.visualstudio.com/download


## Run the project

1. Create a file in Directory and clone your project

   For cloning your project open the git bash in your file directory and give the below command

   Clone the project

```bash
  git clone https://github.com/sanjanabadmanji/TestVagrantCodingChallenge.git
```

2. Open the Cloned folder in the Visual Studio Code 

    Note: If required download the Python package in VSC IDE -> Go to the Extensions in VSC, search for Python package and install it

    In the terminal give the below command to get the output


```bash
  python python.py
```


