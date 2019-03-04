# MrRoss
A python web scraper that finds business leads from the [NY Chamber of Commerce directory](https://www.chamber.nyc/directory.asp")

### Testing 
This scraper uses BeautifulSoup v4 and Python 3.5, make sure these are installed on your machine in order to use this script 
The Makefile for this project includes a command that downloads and installs the dependencies for you. Run ``` make depend ``` to execute this command. 
Make must be installed in order for this to function correctly.

```sh
$ cd MrRoss
$ python main.py
$ make read
```

``` make read ``` opens the csv file using your default csv viewer/editor 

