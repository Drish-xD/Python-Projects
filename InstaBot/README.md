# Instagram Bot

Instagram Bot is a simple bot that allows you to Upload Pics and Send Messages to Instagram. It uses the python2 module [instabot](https://pypi.org/project/instabot/).

## Installation

_Install the required dependencies:_

- [Python 2.7](https://www.python.org/downloads/)
- `pip install -r requirements.txt`

## Usage

_Add Required Arguments in the `config.py` file._

> - Username: `username`
> - Password: `password`
> - img: `uploaded_pics`
> - caption: `caption for the uploaded pics`
> - users: `usernames of users to send messages`
> - msg: `messages to send to the users`

### Run the Script:

- _For Uploading Pics:_

> ```
> python instabot.py upload
> ```

- _For Sending Messages:_

> ```
> python instabot.py message
> ```
