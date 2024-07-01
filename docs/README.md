# Discord Goes Hard Bot
Discord bot to detect if the message "goes hard" using machine learning, and then turn that message into some meme.
# How it works
* Scans messages on a given guild in discord.
* Translates them into english, using language detection from googletrans.
* Every message is scanned and fed into handcrafted model, that is loaded using pickle.
* Model created using Decision Tree Classifier, from sklearn.
* Data handcafted and flagged manually utilizng tkinter GUI for convenience.
* No message is ever saved or stored! It is deleted as soon as it is processed and flagged.
* The model does not train on any users messages. It trains on datased created using wonderwords + DialloGPT, stored in SQLite3 utilising SQLAlchemy.
* If the message is deemed "hard" the bot takes one of the images in resource folder and creates a meme with it using PIL
* Utilizes complex discord perms.
* Uses dotenv for correct secret shadowing.
## Example:
![obraz](https://github.com/coolka1234/Discord-Goes-Hard-Bot/assets/88340455/e706a20a-d082-4083-8880-660bd6ea7b73)
