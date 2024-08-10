# SimpleHTTPServe

## Overview
**SimpleHTTPServe** is a minimalist, no-nonsense HTTP server written in Python. Created purely for fun, this server is as simple as it gets—no third-party dependencies, no unnecessary features, just pure, unfiltered HTTP handling. Note that this project is currently unstable and primarily a learning experiment.

## Features
- Zero third-party dependencies
- Lightweight and easy to understand
- Handles basic HTTP requests and responses
- Designed for simplicity and educational purposes

## Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation
Clone the repository to your local machine:

```bash
pip install SimpleHTTPServe
```

## Usage
```python3
from SimpleHTTPServe import App, Response, HtmlResponse
from http import HTTPStatus

app = App()

def serve(request):
    return Response(HTTPStatus.OK, "aman")

def index(request):
    return HtmlResponse(HTTPStatus.OK, "hello.html")

if __name__=="__main__":
    app.register("GET", "", serve)
    app.register("GET", "/index", index)
    app.start()

```

## Contributing to SimpleHTTPServe

Feel free to add whatever you feel is intresting. Whether you're fixing bugs, adding new features, improving the documentation, or simply offering suggestions, your contributions are highly appreciated.

### How to Contribute

#### 1. Fork the Repository
Click on the "Fork" button at the top of this repository to create your own copy of the SimpleHTTPServe repository. And then create PR.

#### 2. Clone Your Fork
Clone your forked repository to your local machine.

```bash
git clone https://github.com/yourusername/SimpleHTTPServe.git
```

### Next Steps
1. read port from terminal/config
