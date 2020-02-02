# SWEGTweet

This is a web application that allows you to download tweets in a specific range of time and regarding particular arguments.
Indicate the arguments by specifying keywords in the form.

### Tech

Dillinger uses a number of open source projects to work properly:

* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [Python] - great UI boilerplate for modern web apps

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

First place yourself in directory *app*.
Install the dependencies by running:

```sh
$ python -m pip -r requirements.txt
```

Or simply

```sh
$ pip -r requirements.txt
```

To run the Web Application, just run the command

```sh
$ python -m flask run
```

Or

```sh
$ flask run
```

The result of the extraction will be stored, as well, into file _results.csv_ inside folder _app/results_

The application will be automatically exposed on you *localhost* on port _5000_

   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [Python]: <https://www.python.org/>
   [Flask]: <https://flask.palletsprojects.com/en/1.1.x/>
