from os import walk
from functools import reduce

class CommandHandler:
        def __init__(self, client, config):
            self.client = client
            self.config = config
            filenames = reduce(lambda x, y: x + y, [files for root, dirs, files in walk('src/commands')])
            filenames = [x for x in filenames if x.endswith(".py") and x != "__init__.py"]
            self.files = filenames
            self.commands = {}
            [goodFiles, badFiles] = [[], []]
            for file in filenames:
                try:
                    fileTo = "src.commands." + file.replace(".py", "")
                    imported = __import__(fileTo, fromlist=["src.commands"])
                    self.commands[imported.Name] = imported
                    goodFiles.append(file)
                except:
                    badFiles.append(file)

            print("Loaded {} commands".format(len(goodFiles)))
            if len(badFiles) >= 1: print("Failed to load {}: {}".format(len(badFiles), ", ".join(badFiles)))

        async def handle(self, msg):
            input = msg.content.lower()
            cName = input.split(" ")[0].replace(self.config["bot"]["prefix"], "")
            args = msg.content.split(" ")[1:]
            if cName in self.commands:
                await self.commands[cName].process(self.client, msg, args, {
                    "CommandHand": self,
                    "client": self.client,
                    "config": self.config
                })

