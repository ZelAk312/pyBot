Name = "eval"

async def process(client, msg, args, extra):
    if len(args) == 0:
        await client.edit_message(msg, "No code to eval")
    else:
        try:
            await client.edit_message(msg, "Args: ```py\n{}```\n\nEvaled: ```py\n{}```".format(args, str(eval(" ".join(args)))))
        except Exception as e:
            await client.edit_message(msg, "Args: ```py\n{}```\n\nError: ```py\n{}```".format(args, str(e)))