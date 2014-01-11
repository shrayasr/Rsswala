#Rsswala [![Build Status](https://travis-ci.org/shrayas/Rsswala.png?branch=master)](https://travis-ci.org/shrayas/Rsswala)
> The ever-so-simple RSS reader (or at least thats what we think it is)  

***Ideated during the 2013 Aaron Swartz Day [Hacknight](https://hacknight.in/hasgeek/2013-aaron-swartz-day/projects/2-rsswala) organized by [HasGeek](https://github.com/hasgeek)***

##BOOM.

![screeie](https://raw.github.com/shrayas/rsswala/master/rsswala.png)

##Contributors
* [VK](https://github.com/vkarthik26) 
* [Me](https://github.com/shrayas)

##Why another RSS reader?
* We wanted to learn about how the RSS protocol is built and we felt nothing out there still stands in front of the mighty Google Reader
* Because we wanted to learn how to do things right with PY 

##Documentation
* [API-Endpoints](https://github.com/shrayas/rsswala/wiki/API-Endpoints)


##Installation
* Clone the repo
* Start MySQL instance
* `cd rsswala`
* `mysql -u <USERNAME> -p < rsswala.sql`
* `virtualenv env`
* `source env/bin/activate`
* `pip install -r requirements.txt`
* `cd app`
* `cp conf.sample.py conf.py`
* Make the Required changes in `conf.py`
* `cd ..`
* `python run.py`

##TODO
Check [issues](https://github.com/shrayas/Rsswala/issues)
