# Bolt

Idea behind Bolt is to develop a generic high performance crawler that can extract information (Internal links, External links, Images etc.) from a website and display it to the user without requiring user to write any specific code

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Bolt is based on Scrapy and only requires python and pip to be setup on your system. Scrapy might have some other dependencies of its own that are listed [here](https://doc.scrapy.org/en/1.2/intro/install.html#installing-scrapy). Scrapy internally uses the Twisted framework for asynchronous scheduling of crawl requests and has the following dependencies:

- lxml, an efficient XML and HTML parser
- parsel, an HTML/XML data extraction library written on top of lxml,
- w3lib, a multi-purpose helper for dealing with URLs and web page encodings
- twisted, an asynchronous networking framework
- cryptography and pyOpenSSL, to deal with various network-level security needs

### Installing

A step by step series of examples that tell you have to get a development env running

Clone the repo on your system:
```
git clone https://github.com/akskap/bolt.git
```

Switch to 'bolt' directory
```
cd bolt
```

Initiate the crawl
```
scrapy crawl generic
```

## Built With

* [Scrapy](https://scrapy.org/) - The Crawling Framework used

## Future Plans

- Automated script that sets up all python dependencies (Scrapy, Python, Twisted, Lxml etc.) for Bolt to run without problems
- Implementation of custom output formats (JSON, XML etc.)
- Integration with a service that could be used by other tools to remotely crawl a website

## Known Issues

- Logic to avoid crawling external URLs needs to be implemented
- Program output needs to be separated from scrapy logs to distinguish between both
- System should support both - absolute and relative URLs without fail



## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details

