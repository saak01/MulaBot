# MulaBot
 Discord Bot para servidor dos meus amigos











cliente = discord.Client()

@cliente.event
async def bot_on():
    print('O bot está funcionando.')
    print(f'Nome do bot: {cliente.user.name}')
    print(f'Id do bot: {cliente.user.id}')


@cliente.event
async def mensagem(message):
    if message.content.lowet().startswith('*Mix'):
        awai



cliente.run('ODc2OTIyOTEyNDY3MjIyNTc4.YRrIGg.1RbJZNxK3lHbBnaqNjCEpRxpq8o')