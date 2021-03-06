from bashbot.exceptions import MacroNotFoundException
from bashbot.settings import settings
from bashbot.terminal.sessions import sessions
from bashbot.utils import extract_prefix


async def execute_macro(ctx, name):
    terminal = sessions().get_by_channel(ctx.channel)

    if name not in settings().macros:
        raise MacroNotFoundException()

    macro = settings().macros[name]
    for line in macro.split('\n'):
        if extract_prefix(line):
            ctx.message.content = line
            await ctx.bot.process_commands(ctx.message)
        else:
            terminal.input(line)
