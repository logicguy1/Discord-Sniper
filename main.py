import json
import time
import bot
import os

class Sniper:
    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
        print(""" █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
                                                        """) # Print the title card

        time.sleep(2) # Wait a few seconds
        self.slowType("Made by: Drillenissen#4268 && Benz#4947", .02) # Print who developed the code
        time.sleep(1) # Wait a little more
        self.slowType("\nInput your Discord token: ", .02, newLine = False)
        token = input("") # Get the discord token

        self.slowType("\nDo you wish to use AutoBump? (Y/n): ", .02, newLine = False)
        bumper = input("")

        if "y" in bumper.lower():
            bumpData = self.setupBump()
        else:
            bumpData = None

        with open("dataPass", "w") as josnFile:
            json.dump(
                {"snipeToken" : token, "bumpServers" : bumpData},
                josnFile
            )

        os.system('cls' if os.name == 'nt' else 'clear')

        self.start(token)

    def slowType(self, text, speed, newLine = True): # Function used to print text a little more fancier
        for i in text: # Loop over the message
            print(i, end = "", flush = True) # Print the one charecter, flush is used to force python to print the char
            time.sleep(speed) # Sleep a little before the next one
        if newLine: # Check if the newLine argument is set to True
            print() # Print a final newline to make it act more like a normal print statement

    def setupBump(self):
        self.slowType("Input a guild ID and channel ID ( Split with a space ) and stop to stop", .02)
        bumpInfo = []

        while True:
            bumpInfoRaw = input(">>> ").strip()

            if bumpInfoRaw.lower() == "stop":
                break

            bumpInfo.append(
                {
                    "guildId" : bumpInfoRaw.split(" ")[0],
                    "channelId" : bumpInfoRaw.split(" ")[1]
                }
            )

        return bumpInfo

    def start(self, token):
        Bot = bot.bot

        Bot.run(
            token,
            bot = False,
            reconnect = True
        )

if __name__ == '__main__':
    NitroSniper = Sniper()
    NitroSniper.main()
