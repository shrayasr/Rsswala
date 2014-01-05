#Rsswala
> The ever-so-simple RSS reader (or at least thats what we think it is)

##Authors
* [VK](https://github.com/vkarthik26) 
* [Me](https://github.com/shrayas)

##Why another RSS reader?
* We wanted to learn about how the RSS protocol is built and we felt nothing out there still stands in front of the mighty Google Reader
* Because we wanted to learn how to do things right with PY 

##Documentation
* [API-Endpoints](https://github.com/shrayas/rsswala/wiki/API-Endpoints)


##Installation
* Clone the repo
* `cd rsswala`
* `virtualenv env`
* `source env/bin/activate`
* `pip install -r requirements.txt`
* `cd app`
* `cp conf.sample.py conf.py`
* Make the Required changes in `conf.py`
* `cd ..`
* `python run.py`

##TODO
* Get UI up and running
* Write tests
* Setup travisCI
* Comment code
