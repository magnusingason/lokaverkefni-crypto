# SmileyCoin Tipping Discord Bot

## How does it work?

The bot is written in python and reacts to commands given through discord. You can command the bot to tip a specific SmileyCoin address through the command:
```
!sendtoaddress [recievers address] [number of smileycoins you want to tip]
```
The bot requires you to have a smileycoin core wallet installed on your linux device as well as be connected to the Smileycoin server through the command:

```
smileycoind --server&
```

The bot also requires for the smileycoin-cli command to be in the bin folder so it can be called globally. More information can be found here: https://tutor-web.net/comp/crypto251.0/@@download-pdf/comp.crypto251.0.pdf

## How does the code work?

Through the discord python library, the code is able to activate a discord bot and read messages sent through a discord server's channel. The code performs some business logic creating the command "smileycoin-cli sendtoaddress [address] [amount]" and executing it through linux. The code has multiple error messages indicating what might be wrong incase of an error

## Screenshots of functionality

![Screenshot](./image.png)

Here is the link to the transaction of the screenshot: https://chainz.cryptoid.info/smly/tx.dws?cce530367656667c47b09c5066c5e88745264ddcb3cc47a926ea9887966aaf5f.htm