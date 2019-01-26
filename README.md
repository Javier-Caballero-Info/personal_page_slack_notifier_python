# Personal Page Slack Notifier - Python

> Python [Django RestFramework API](https://www.django-rest-framework.org/) and [Slack](https://slack.com) webhook interactions

## Table of Contents

- [Overview](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master/README.md#overview)
- [API Description](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master/README.md#api_description)
- [Clone](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master/README.md#clone)
- [Requirements](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#requirements)
- [Installation](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#installation)
	- [Pyhton 3](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#pyhton-3)
	- [Virtual environments - pyenv (Linux/MacOS)](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#virtual-environments---pyenv-linuxmacos)
	- [Creation of virtualenv (Linux/Mac)](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#creation-of-virtualenv-linuxmac)
	- [Dependencies (All)](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#dependencies-all)
- [Environment](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#environment)
- [Test](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#test)
- [Running with Docker](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#running-with-docker)
	- [Building the image](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#building-the-image)
	- [Starting up a container](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#starting-up-a-container)
- [Contributing](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#contributing)
- [Author](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#author)
- [License](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/tree/master#license)

## Overview

This API is a proxy to interact across multiple Slack accounts in a simple hub.

## API Description

For more information about the endpoints of the API please check the [apiary doc](https://personalpageslacknotifierpython.docs.apiary.io/).

## Clone

```bash
git clone https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python.git
git remote rm origin
git remote add origin <your-git-path>
```

## Requirements

* **Python:** 3.6.5 or above

## Installation

The installation is recommended made by python virtual environments (Linux and Mac users). For that reason, the following instruction includes the installation of virtualenv.

1. ### Pyhton 3

    - Debian / Ubuntu
    
        - Ubuntu 16.04
        
        ```Bash
        sudo add-apt-repository ppa:jonathonf/python-3.6
        sudo apt update
        sudo apt install python3.6
        ```
            
        - Ubuntu 16.10 or above
    
        ```bash
        sudo apt update
        sudo apt install python3.6
        ```
    
    - MacOS
    
        - Installer
        
        Install Python 3.6.x from [https://www.python.org/downloads/](https://www.python.org/downloads/).
        
        - Brew
        ```bash
        brew install python3
        ```
    
    - Windows
    
        - Installer
        
        Install Python 3.6.x from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. ### Virtual environments - pyenv (Linux/MacOS) 

    - Debian / Ubuntu
    
    ```bash
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    ```
    
    - MacOS
    
        - Bash
        
        ```bash
        curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
        ```
        
        - Brew
        ```bash
        brew install pyenv
        ```
    
3. ### Creation of virtualenv (Linux/Mac)
    
    Creation of virtualenv:
    
    ```bash
    virtualenv -p python3 <desired-path>
    ```
    Activate the virtualenv:
    
    ```bash
    source <desired-path>/bin/activate
    ```
    
    Deactivate the virtualenv:
    
    ```bash
    deactivate
    ```

4. ### Dependencies (All)

    This will install all dependencies from requirements.txt
    
    ```bash
    pip install -r requirements.txt
    ```

## Environment

Nop environment vars are needed

## Test

Without test for the moment

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

### Building the image
```bash
docker build -t personal_page_slack_notifier_python .
```
### Starting up a container
```bash
docker run -p 8000:8000 personal_page_slack_notifier_python
```
## Contributing

Contributions welcome! See the  [Contributing Guide](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/blob/master/CONTRIBUTING.md).

## Author

Created and maintained by [Javier Hernán Caballero García](https://javiercaballero.info)).

## License

GNU General Public License v3.0

See  [LICENSE](https://github.com/Javier-Caballero-Info/personal_page_slack_notifier_python/blob/master/LICENSE)