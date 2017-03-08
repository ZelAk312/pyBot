from time import time

Name = "ping"

async def process(client, msg, args, extra):
    start = time()
    msgToEdit = await client.edit_message(msg, "Getting ping...")
    pingTime = ((time() - start) * 1000)
    if len(args) == 0:
        await client.edit_message(msgToEdit, "Pong!!! {0:.2f}ms".format(pingTime))
    else:
        await client.edit_message(msgToEdit, "Pong!!! {0:.2f}ms | {1}".format(pingTime, " ".join(args)))