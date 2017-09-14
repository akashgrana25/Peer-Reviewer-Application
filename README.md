# Peer Video Reviewer Application
**https://peer-review-application.herokuapp.com/**

[![Build Status](https://travis-ci.org/akashgrana25/Peer-Reviewer-Application.svg?branch=master)](https://travis-ci.org/akashgrana25/Peer-Reviewer-Application)

This application allows a mechanism to assign N users M different videos to watch. The specifications are provided as follows:

  - No one should review their own video
  - Each person should review /exactly/ M videos
  - Each video should be reviewed /exactly/ M times
  - M must be strictly less than N - if we have 2 people and each watches 2 videos, they
    necessarily have to watch their own video, which we don’t want.


## Example
If we had 4 people (we’ll name them 1, 2, 3 and 4 ) and each were meant to get 2 piece of feedback (N=4, M=2)

| User | Reviewer |
| ------ | ------ |
| 4 | Person 1, Person 2 |
| 3 | Person 2, Person 3 |
| 2 | Person 3, Person 0 |
| 1 | Person 0, Person 1 |


## Approach

> This problem is an example of mamy to many relationship. It can be best implemented using graph data structure. Graphs allow you to store information about the relationship between the different components (here Users).
Graphs help to store information in a way that help implement algorithms and makes problem solving easier.
In this approach graph is represented using a dictionary and is built using array notation.

### Tech

Peer Video Reviewer Application uses the following technologies:

* [Heroku] - is a container-based cloud Platform as a Service (PaaS) to deploy, scale and manage modern apps.
* [Travis CI] - is a hosted, distributed continuous integration service used to build and test software projects hosted at GitHub.
* [Python] - Python is an interpreted, object-oriented, high-level programming language with dynamic semantics!
* [Flask] - Flask is a microframework for Python based on Werkzeug and Jinja 2
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [Javascript] - an object-oriented computer programming language commonly used to create interactive effects within web browsers.

* [jQuery] - a fast, small, and feature-rich JavaScript library


### Installation

Peer Video Review Application requires [Python](https://www.python.org/) v3.5.4+ to run.

The application can be deployed by using.

```sh
$ cd Peer Reviewer Application
$ python app.py
```
Test cases can be run using
```sh
$ cd Peer Reviewer Application
$ python test.py -v
```
   [Travis CI]:<https://travis-ci.org/>
   [Heroku]:<https://www.heroku.com/>
   [Python]:<https://www.python.org/>
   [Flask]: <http://flask.pocoo.org/>
   [Javascript]: <https://www.javascript.com/>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   
   
    
