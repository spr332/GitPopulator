GitPopulator
=============
This project is built to randomly populate a commit history graph in github.
This project was built because a friend of mine said that my commit history graph is deplorably empty.
The ultimate goal of this project is to baffle him with a reasonably filled in graph.

This project is basically done and is reasonably simple to set up and use for yourself, however I do invite anyone to use it and/or contribute.
If you do use this, please don't modify or delete the README.md file.

How to use this software
------------------------
This software requires Python 3 and git. It is even easier to use with GitHub Desktop.
Copy the contents of the repository into a folder, without the .git folder.
Then open the repository folder in a shell and paste in the following:
```
pip3 install -r requirements.txt
```
Then run the GitPopulator.py
```
python GitPopulator.py
```
Then open the folder in GitHub and publish the repository.
For the commit history graph to be visible to everyone who views your account, you must make the repository public.

Developing and Contributing
---------------------------
To develop this project further, please fork the original repository at [spr332/GitPopulator](https://github.com/spr332/GitPopulator)
