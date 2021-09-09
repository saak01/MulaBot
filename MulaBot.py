import discord
from discord.ext import commands
from random import *

bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")

@bot.command()
async def level(ctx):
    level = randint(0,20)
    await ctx.send('=-='*20)
    await ctx.send(f'Seu level é: {level}')
    if 0 <= level <=5:
        await ctx.send(f'Amigo,você joga em um volante ?')
    if 6 <= level <= 10:
        await ctx.send('ATENÇÃO!!! Cone detectado!!!')
    if 11 <= level <= 15:
        await ctx.send('Você é razoavel, melhor dizendo...Medíocre') 
    if 16 <= level <= 18:
        await ctx.send('Você é bom. Só falta melhorar: posicionamento de mira, noção de espaço no mapa, movimentação, comunicação, utilitárias, noção de jogo, reflexo, tirando isso ta tudo perfeito') 
    if 19 <= level <= 20:
        await ctx.send('Você é bom amigo, Parabéns!')
    await ctx.send('=-='*20)



@bot.command()
async def mix(ctx):
    await ctx.send('=-='*20)
    await ctx.send(f'''
    --Lista de Servidores Mix--

Russu: connect 164.163.32.149

Fernandinho: 

    ''')
    await ctx.send('=-='*20)

@bot.command()
async def galil(ctx):
    await ctx.send('Simplismente um laser! Fidelize com a galhar e veja seus melhores sonhos se tornarem realidade!!!!')

    

@bot.command()
async def mapa(ctx):
    mapas=('Mirage','Dust2','Inferno','Ancient','Nuke','Overpass','Vertigo')
    esc=choice(mapas)
    await ctx.send(f'O mapa escolhido foi: {esc}')

@bot.command()
async def cap(ctx):
    while True:
        cap1 = randint(1,10)
        cap2 = randint(1, 10)
        if cap1 != cap2:
            await ctx.send(f'O capitães serão {cap1}, {cap2}')
            break

@bot.command()
async def sak(ctx):
    await ctx.send('''O melhor jogador de deagle do mundo. Rejeite falsos icones e entre para o sakismo! assim você
reconquistará a confia do seu querido paizinho, que saiu de casa para comprar Malboro. ''')




bot.run('token')


