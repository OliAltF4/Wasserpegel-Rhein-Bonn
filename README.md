# Wasserpegel
This project is a Telegram bot designed to provide real-time water level updates for the Rhine River at Bonn. By leveraging data from the official Pegel Online API, the bot offers insights into current water levels and historical trends. It is packaged in a lightweight Docker container for ease of deployment and is intended to include CI/CD pipelines for streamlined updates and task automation.

## Prerequisites
-Python 3.x installed on your system

-Telegram account

-Docker

## Getting started

### Create a Telegram Bot Using BotFather

1. Open Telegram and search for BotFather.
2. Start a chat with BotFather and use the command /newbot .
3. Follow the prompts to
   
     -Give your bot a name.
  
     -Assign it a unique username ending in bot.
  
5. Once created,you will receive a token that looks like this: 123456789:ABCdefGhIJklMnoPQRstUVwXyZ123456789

Important: Keep this token secure, it grants controle over your bot.

### Set the token as an Environment Variable

For the bot to work locally or in a Docker container, you need to configure the token as an environment variable named TELEGRAM_TOKEN.

    -Local Development: Add the following line to your terminal or .env file:
    export TELEGRAM_TOKEN="your-bot-token"

    Replace your-bot-token with the token provided by BotFather.
    If using a .env file, install a library like python-dotenv and load the variables in the script:
    from dotenv import load_dotenv
    load_dotenv()

    -Running in Docker: When running the bot in a Docker container, pass the token as an environment variable:
    docker run -e TELEGRAM_TOKEN="your-bot-token" your-docker-image

