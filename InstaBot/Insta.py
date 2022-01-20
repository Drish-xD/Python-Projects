from instabot import Bot
import config
import compago
app = compago.Application()
# Upload the image to instagram using the bot


@app.command
def upload():
    bot = Bot()
    bot.login(username=config.User['username'],
              password=config.User['password'])
    bot.upload_photo(config.Upload['img'], caption=config.Upload['caption'])


@app.command
def message():
    bot = Bot()
    bot.login(username=config.User['username'],
              password=config.User['password'])
    bot.send_message(config.Message['users'], config.Message['msg'])

if __name__ == '__main__':
    app.run()
