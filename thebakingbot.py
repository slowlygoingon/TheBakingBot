# Copyright 2018 Slowly/slowlygoingon

import discord
import asyncio
import random
import datetime
from discord.ext import commands
import os
import sys
import logging

logging.basicConfig(level="INFO")

bot = commands.Bot(
    description='The Baking Bot is the amazing official bot for the community & mental health server The Baking Spot. As of now, it has very basic commands, but we hope to implement more of them in the future!',
    command_prefix='tbs!', case_insensitive=True)
timenow = datetime.datetime.utcnow()
bot.remove_command('help')

status2str = {
    discord.Status.dnd: 'Do Not Disturb',
    discord.Status.idle: 'Idle',
    discord.Status.online: 'Online',
    discord.Status.offline: 'Offline'
}

activity2str = {
    discord.ActivityType.playing: 'Playing ',
    discord.ActivityType.streaming: 'Streaming ',
    discord.ActivityType.watching: 'Watching ',
    discord.ActivityType.unknown: 'Unknown - '
}


@bot.listen()
async def on_ready():
    game = discord.Game(name="with a cake | tbs!help")
    await bot.change_presence(status=discord.Status.online, activity=game)
    readymessage = "Hello, I'm up and running! It is " + str(timenow) + "\n" + "System version: " + (sys.version)
    uptimedict['timeuptime'] = timenow
    print(readymessage)


@bot.listen()
async def on_member_join(member):
    msg = discord.Embed(
        title='Welcome!',
        description=
        'Welcome to The Baking Spot!\nTBS is a server centered around **community** (events, fun, and making friends) and **mental health** (recovery and awareness).\nThe main purpose of this server is to relax, have fun, discuss mental health with people who can understand your journey through healing, and encourage each other positively.\n\n.',
        colour=discord.Colour.green())
    msg.add_field(
        name='How to enter',
        value=
        "It's normal if you see few channels: to get full access, just read the #rules channel from the beginning. It should take no more than about 3-4 minutes, but don't skip any part!\nWe have 200+ members, and 25+ channels (many are opt-in) about any kind of topic and interest - yes even baking! Why don't you join your big family ASAP?!\nIf you have any problem, contact @Staff.\n\nWe hope you have fun with us!",
        inline=False)

    if member.guild.id == 369918224713908226:
        await member.send(embed=msg)

    else:
        print("Welcome message was not sent because server ID did not match TBS' ID.")


uptimedict = {
    'timeuptime': 0,
}


@bot.command(aliases=['urgentreport', 'reporturgent'])
async def urgent(ctx, *, message):
    messagetosend = ("User **{0.author}** sent the following report:\n\n'".format(ctx.message) + message) + "'"
    await ctx.message.delete()
    await (await bot.get_user_info(345307151989997568)).send(messagetosend)
    await (await bot.get_user_info(295612342274621442)).send(messagetosend)
    await (await bot.get_user_info(369984506809155586)).send(messagetosend)
    await (await bot.get_user_info(152190605970112512)).send(messagetosend)
    await (await bot.get_user_info(339886120407924736)).send(messagetosend)


@bot.command(aliases=['suggest', 'report'])
async def suggestion(ctx, *, message):
    messagetosend = ("User **{0.author}** suggested/reported the following:\n\n'".format(ctx.message) + message) + "'"
    channel = bot.get_channel(427219707683405844)
    await channel.send(messagetosend)
    await ctx.message.delete()


@bot.command()
async def bugreport(ctx, *, message):
    messagetosend = ("""**BUG REPORT**\n\nUser {0}.author reported the following bug: """.format(ctx.message) + message)
    await ctx.send("Bug report sent. Thank you!")
    await (await bot.get_user_info(345307151989997568)).send(messagetosend)


@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        message1 = discord.Embed(title="Error!", description='I do not know this recipe! (Bot is missing permissions)',
                                 color=0xd90000)
        await ctx.send(embed=message1)
        return

    if isinstance(error, commands.BadArgument):
        message2 = discord.Embed(title="Error!",
                                 description='I do not quite understand what you want me to do... (User input failed to be converted: what you typed after the command is not correct)',
                                 color=0xd90000)
        await ctx.send(embed=message2)
        return

    if isinstance(error, commands.MissingRequiredArgument):
        message3 = discord.Embed(title="Error!",
                                 description='You sure this is the whole recipe? (Missing required argument: you should type something after the command)',
                                 color=0xd90000)
        await ctx.send(embed=message3)
        return

    if isinstance(error, commands.MissingPermissions):
        message4 = discord.Embed(title="Error!", description='You are not my Chef! (You are missing permissions)',
                                 color=0xd90000)
        await ctx.send(embed=message4)
        return

    if isinstance(error, commands.UserInputError):
        message5 = discord.Embed(title="Error!",
                                 description="I do not quite understand what you mean... (Invalid user input)",
                                 color=0xd90000)
        await ctx.send(embed=message5)
        return


class Info():

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong! I'm alive.")

    @commands.command()
    async def invite(self, ctx):
        invitelink = discord.Embed(title="Invite me!",
                                   description="https://discordapp.com/oauth2/authorize?client_id=428260876722634765&scope=bot",
                                   colour=0x082E6F)
        await ctx.send(embed=invitelink)

    @commands.command(aliases=['git', 'github', 'src'])
    async def source(self, ctx):
        link = "https://github.com/slowlygoingon/TheBakingBot/"
        await ctx.send(link)

    @commands.command(aliases=['about'])
    async def info(self, ctx):
        uptimemessage = ("I've been online since " + str(uptimedict['timeuptime'])) + ' UTC.'
        em = discord.Embed(
            title='About this bot', description='All about The Baking Bot.', colour=0x082E6F)
        em.add_field(name='Creator', value='Slowly#1846', inline=False)
        em.add_field(
            name='Thank-yous',
            value="Special thanks to: \n- Sebi's Bot Tutorial\n- Espy (Esp#1204)\n- Chanku (Chanku#4372)\n\nThis bot wouldn't have been possible without your help.",
            inline=False)
        em.add_field(name='Uptime', value=uptimemessage, inline=False)
        em.add_field(name='Version', value='Still in development.', inline=False)
        await ctx.send(embed=em)

    @commands.command()
    async def tumblr(self, ctx):
        await ctx.send('Here is our official tumblr.\nhttps://thebakingspot.tumblr.com/')

    @commands.command()
    async def analyze(self, ctx, member: discord.Member):
        m = "Elaborating..."
        user = ctx.message.mentions[0]
        statusconvert = status2str.get(member.status)

        analyzation = discord.Embed(title="Analyzed!", colour=0x082E6F)
        analyzation.add_field(name="Name", value=user.name + "#" + user.discriminator + " (" + user.display_name + ")",
                              inline=False)
        analyzation.add_field(name="ID", value=user.id, inline=False)
        analyzation.add_field(name="Joined at", value=f"{user.joined_at:%A %d, %B %Y at %H:%M}", inline=False)
        analyzation.add_field(name="Status", value=statusconvert, inline=False)
        analyzation.set_thumbnail(url=user.avatar_url)

        if user.activity is None:
            analyzation.add_field(name="What you up to?", value="Nothing!")
            await ctx.send(m, delete_after=3)
            await asyncio.sleep(3)
            await ctx.send(embed=analyzation)

        else:
            activityconvert = activity2str.get(user.activity.type)
            analyzation.add_field(name="What you up to?", value="{} {}".format(activityconvert, user.activity.name))
            await ctx.send(m, delete_after=3)
            await asyncio.sleep(3)
            await ctx.send(embed=analyzation)

    @commands.command()
    async def faq(self, ctx):
        await ctx.send("Here is a link with all FAQ's.\nhttps://thebakingspot.tumblr.com/faq")

    @commands.command(aliases=['feedbackform'])
    async def feedback(self, ctx):
        await ctx.send(
            'Send a completely anonymous report or feedback regarding the server, other members, or Staff.\nhttps://goo.gl/forms/2pO3gDoxKz45mNh92'
        )

    @commands.group(invoke_without_command=True, aliases=['cmds', 'commandlist', 'commandslist'])
    async def help(self, ctx):
        em = discord.Embed(
            description=
            """These are all the commands groups of The Baking Bot,\nthe official bot for The Baking Spot.\n\nType `tbs!help commandsgroup` to see more on a specific group.\n\n
**About
MentalHealth
Fun
Server**\n\nThis is case-sensitive.""", colour=0x082E6F)
        await ctx.send(embed=em)

    @help.command(name="About")
    async def infomenu(self, ctx):
        em = discord.Embed(title="Info & about commands",
                           description="**invite**   -   Invite me!\n**bugreport**   -   Report a bug.\n**info**   -   Shows basic info about the bot. [about]\n**commands**   -   Shows help message. [help, commandslist]\n**ping**   -   Are you alive, bot?\n**source**   -   Shows bot's source code. [src, git, github]\n",
                           colour=0x082E6F)
        await ctx.send(embed=em)

    @help.command(name="""MentalHealth""")
    async def mentalhealthmenu(self, ctx):
        em = discord.Embed(title="Mental health commands",
                           description="**distraction**   -   Cure boredom or distract yourself from stress.\n**comfort**   -   Tells you something comforting. [comforting, comfortme]\n**whatis** (something)   -   Find a definition on something regarding mental health. [define, definition]\n**anxiety**   -   Breathing gif. [anxious, breathing, calm]\n**grounding**   -   Grounding exercises. [dissociation, panic, flashbacks]\n**emergency**   -   Links to a page with emergency resources. Use this in case of serious suicidal ideation.\n**support**   -   If you need help or advice urgently, check this out. [getsupport, gethelp]\n**positivity**   -   Displays a random nice little gif! [positive]\n**therapy**   -   So you're looking for therapy? (Opens Therapy menu) [therapist, counsellor, counselling]",
                           colour=0x082E6F)
        await ctx.send(embed=em)


    @help.command(name="Fun")
    async def funmenu(self, ctx):
        em = discord.Embed(title="Fun commands",
                           description="**spooniefriendlyrecipe**   -   Gives you a random spoonie-friendly recipe. [sfr]\n**analyze**   -   Show basic info on a user you ping. [user, userinfo]\n**say**   -   Bot repeats what you say. [echo]\n**compliment**   -   Displays a random compliment or says something reassuring. [randomcompliment]\n**dice**   -   Throws a dice. [dicethrow, throwdice]\n**coinflip**   -   Flips a coin. [coin, flipcoin]\n**question**   -   Ask the bot a yes or no question. [ask]\n**dessert**   -   Displays a random gif of a dessert.\n**cornyjoke**   -   Makes a corny joke. [joke, pun, randomjoke, randompun]\n**givecookie**   -   Give someone a cookie. [cookie]\n**hug**   -   Give someone a hug. [givehug, hugs, givehugs]",
                           colour=0x082E6F)
        await ctx.send(embed=em)

    @help.command(name="Server")
    async def servermenu(self, ctx):
        em = discord.Embed(title="Server commands",
                           description="**faq**   -   Displays link to our FAQ page on Tumblr.\n**tumblr**   -   Link to the official Tumblr.\n**report**   -   Send a (non-urgent) report or suggestion to Staff, regular members will NOT see your message. [suggestion]\n**urgentreport**   -   Send an __urgent__ report to Staff, regular members will NOT see your message. __Do not abuse this command.__ [urgent, reporturgent]\n**feedback**   -   Send feedback, suggestions, or reports through an anonymous form. Nobody, not even Staff, will know who sent it. [feedbackform]",
                           colour=0x082E6F)
        await ctx.send(embed=em)


class MentalHealth():
    
    @commands.command()
    async def distraction(self, ctx):
        distractionslist = random.choice([
            """Bored or in need of a distraction?\nTry checking out this website:\n\nhttps://www.ted.com/""",
            """Bored or in need of a distraction?\nTry checking out this website:\n\nhttp://emergencycompliment.com/""",
            """Bored or in need of a distraction?\nTry checking out this website:\n\nhttp://www.pixelthoughts.co/""",
            """Bored or in need of a distraction?\nTry checking out this website:\n\nhttps://www.wikihow.com/Distract-Yourself""",
            """Bored or in need of a distraction?\nTry checking out this website:\n\nhttps://theuselessweb.com/""",
            """Bored or in need of a distraction?\nTry checking out this website:\n\nhttps://www.boredbutton.com/""",
            """Bored or in need of a distraction?\nTry checking out this website:\n\nhttp://www.pointless.com/""",
            """Bored or in need of a distraction?\nTry checking out this website:\n\nhttps://weirdorconfusing.com/""",
            """Bored or in need of a distraction?\nTry checking out this website:\n\nhttps://quickdraw.withgoogle.com/""",
            """Bored or in need of a distraction?\nTry checking out this website:\n\nhttps://goo.gl/11aeqc"""])
        await ctx.send(distractionslist)
          

    @commands.command()
    async def reminder(self, ctx):
        medsreminder = random.choice(["Oof, did you forget your meds? Go take em now then! <@&475280525461028876> Good job.", "Hi there, please take your meds. Done? GG! <@&475280525461028876>", "Hey, this is your frembly remembly to take your meds! :) <@&475280525461028876>"])
        await ctx.send(medsreminder)
        
    @commands.command()
    async def pluralkit(self, ctx):
        pkmessage = """<@466378653216014359> is a that allow people with DID/OSDD (formerly known as *Multiple Personality Disorder*, but that is an outdated name!) to give their alters something that resembles a Discord profile, through the use of webhooks. Users choose a "prefix" for each alter, and when an alter is present, they can use such a prefix to type their message. Their name and profile picture will then appear :thumbsup:
Therefore, there is an actual person behind these users that appear as "Bots"."""
        await ctx.send(pkmessage)
        

    @commands.group(invoke_without_command=True, aliases=["define", "definition"])
    async def whatis(self, ctx):
        errormessage = discord.Embed(title="Error!",
                                     description="You must specify what you want to know about. The correct format is: `tbs!whatis whateveryouwant`, the command is case sensitive.\n\nTo know the available definitions, type `tbs!whatis list`.",
                                     colour=discord.Colour.red())
        await ctx.send(embed=errormessage)


    @whatis.command(name="list")
    async def whatis_list(self, ctx):
        list = discord.Embed(title="List of available definitions",
                             description="**Important:** Please inspect trigger warning-worthy definitions with caution.\n\nabuse, anxiety, bipolar, counsellor, c-ptsd, depression, did, dsm, grounding, icd, osdd, ptsd, psychiatrist, psychologist, schizophrenia, therapist, therapy, trauma")
        await ctx.send(embed=list)

    @whatis.command(name="grounding")
    async def whatis_grounding(self, ctx):
        groundingmessage = discord.Embed(title="What is grounding?",
                             description="**Grounding** is a coping mechanism designed to bring you back to/connect you with reality, or the 'here-and-now'. For example, it can involve the five senses to 'ground' you in the present, or mental strategies to keep the mind occupied. Grounding is used mainly to cope with flashbacks, anxiety, panic attacks, or dissociation, and you can use these techniques on your own or with the guidance of a loved one or a therapist.")
        await ctx.send(embed=groundingmessage)

    @whatis.command(name="trauma")
    async def whatis_trauma(self, ctx):
        traumamessage = discord.Embed(title="What is trauma?",
                                      description="""**Trauma** can be defined as a psychological damage and subsequent response to witnessing or being part of an extremely distressing event, such as being a victim of abuse or a natural disaster. Trauma can lead to the development of Post-Traumatic Stress Disorder (PTSD), or Complex Post-Traumatic Stress Disorder (C-PTSD) in the case of repeated/continuous trauma.""")
        await ctx.send(embed=traumamessage)

    @whatis.command(name="abuse")
    async def whatis_abuse(self, ctx):
        abusemessage = discord.Embed(title="What is abuse?", description="""**Abuse** is a form of maltreatment (usually a pattern of behavior rather than one single incident) that causes harm to another person. Though opinions on whether it needs to be intentional in order to be called abuse, it is certain that abusive or toxic behavior can also be unintentional, meaning an abuser can genuinely think they are doing what is best while actively harming someone else. However, many abusers are perfectly aware of the damage and impact of their actions.
    \nBeing subject to abuse can last months to years on end, and may cause mental health issues, such as PTSD, C-PTSD, mood disorders, anxiety disorders, and more.
    Abuse can take onto many forms, all of which are just as valid as they can all be extremely distressing. Here are some examples of types of abuse.
    \n• **Emotional abuse**: creates psychological pain, usually through a pattern of threats, guilt tripping, manipulation, gaslighting, humiliating, intimidating, having an unpredictable anger, etc.
    • **Emotional or physical neglect**: involves not catering to the psychological, social, or physical needs of another individual (especially of a child, elder, or person with disability) - such as isolating an individual from the outside world, or not providing food or medical treatment.
    • **Physical abuse**: involves hitting an individual in various ways. Examples include kicking, slapping, bruising, pushing, choking.
    • **Sexual abuse**: meaning forcing someone to engage in any type of sexual behavior, sometimes with another individual.
    • **Medical abuse**: undergoing unnecessary and harmful, potentially harmful, or extremely invasive medical treatments/procedures, often at the instigation of a caretaker.
    • **Religious abuse**: using religion as a justification or excuse for any type of abuse.""")
        await ctx.send(embed=abusemessage)

    @whatis.command(name="therapy")
    async def whatis_therapy(self, ctx):
        therapymessage = discord.Embed(title="What is therapy?", description="""**Therapy** consists in working with a mental health professional to manage mental health problems, develop coping or self-care skills, and more. Therapy is a safe, non-judgemental space where you can truly get to know yourself.\n\n
• **Family-focused therapy**, is for family members to understand how family dynamics and individual behavior can affect mental health.
• **Cognitive Behavioral Therapy (CBT)** challenges negative patterns, enhance your problem-solving skills, practice mindfulness, and more. It is most used for mood disorders, PTSD, or anger problems.
• **Dialectical Behavioral Therapy (DBT)** helps with emotional regulation, mindfulness, distress tolerance and other skills. It is most used for personality and mood disorders.
• **Cognitive enhancement therapy (CET)** helps with being aware of social contexts, increase vocational capabilities, better problem-solving skills, and more in people with psychotic or cognitive disorders.
• **Eye movement desensitization reprocessing (EMDR)** is designed to treat symptoms of PTSD, anxiety, or depression. Practitioners use bilateral stimulation on the brain - such as eye movements from left to right - to help the client process trauma memories.
• **Play therapy** (for children) provides younger clients with a caring, confidential environment. It can help with emotional problems, social skills, stress, trauma, etc.
• **Art therapy** uses the creative process to increase self-awareness, express emotions, deal with self-esteem issues and more. No artistic skills required.
• **Pet therapy** or **animal-assisted therapy** involves the client interacting with animals like horses or dogs. Its effects have been observed with people who suffer from depression, PTSD, developmental disorders or anger issues.
\nAlso see: <https://www.psychologytoday.com/us/types-of-therapy>""")
        await ctx.send(embed=therapymessage)

    @whatis.command(name="did")
    async def whatis_did1(self, ctx):
        didosddmessage = discord.Embed(title="What is DID/OSDD-1?", description="""DID or Dissociative Identity Disorder and OSDD-1, or Other Specified Dissociative Disorder are disorders classified in the DSM-5.\n**DID and OSDD-1** were once referred to as “Multiple Personality Disorder” but have since been renamed as a result of research into the nature of the disorder. Individuals with either DID or OSDD often refer to themselves as **systems**.\n\nOne of the most evident symptoms is the presence of multiple dissociated parts of the self that can take executive control of the body/mind of the individual with this disorder.\nThese dissociated parts are commonly referred to as **alters**. Each alter has or can have a different personality, gender, sexuality, and often different skills, opinions, preferences, goals, and wishes.
\nSince these disorders are often misunderstood or not believed, it is not always easy to find professionals for the treatment of DID/OSDD. Ideally, one should look for a specialist, but in any case, treatment for PTSD or comorbid disorders can also be of great help.
\nIf you wish to learn more, visit: <https://docs.google.com/document/d/1DsVbowMk1ROeEOvZ7UoAaoEk7Y2x0WS2CX33b1tjJog/edit?usp=sharing>""")
        await ctx.send(embed=didosddmessage)

    @whatis.command(name="osdd")
    async def whatis_osdd1(self, ctx):
        didosddmessage = discord.Embed(title="What is DID/OSDD-1?", description="""DID or Dissociative Identity Disorder and OSDD-1, or Other Specified Dissociative Disorder are disorders classified in the DSM-5.\n**DID and OSDD-1** were once referred to as “Multiple Personality Disorder” but have since been renamed as a result of research into the nature of the disorder. Individuals with either DID or OSDD often refer to themselves as **systems**.\n\nOne of the most evident symptoms is the presence of multiple dissociated parts of the self that can take executive control of the body/mind of the individual with this disorder.\nThese dissociated parts are commonly referred to as **alters**. Each alter has or can have a different personality, gender, sexuality, and often different skills, opinions, preferences, goals, and wishes.
\nSince these disorders are often misunderstood or not believed, it is not always easy to find professionals for the treatment of DID/OSDD. Ideally, one should look for a specialist, but in any case, treatment for PTSD or comorbid disorders can also be of great help.
\nIf you wish to learn more, visit: <https://docs.google.com/document/d/1DsVbowMk1ROeEOvZ7UoAaoEk7Y2x0WS2CX33b1tjJog/edit?usp=sharing>""")
        await ctx.send(embed=didosddmessage)

    @whatis.command(name="dsm")
    async def whatis_dsm(self, ctx):
        dsmmessage = discord.Embed(title="What is the DSM?",
                                   description="""The **Diagnostic and Statistical Manual of Mental Disorders (DSM)** is used by clinicians and psychiatrists to diagnose psychiatric illnesses. Its latest version (DSM-5) was released in 2013 and is used worldwide.""")
        await ctx.send(embed=dsmmessage)

    @whatis.command(name="icd")
    async def whatis_icd(self, ctx):
        icdmessage = discord.Embed(title="What is the ICD?",
                                   description="""The **International Statistical Classification of Diseases and Related Health Problems (ICD)** is a manual for the identification of health trends and statistics globally, and the international standard for reporting diseases and health conditions (including mental health disorders). It is the diagnostic classification standard for all clinical and research purposes. The latest version (ICD-11) was released in 2018 and is currently used worldwide.""")
        await ctx.send(embed=icdmessage)

    @whatis.command(name="schizophrenia")
    async def whatis_schizophrenia(self, ctx):
        schizophreniamessage = discord.Embed(title="What is schizophrenia?", description="""**Schizophrenia** is a chronic and severe mental disorder that affects how a person thinks, feels, and behaves. People with schizophrenia may seem like they have lost touch with reality. Symptoms include: delusions, hallucinations, trouble with thinking and concentration, difficulty feeling or expressing emotions, lack of motivation, and more.\n
While there is no cure for schizophrenia, research is leading to more advanced treatments. Researches also are unraveling its causes studying genetics and the brain’s structure and functions. These promising approaches make us hope for more effective therapies soon. Medication and talking therapy, such as cognitive-behavioral therapy (CBT), cognitive enhancement therapy (CET) and others are usually recommended.""")
        await ctx.send(embed=schizophreniamessage)

    @whatis.command(name="depression")
    async def whatis_depression(self, ctx):
        depressionmessage = discord.Embed(title="What is depression?", description="""**Depression** is often an umbrella term for a variety of **mood disorders**, including major depressive mood disorder, post-partum depression, seasonal affective disorder, etc.
\nThe common features of all these disorders can be mild to severe and include: loss of interest or pleasure in activities one usually enjoy(ed), negative thoughts about oneself, suicidal or self-harming tendencies or thoughts, difficulty concentrating, trouble maintaining a healthy sleep schedule, and more.
Fortunately, depression is farily easily treatable compared to other disorders. Usually, people with a mood disorder can find relief in talking therapy (such as dialectical-behavioral therapy (DBT), cognitive behavioral therapy (CBT), etc.), art therapy, medications, and other types of therapy/treatments.""")
        await ctx.send(embed=depressionmessage)

    @whatis.command(name="anxiety")
    async def whatis_anxiety(self, ctx):
        anxietymessage = discord.Embed(title="What is anxiety?", description="""**Anxiety** is often an umbrella term for disorders such as generalized anxiety disorder, panic disorder, or social anxiety disorder, or can be seen as a symptom that accompanies other disorders. Keep in mind everyone experiences anxiety from time to time, so it only becomes worrisome when it's so strong or frequent that it prevents you from living your life to the fullest or causes significant distress.
\nCommon symptoms of anxiety include: an accelerated heartbeat, excessive sweating, panic, uneasiness, stomach problems, trouble sleeping, hyperventilation, numbness, and more.
\nAnxiety disorders are treatable and generally psychotherapy and/or medication is what works best. Cognitive-behavioral therapy (CBT) is an example of a specific kind of therapy that can help with anxiety disorders.""")
        await ctx.send(embed=anxietymessage)

    @whatis.command(name="bipolar")
    async def whatis_bipolar(self, ctx):
        bipolarmessage = discord.Embed(title="What is bipolar disorder?", description="""**Bipolar disorder** is a mental health disorder that causes unusual and extreme shifts in mood, energy, activity levels, and productivity.
\nIndividuals with bipolar disorder may experience:
- **manic episodes**, which means they might feel very jumpy, restless and irritable, they may want to do dangerous things, feel like being super productive at the expense of their own health, and more
- **hypomanic episodes**, during which they may feel very good, be highly productive, and function well. The person may not feel that anything is wrong, but loved ones may recognize the mood swings and changes.
- **depressive episodes**, which make the person feel depressed, empty, hopeless, have trouble sleeping, think about self-harm, and other depressive symptoms.
\nThere are four types of bipolar disorder: Bipolar I, defined by manic, depressive, and mixed episodes; Bipolar II, defined by hypomanic and depressive episodes; cyclothymia, defined by hypomanic and depressive episodes which however do not meet the requirements for Bipolar II; and Other Specified and Unspecified Bipolar and Related Disorders, defined by bipolar disorder symptoms that do not match the three categories listed above.
\nAn effective treatment plan for bipolar disorder usually includes both medication and psychotherapy, such as cognitive-behavioral therapy (CBT) or interpersonal therapy.""")
        await ctx.send(embed=bipolarmessage)

    @whatis.command(name="ptsd")
    async def whatis_ptsd1(self, ctx):
        ptsdmessage = discord.Embed(title="What is PTSD?", description="""**Post-traumatic stress disorder** is a mental health disorder that one may develop after experiencing or witnessing a traumatic event.
\nSymptoms include: flashbacks, nightmares about the trauma, avoidance of reminders of the traumatic event, negative changes in beliefs about oneself/others/the world, and more. PTSD is often associated with co-morbid conditions and problems, such as suicidal tendencies, anxiety disorders, eating disorders, substance abuse and more.
\nPTSD is treatable and the sooner one intervenes, the better. Trauma-focused therapies, such as Eye Movement Desensitization and Reprocessing (EMDR), Cognitive Processing Therapy (CPT), or exposure therapy, and more, as well as meds, can be used to heal.""")
        await ctx.send(embed=ptsdmessage)

    @whatis.command(name="PTSD")
    async def whatis_ptsd2(self, ctx):
        ptsdmessage = discord.Embed(title="What is PTSD?", description="""**Post-traumatic stress disorder** is a mental health disorder that one may develop after experiencing or witnessing a traumatic event.
\nSymptoms include: flashbacks, nightmares about the trauma, avoidance of reminders of the traumatic event, negative changes in beliefs about oneself/others/the world, and more. PTSD is often associated with co-morbid conditions and problems, such as suicidal tendencies, anxiety disorders, eating disorders, substance abuse and more.
\nPTSD is treatable and the sooner one intervenes, the better. Trauma-focused therapies, such as Eye Movement Desensitization and Reprocessing (EMDR), Cognitive Processing Therapy (CPT), or exposure therapy, and more, as well as meds, can be used to heal.""")
        await ctx.send(embed=ptsdmessage)

    @whatis.command(name="cptsd")
    async def whatis_cptsd1(self, ctx):
        ptsdmessage = discord.Embed(title="What is C-PTSD?", description="""**Complex Post-traumatic stress disorder** is a mental health disorder that one may develop after experiencing or witnessing an ongoing traumatic event that is perceived as extremely threatening or horrific, and from which escape is impossible (or very difficult).
The difference from PTSD is that complex trauma is ongoing, often (but not necessarily) starting in childhood years.
\nSymptoms include the same as PTSD, with the addition of difficulties with emotional regulation, negative self-concept, interpersonal disturbances such as being unable to feel close to others, and more. C-PTSD is often associated with co-morbid conditions and problems, such as suicidal tendencies, anxiety disorders, eating disorders, substance abuse and more.
\nC-PTSD is treatable and the sooner one intervenes, the better. Trauma-focused therapies, such as Eye Movement Desensitization and Reprocessing (EMDR), Cognitive Processing Therapy (CPT), or exposure therapy, and more, as well as meds, can be used to heal.""")
        await ctx.send(embed=ptsdmessage)

    @whatis.command(name="c-ptsd")
    async def whatis_cptsd2(self, ctx):
        cptsdmessage = discord.Embed(title="What is C-PTSD?", description="""**Complex Post-traumatic stress disorder** is a mental health disorder that one may develop after experiencing or witnessing an ongoing traumatic event that is perceived as extremely threatening or horrific, and from which escape is impossible (or very difficult).
    The difference from PTSD is that complex trauma is ongoing, often (but not necessarily) starting in childhood years.
    \nSymptoms include the same as PTSD, with the addition of difficulties with emotional regulation, negative self-concept, interpersonal disturbances such as being unable to feel close to others, and more. C-PTSD is often associated with co-morbid conditions and problems, such as suicidal tendencies, anxiety disorders, eating disorders, substance abuse and more.
    \nC-PTSD is treatable and the sooner one intervenes, the better. Trauma-focused therapies, such as Eye Movement Desensitization and Reprocessing (EMDR), Cognitive Processing Therapy (CPT), or exposure therapy, and more, as well as meds, can be used to heal.""")
        await ctx.send(embed=cptsdmessage)

    @whatis.command(name="C-PTSD")
    async def whatis_cptsd3(self, ctx):
        cptsdmessage = discord.Embed(title="What is C-PTSD?", description="""**Complex Post-traumatic stress disorder** is a mental health disorder that one may develop after experiencing or witnessing an ongoing traumatic event that is perceived as extremely threatening or horrific, and from which escape is impossible (or very difficult).
    The difference from PTSD is that complex trauma is ongoing, often (but not necessarily) starting in childhood years.
    \nSymptoms include the same as PTSD, with the addition of difficulties with emotional regulation, negative self-concept, interpersonal disturbances such as being unable to feel close to others, and more. C-PTSD is often associated with co-morbid conditions and problems, such as suicidal tendencies, anxiety disorders, eating disorders, substance abuse and more.
    \nC-PTSD is treatable and the sooner one intervenes, the better. Trauma-focused therapies, such as Eye Movement Desensitization and Reprocessing (EMDR), Cognitive Processing Therapy (CPT), or exposure therapy, and more, as well as meds, can be used to heal.""")
        await ctx.send(embed=cptsdmessage)

    @whatis.command(name="CPTSD")
    async def whatis_cptsd4(self, ctx):
        cptsdmessage = discord.Embed(title="What is C-PTSD?", description="""**Complex Post-traumatic stress disorder** is a mental health disorder that one may develop after experiencing or witnessing an ongoing traumatic event that is perceived as extremely threatening or horrific, and from which escape is impossible (or very difficult).
    The difference from PTSD is that complex trauma is ongoing, often (but not necessarily) starting in childhood years.
    \nSymptoms include the same as PTSD, with the addition of difficulties with emotional regulation, negative self-concept, interpersonal disturbances such as being unable to feel close to others, and more. C-PTSD is often associated with co-morbid conditions and problems, such as suicidal tendencies, anxiety disorders, eating disorders, substance abuse and more.
    \nC-PTSD is treatable and the sooner one intervenes, the better. Trauma-focused therapies, such as Eye Movement Desensitization and Reprocessing (EMDR), Cognitive Processing Therapy (CPT), or exposure therapy, and more, as well as meds, can be used to heal.""")
        await ctx.send(embed=cptsdmessage)

    @whatis.command(name="therapist")
    async def whatis_therapist(self, ctx):
        therapistmessage = discord.Embed(title="Who is a therapist?",
                                         description="""The word **therapist** is an umbrella term for professionals who are trained (and/or licensed) to provide a variety of treatments, rehabilitation and support to people.\nExamples include psychologists, LMFT's, social workers, etc.""")
        await ctx.send(embed=therapistmessage)

    @whatis.command(name="psychologist")
    async def whatis_psychologist(self, ctx):
        psychologistmessage = discord.Embed(title="Who is a psychologist?",
                                            description="""A **psychologist** is a doctor who can diagnose mental disorders, do testings and assessments, and provide treatment plans to patients.""")
        await ctx.send(embed=psychologistmessage)

    @whatis.command(name="counsellor")
    async def whatis_counsellor(self, ctx):
        counsellormessage = discord.Embed(title="Who is a counsellor?", description="""The term **counsellor** is rather vague and can include a variety of professionals or trained individuals, including life coaches.
\nIf you meant a **Mental Health Counsellor (MHC)**, they are a mental health professional who rovides support and guidance along the way, for example, when you feel stressed because of whatever reason and need additional support in your life. A MHC could work in schools, facilities, and other settings and is often low-cost or free. Some MHC's are trained in a specific area, such as substance abuse or youth. However, they cannot diagnose or provide more in-depth treatment plans.
\nIf you meant **Licensed Professional Counsellor (LPC)** (also known as Licensed Clinical Professional Counsellor or Licensed Mental Health Counsellor), these professionals work with families, individuals, and groups for a variety of problems, similar to a MHC. However, they have more training than MHC's and can provide diagnoses and treatment plans.""")
        await ctx.send(embed=counsellormessage)

    @whatis.command(name="psychiatrist")
    async def whatis_psychiatrist(self, ctx):
        psychiatristmessage = discord.Embed(title="Who is a psychiatrist?",
                                            description="""A **psychiatrist** is a medical doctor who can offer assessments, testings, talking therapy and other types of treatment. Usually, they work along with other mental health professionals to decide what kind of meds to prescribe to a client. They may also be researchers.""")
        await ctx.send(embed=psychiatristmessage)

    @commands.command()
    async def emergency(self, ctx):
        messagetosend = discord.Embed(title="Emergency",
                                      description="If anyone you know is in any kind of emergency, please visit the following page:\nhttps://sunrayresources.tumblr.com/urgenthelp\nI suggest you also try the `tbs!livesupport` and `tbs!therapy` commands.",
                                      colour=0x082E6F)
        await ctx.send(embed=messagetosend)

    @commands.command(aliases=['positive'])
    async def positivity(self, ctx):
        pos = random.choice([
            "Hey there, here's your daily nice gif.\nhttps://giphy.com/gifs/studiosoriginals-domitille-collardey-l41Yh1olOKd1Tgbw4",
            "Hey there, here's your daily nice gif. (source: teenypinkbunny)\nhttps://78.media.tumblr.com/8b468c1f9c20ca5f9483da6753460ec2/tumblr_onfpirBibx1tyggbco1_1280.gif",
            "Hey there, here's your daily nice gif.\nhttps://giphy.com/gifs/chuber-turtle-hang-in-there-l1J3zw3sgJ6Ye6I4E",
            "Hey there, here's your daily nice gif.\nhttps://78.media.tumblr.com/c0a1ffdef8c5b710769595cdf1119356/tumblr_on4s1k5Gru1w7ymkuo1_500.gif",
            "Hey there, here's your daily nice gif. (source: fuwaprince)\nhttps://78.media.tumblr.com/8317376ec2f138b962d7dec63d479c46/tumblr_os6c25dzp21w4zse0o1_r1_500.gif",
            "Hey there, here's your daily nice gif. (source: gogh-save-the-bees)\nhttps://78.media.tumblr.com/a92282dfc57d01e2e29184e3ed12fa5d/tumblr_otngozhihv1ut0lfho1_400.gif",
            "Hey there, here's your daily nice gif.\nhttps://78.media.tumblr.com/7ba86c4cbc0b0f8fc981ca780fe8bb61/tumblr_osdkc2EJZL1w4zse0o1_1280.gif",
            "Hey there, here's your daily nice gif. (source: positiveupwardspiral)\nhttps://78.media.tumblr.com/3914e99610371d427989d5146c42b85e/tumblr_p0981oKsrJ1vimk88o1_400.gif",
            "Hey there, here's your daily nice gif. (source: fuwaprince)\nhttps://78.media.tumblr.com/2bbe256eba6d07ea6df9698dd20dfa65/tumblr_ot4afrYG181w4zse0o1_500.gif",
            "Hey there, here's your daily nice gif. (source: fuwaprince)\nhttps://78.media.tumblr.com/6acf4ed92328f675ae8890df51b23794/tumblr_os27xwOzXz1w4zse0o1_500.gif",
            "Hey there, here's your daily nice gif. (source: vanish)\nhttps://78.media.tumblr.com/ca9372839569a8406c0709bcc50a15ec/tumblr_p2iebnGUZr1sga7ujo1_500.gif",
            "Hey there, here's your daily nice gif.\nhttps://78.media.tumblr.com/e0e093271b5657b75000f693bb48d877/tumblr_opy7xzfkJS1tssyz8o1_500.gif",
            "Hey there, here's your daily nice gif. (source: positiveupwardspiral)\nhttps://78.media.tumblr.com/91fbd29211a1c7b06e7a16adf2deae50/tumblr_ozl7ooyZxQ1vimk88o1_400.gif",
            "Hey there, here's your daily nice gif. (source: positiveupwardspiral)\nhttps://78.media.tumblr.com/dd5e45b3690ac2e979bc694ea473cf0b/tumblr_oyo1zfEii61vimk88o1_400.gif",
            "Hey there, here's your daily nice gif. (source: gogh-save-the-bees)\nhttps://78.media.tumblr.com/4b8c9b079cd3da2d74275d3063d83b72/tumblr_oxidf7tQjz1ut0lfho1_500.gif",
            "Hey there, here's your daily nice gif. (source: magical-latte)\nhttps://78.media.tumblr.com/d2fa0d7d4ca67af23750bb79a674d5c2/tumblr_p67f6ugJp91x69labo1_500.gif",
            "Hey there, here's your daily nice gif.\nhttps://78.media.tumblr.com/85efdd7380284bd7279a0839e9674f96/tumblr_oqish5aNqX1ufccs2o1_500.gif",
            "Hey there, here's your daily nice gif. (source: faiemagick)\nhttps://78.media.tumblr.com/bf7cad140e3e113cd4062b0377842ca3/tumblr_otogrpArAo1wo3hpco1_1280.gif",
            "Hey there, here's your daily nice gif.\nhttps://giphy.com/gifs/studiosoriginals-domitille-collardey-l41Yh1olOKd1Tgbw4",
            "Hey there, here's your daily nice gif.\nhttps://giphy.com/gifs/help-motivation-positivity-l4pT49ce47qFBdVT2",
            "Hey there, here's your daily nice gif.\nhttps://giphy.com/gifs/art-animation-illustration-l3q2A6Jn9uo2262pW",
            "Hey there, here's your daily nice gif.\nhttps://giphy.com/gifs/positive-tEXeL9FRm6PAI",
            "Hey there, here's your daily nice gif.\nhttps://giphy.com/gifs/destressmonday-destress-red-balloon-3og0IPjBrpAto5yJEs",
            "Hey there, here's your daily nice gif.\nhttps://giphy.com/gifs/quotes-calm-keep-RLgIrDgrPMWdy",
            "Hey there, here's your daily nice gif.\nhttps://cdn.discordapp.com/attachments/369922094223458304/515313193221095446/75e10739-245a-42c6-8798-7cdaa90201e2.png",
            "Hey there, here's your daily nice gif.\nhttps://cdn.discordapp.com/attachments/369922094223458304/509975106827583488/image0.gif",
            "Hey there, here's your daily nice gif.\nhttps://cdn.discordapp.com/attachments/369922094223458304/509813104079536214/16ca4131-7d19-4d6b-b4bc-18a214fac2e7.gif",
            "Hey there, here's your daily nice pic.\nhttps://78.media.tumblr.com/fe6d11172e5e213d1147424768fbaab6/tumblr_pdxyn6zlhz1w73ry4o1_500.jpg",
            "Hey there, here's your daily nice pic.\nhttps://78.media.tumblr.com/ed8e14743dac29bbc606fc099ab77ec3/tumblr_nphyqvqGvi1qzz08do1_500.jpg",
            "Hey there, here's your daily nice pic. (source unknown)\nhttps://78.media.tumblr.com/ef9c6dcfdf0aa540d7a0a84924a626e8/tumblr_mn6lzcds6O1renyrao1_500.png",
            "Hey there, here's your daily nice pic. (source: harmony-is-happiness)\nhttps://78.media.tumblr.com/161afec870afde45359b602edfad5c3e/tumblr_ooxwrrNwhZ1w36xb2o8_r3_250.jpg",
            "Hey there, here's your daily nice pic. (source: harmony-is-happiness)\nhttps://78.media.tumblr.com/6602114029258f4097fffc33a2ae5887/tumblr_otfj86Xgq91wssyrbo1_r4_250.jpg"
        ])
        await ctx.send(pos)

    @commands.command(aliases=['breathing', 'calm', 'anxious', 'breathe'])
    async def anxiety(self, ctx):
        image = random.choice([
            "Hello there, here's a gif for a breathing exercise.\nhttps://media.giphy.com/media/3oxQNhjjZKLPs26Mve/giphy.gif",
            "Hello there, here's a gif for a breathing exercise.\nhttps://i.imgur.com/XbH6gP4.gif",
            "Hello there, here's a gif for a breathing exercise.\nhttps://media.giphy.com/media/8YfwmT1T8PsfC/giphy.gif",
            "Hello there, here's a gif for a breathing exercise.\nhttp://karlolabs.com/wp-content/uploads/2017/01/breathing.gif",
            "Hello there, here's a gif for a breathing exercise.\nhttp://i67.tinypic.com/2qant76.gif",
            "Hello there, here's a gif for a breathing exercise.\nhttps://giphy.com/gifs/monday-destress-3o7WTp5nxyRqh6T21O",
            "Hello there, here's a gif for a breathing exercise.\nhttps://giphy.com/gifs/monday-destress-l0NhWtOfbVze6KzFm",
            "Hello there, here's a gif for a breathing exercise.\nhttps://giphy.com/gifs/monday-destress-xThuWwbtRvTFh7fjxu",
            "Hello there, here's a gif for a breathing exercise.\nhttps://giphy.com/gifs/monday-destress-xThuWqxgKOhbutFyCY",
            "Hello there, here's a gif for a breathing exercise.\nhttps://giphy.com/gifs/monday-destress-xThuWkfIpGNrUnhu9O",
            "Hello there, here's a gif for a breathing exercise.\nhttps://giphy.com/gifs/destressmonday-relax-meditation-l1J9MS2Ia617Kky3u",
            "Hello there, here's a gif for a breathing exercise.\nhttps://giphy.com/gifs/meditation-mAsGwBc4pZGYE",
            "Hello there, here's a gif for a breathing exercise.\nhttps://giphy.com/gifs/square-ZwuBxuIHhIkXm",
            "Hello there, here's a gif for a breathing exercise.\nhttps://giphy.com/gifs/yoga-air-relax-3o7aD2T6zL8bKIt2tq",
            "Hello there, here's a gif for a breathing exercise.\nhttps://giphy.com/gifs/meditation-NwzYTVWay9T6o",
            "Hello there, here's a gif for a breathing exercise.\nhttps://media.boingboing.net/wp-content/uploads/2016/11/tumblr_og31bxrtOn1qls18ho6_400.gif"
        ])
        await ctx.send(image)

    @commands.command(aliases=['ground', 'dissociation', 'panic', 'flashbacks', 'flashback'])
    async def grounding(self, ctx):
        ground = random.choice([
            'Hey there, here are a few ideas to ground yourself.\nThese can be useful for dissociation, anxiety, panic attacks, and flashbacks. You can try one, a few, or all of them.\n    - Choose a letter of the alphabet and try and come up with as many examples of a category you choose as you can. For example, animals that start with D: dog, deer, dingo, donkey, etc. Or vegetables that start with C: cucumber, cauliflower, celery, etc.\n    - Count backwards from 100 by 3s, 6s, or 7s.\n    - Describe an every day event or process in great detail, listing all of the steps in order and as thoroughly as possible (e.g., how to cook a meal)\n    - Say or think to yourself: "My name is (...). I am safe right now. I am (...) years old and currently at (place). The date is (...). If I need help, I can contact (...). Everything is going to be alright, I can handle this."\n    - Name five things that you see, four that you can touch, three that you hear, and two that you smell or taste, and then one thing that you like about yourself.\n    - Try this link <https://www.healthyplace.com/blogs/treatinganxiety/2010/09/top-21-anxiety-grounding-techniques/> or <http://did-research.org/treatment/grounding.html> for more.',
            "Hey there, here are a few ideas to ground yourself.\nThese can be useful for dissociation, anxiety, panic attacks, and flashbacks. You can try one, a few, or all of them.\n    - Touch and hold objects around you. Compare the feel, weight, temperature, textures, colors, and materials, describe them to yourself.\n    - Squeeze a pillow, stuffed animal, or rubber ball, touch sandpaper (gently), sponges, denim, pop bubble wrap, rip up paper, run lukewarm water on your hands or splash your face with it (be careful).\n    - Picture yourself breathing in relaxation/positive feelings/strength and breathing out negativity. You can also imagine you're breathing in soothing colors (blue, purple, green) and out intense colors (red, black).\n    - Put your feet on the floor, gently squeeze or rub your legs and sit upright. 'Push' with your feet, almost as if you wanted to stand up, but do *not* stand up. Notice how your muscles work and how your body tenses.\n    - If possible, crack a window and notice the cold air, the new sounds, and all the smells. Describe them to yourself.\n    - Try this link <https://www.healthyplace.com/blogs/treatinganxiety/2010/09/top-21-anxiety-grounding-techniques/> or <http://did-research.org/treatment/grounding.html> for more.",
            'Hey there, here are a few ideas to ground yourself.\nThese can be useful for dissociation, anxiety, panic attacks, and flashbacks. You can try one, a few, or all of them.\n    - Ask a friend for a reality-test. If you aren’t sure if something you’re feeling, seeing, hearing or thinking is real, ask a safe friend to help you decide what is fact, what is fiction, what is a flashback, and so on.\n    - Do a few jumping jacks, sit-ups, or push-ups.\n    - Try counting by 3\'s or 7\'s up to 200, then try multiplying by them.\n    - Play with a tangle or a fidget cube. (Fidget spinners are not recommended!)\n    - Remind yourself that extreme emotions, panic/anxiety attacks, flashbacks, or dissociation will go away just as they came. They cannot "hurt" you.\n    - Try this link <https://www.healthyplace.com/blogs/treatinganxiety/2010/09/top-21-anxiety-grounding-techniques/> or <http://did-research.org/treatment/grounding.html> for more.'
        ])
        await ctx.send(ground)

    @commands.command(aliases=['getlivehelp', 'getlivesupport'])
    async def livesupport(self, ctx):
        websites = discord.Embed(title="Live Support Online",
                                 description="If you need advice/help or to vent, here are some links for you. These include mainly live chats with volounteers and other websites that offer peer-support.\n<http://www.yourlifeyourvoice.org/Pages/ways-to-get-help.aspx>\n<https://www.7cups.com>\n<https://mellowtalk.com/>\n<http://blahtherapy.com/chat-hub/>\n<https://www.vetsprevail.org/> (For veterans)\n<https://ginger.io/>\n<https://kooth.com/>\n<https://www.iprevail.com/>\n<https://www.imalive.org/>\n<https://www.reddit.com/r/KindVoice/>",
                                 colour=0x082E6F)
        await ctx.send(embed=websites)

    @commands.command(aliases=['cheaptherapy', 'lowcosttherapy', 'onlinetherapy'])
    async def freetherapy(self, ctx):
        websites = discord.Embed(title="Low-Cost Therapy",
                                 description="It's possible to get low-cost or free therapy in various ways! Visit this link for more info and tips: <https://sunrayresources.tumblr.com/therapy>.\n\nHere are some places to get free or low-cost professional help, online or otherwise.\nWe also recommend you try the `tbs!database` command.\n\n<https://mindspot.org.au/>\n<https://inpathy.com/>\n<https://www.counsellingonline.org.au/>\n<https://cimhs.com/>\n<https://www.iprevail.com>\n<http://www.yourlifeyourvoice.org/Pages/ways-to-get-help.aspx>\n<https://www.talkspace.com/>\n<http://blahtherapy.com/>\n<https://onlinecounselling.io/>\n<https://www.betterhelp.com/>\n<https://www.iprevail.com/>",
                                 colour=0x082E6F)
        await ctx.send(embed=websites)

    @commands.command(
        aliases=['counsellor', 'therapist', 'therapymenu', 'counselling', 'support', 'gethelp', 'getsupport'])
    async def therapy(self, ctx):
        messagetosend = discord.Embed(title='Commands', description="""Hello! So you need some kind of support? Great, you are in the right place.\nWhat are you looking for?\n
:one: If you are looking for low-cost or free therapy do `tbs!freetherapy`.\n\n :two: If you're looking for therapist databases, do `tbs!database`.\n\n :three: If you're looking for live support, do `tbs!livesupport`.""",
                                      colour=0x082E6F)
        messagetosend.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/369960338436915210/479411887583395850/Embrace-nowledge.png")
        await ctx.send(embed=messagetosend)

    @commands.command(aliases=['therapydatabase', 'databasetherapy'])
    async def database(self, ctx):
        websites = discord.Embed(title="Type 'next' to go to next page.",
                                 description="If you are experiencing mental health problems that cause distress in your life, you may need to consider seeking proper support from a professional or someone who’s trained to help you in the best way possible. Peer-support, while different, is also an essential part of your recovery, so you might wish to look into that, too.\n\nAlso try `tbs!livesupport` and `tbs!cheaptherapy`.",
                                 colour=0x082E6F)
        websites.add_field(name="International/Multiple countries",
                           value="<https://members.nielasher.com/>\n<https://www.therapistlocator.net//imis15/tl/Default.aspx>\n<https://www.therapytribe.com/>\n<https://www.therapytribe.com/>\n<http://www.istss.org/find-a-clinician.aspx>\n<https://www.onlinecounselling.com/therapist-finder/>\n<https://www.goodtherapy.org/international-search.html>",
                           inline=False)
        websites.add_field(name="Canada and USA",
                           value="<https://help.recoverywarriors.com/>\n<https://www.sidran.org/help-desk/get-help/>\n<https://www.networktherapy.com/directory/find_therapist.asp>\n<https://members.adaa.org/page/FATMain>\n<https://www.theravive.com/zip/>\n<https://www.psychologytoday.com/us/therapists/>\n<http://www.findcbt.org/xFAT/index.cfm>\n<http://www.isst-d.org/default.asp?contentID=18>\n\nAdditionally, check **this page**, which is always up-to-date and has more resources for you:\n\n<https://sunrayresources.tumblr.com/resources>",
                           inline=False)
        websites.set_footer(text="(Page 1/2) Type 'next' to go to next page.")
        embedone = await ctx.send(embed=websites)

        websites2 = discord.Embed(
            description="If you are experiencing mental health problems that cause distress in your life, you may need to consider seeking proper support from a professional or someone who’s trained to help you in the best way possible. Peer-support, while different, is also an essential part of your recovery, so you might wish to look into that, too.\n\nAlso try `tbs!livesupport` and `tbs!cheaptherapy`.",
            colour=0x082E6F)
        websites2.add_field(name="UK",
                            value="<https://bpdworld.org/specialist/> (Various services)\<https://www.bps.org.uk/public/find-psychologist>\n<http://www.cmha.org.uk/>\n<https://www.psychologytoday.com/gb/counselling>\n<http://www.callhelpline.org.uk/Help.asp#search>\n<https://www.psychotherapy.org.uk/find-a-therapist/>\n<https://www.bacp.co.uk/search/Therapists>\n<https://www.nhs.uk/Service-Search/Psychological%20therapies%20(IAPT)/LocationSearch/10008>")
        websites2.add_field(name="Australia",
                            value="<https://www.1800respect.org.au/services/>\n<http://www.oneinthree.com.au/servicesandresources/>\n<https://lysnhealth.com.au/>\n<https://www.psychology.org.au/Find-a-Psychologist>\n\n Additionally, check **this page**, which is always up-to-date and has more resources for you:\n\n <https://sunrayresources.tumblr.com/resources>")
        websites2.set_footer(text="(Page 2/2)")

        def check(a):
            return a.content == "next"

        try:
            await bot.wait_for("message", timeout=60.0, check=check)
            await embedone.edit(embed=websites2)

        except asyncio.TimeoutError:
            return await ctx.send('Sorry, command timed out!')


class Fun():

    @commands.command(aliases=['coin', 'flip', 'flipcoin'])
    async def coinflip(self, ctx):
        choices = random.choice(['Heads!', 'Tails!'])
        await ctx.send(choices)

    @commands.command(aliases=['say', 'talk'])
    async def echo(self, ctx, *, something):
        error = discord.Embed(
            title='Error!', description="Don't ping with this bot command, thank you.", colour=discord.Colour.red())
        errorm = discord.Embed(
            title='Error!', description='Did you seriously just try to mass-ping? :/', colour=discord.Colour.red())
        messagetosend = '{0.author} just tried to mass-ping.'.format(ctx.message)
        if ('@' in ctx.message.content) and ('@someone' not in ctx.message.content):
            await ctx.send(embed=error)
        if '@everyone' in ctx.message.content:
            await ctx.send(embed=errorm)
            await (await bot.get_user_info(345307151989997568)).send(messagetosend)
        if ('@' not in ctx.message.content) or ('@someone' in ctx.message.content):
            await ctx.send(something)

    @commands.command(aliases=['hug', 'hugs', 'givehugs'])
    async def givehug(self, ctx):
        botmention = discord.Embed(description="T-thank you! I feel so loved now >///<", colour=0x082E6F)
        botmention.set_thumbnail(
            url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif")
        normalmention = discord.Embed(description="Aw, you just received a warm hug!", colour=0x082E6F)
        normalmention.set_thumbnail(
            url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif")
        me = discord.Embed(description="All the hugs for you!", colour=0x082E6F)
        me.set_thumbnail(
            url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif")

        if ctx.me.mention in ctx.message.content:
            await ctx.send(embed=botmention)
        elif '@' in ctx.message.content:
            await ctx.send(embed=normalmention)
        elif 'me' in ctx.message.content:
            await ctx.send(embed=me)

    @commands.command(aliases=['randomcompliment'])
    async def compliment(self, ctx):
        randomcomp = random.choice([
            "You're so resourceful.", "You're such a strong person.", 'Your light shines so brightly.',
            'You matter, and a lot.', "You have an incredible talent even if you don't see it.",
            'You are deserving of a hug right now.', "You're more helpful than you realize.", 'You can inspire people.',
            'I bet you do the crossword puzzle in ink.',
            "You're someone's reason to smile, even if you don't realize it.",
            "It's so great to see you're doing your best.", "Your smile can make someone's day.", 'Your ideas matter.',
            'Your feelings matter.', 'Your emotions matter.', 'Your opinions matter.', 'Your needs matter.',
            'Your own vision of the world is unique and interesting.',
            "Even if you were cloned, you'd still be one of a kind. (And the better one between the two.)",
            'You are more unique and wonderful than the smell of a new book.',
            "You're great at being you! No one can replace you - so keep it up.", 'You can get through this.',
            "If you're going through something, remember: this too shall pass.",
            'You deserve to get help if you need it.', 'You - yes you - are valid.', 'You are more than enough.',
            'Your presence is appreciated.', 'You can become whoever you want to be.', 'You deserve to be listened to.',
            'You deserve to be heard.', 'You deserve to be respected.', "You're an absolute bean.",
        ])
        await ctx.send(randomcomp)

    @commands.command(aliases=['comfort', 'comforting'])
    async def comfortme(self, ctx):
        randomcomf = random.choice(
            ["You've always been able to always figure out how to pick yourself up. You can do it again.",
             "It's so great to see you're doing your best.",
             'You can get through this.',
             "If you're going through something, remember: this too shall pass.",
             "If today was bad, remember that you won't have to repeat this day ever again.",
             "Even if you feel like you're getting nowhere you're still one step ahead of yesterday - and that's still progress.",
             "You're growing so much, and if you can't see it now, you certainly will in a few months.",
             "You're strong for going on even when it's so hard.",
             "If you are having really awful thoughts right now or feeling very insecure, remember that what you think does not always reflect the reality of things.",
             "I know they can be hard to deal with, but even a bot like me knows your emotions are valid and important!",
             "(source: softangelita)\nhttps://78.media.tumblr.com/757d6f9eceacd22e585f5763aed3b6b7/tumblr_pbs2drA9yX1wzarogo1_1280.gif",
             "You are going to be okay. Things are going to be okay. You will see.",
             "(source: princess-of-positivity)\nhttps://78.media.tumblr.com/209ac4a784925d71d3d3c7293b7d75f4/tumblr_o883p7C7e21vwxwino1_1280.jpg",
             "Sit down, take a breath. There’s still time. Your past isn’t going anywhere, the present is right here and the future will wait.",
             "It is never too late to make a positive change in your life.",
             "https://78.media.tumblr.com/14a19b1f5c785c0af5966175c0c87c8f/tumblr_owob0dUAzy1ww31y6o1_500.jpg",
             "Don't be upset if you aren't always doing your absolute best every waking moment. Flowers cannot always bloom.",
             "(source: jessabella-hime)\nhttps://78.media.tumblr.com/b1e54721f7520a6f425c112a67170e63/tumblr_ozi5gdM4de1trvty1o1_500.png",
             "There are good people in this world who do or will help you, care about you, and love you.",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/37778dd51384fbdba835349e6f0081d5/tumblr_oz8v11c9CC1wssyrbo1_500.jpg",
             "https://78.media.tumblr.com/ed8e14743dac29bbc606fc099ab77ec3/tumblr_nphyqvqGvi1qzz08do1_500.jpg",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/980109437f848b501d9ac96ed5a9ead0/tumblr_p285yaPKk31wssyrbo2_r2_250.jpg",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/63a7933dfe6ed98dd00682533d249efe/tumblr_pc558poobr1wssyrbo1_250.jpg",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/5827e477fff5b22c693c00d94eb19b2a/tumblr_p40de4xrrC1wssyrbo1_250.jpg",
             "It is perfectly okay to rest and take a break from things If you are taking yourself to exhaustion, at that point it isn't your best anymore.",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/50f06d2360aae36c815b1757326d878d/tumblr_p40de4xrrC1wssyrbo5_r1_250.jpg",
             "Sometimes it's okay if the only thing you did today was breathe.",
             "(source: recovering-and-healing)\nhttps://78.media.tumblr.com/e7b47e53ba372425728f384685748435/tumblr_oc93tmtPBj1ue8qxbo3_r1_250.jpg",
             "(source: positivedoodles)\nhttps://78.media.tumblr.com/c04f396bfd2501b4876c239a329c035b/tumblr_pcutj6i57Z1rpu8e5o1_1280.png",
             "(source: harmony-is-happiness)\nhttps://78.media.tumblr.com/6602114029258f4097fffc33a2ae5887/tumblr_otfj86Xgq91wssyrbo1_r4_250.jpg"])
        await ctx.send(randomcomf)

    @commands.command(aliases=['throwdice', 'dicethrow', 'throw'])
    async def dice(self, ctx):
        throw = random.choice(['1.', '2.', '3.', '4.', '5.', '6.'])
        await ctx.send(throw)

    @commands.command(aliases=['cookie'])
    async def givecookie(self, ctx):
        botmention = discord.Embed(description="Wow, thanks! I love cookies >///<", colour=0x082E6F)
        botmention.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/477948503830560779/479616197143429135/chocochipcookie.png")
        normalmention = discord.Embed(description="Aw, you just gave them a cookie. How sweet of you!", colour=0x082E6F)
        normalmention.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/477948503830560779/479616197143429135/chocochipcookie.png")
        me = discord.Embed(description="There you go. Enjoy your cookie!", colour=0x082E6F)
        me.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/477948503830560779/479616197143429135/chocochipcookie.png")

        if ctx.me.mention in ctx.message.content:
            await ctx.send(embed=botmention)
        elif '@' in ctx.message.content:
            await ctx.send(embed=normalmention)
        elif ('me' in ctx.message.content) or ('Me' in ctx.message.content):
            await ctx.send(embed=me)

    @commands.command(
        aliases=['joke', 'jokes', 'cheesyjoke', 'randomjoke', 'pun', 'randompun', 'cheesypun', 'cornypun', 'puns'])
    async def cornyjoke(self, ctx):
        randomjoke = random.choice([
            'What do you call a thieving alligator? A crookodile.',
            "What did the watermelon say to the cantaloupe? You're one in a melon.",
            'How do you put a baby alien to sleep? You rocket.', 'How do you throw a space party? You planet.',
            'What do you call a bear with no teeth? A gummy-bear.', 'What does a house wear? Address.',
            'Why is it hard to be in a relationship with a thief? Because they always take things... literally.',
            "Why can't a bycycle stand on its own? Because it's two tired.", 'Do french people play videogames? Wii.',
            "Did you hear about the joke about German sausages? It's the wurst.",
            'What does a falling star say to start a fight? Comet me bro.',
            "What did E.T.'s mother say to him when he got home? 'Where on Earth have you been?!'",
            "Why are calendars so popular? They have lots of dates.",
            'Why do musicians always get good grades? They have lots of notes.',
            'What did the traffic light say to the car? Don’t look! I’m about to change.',
            'Why was the little strawberry crying? Its mom was in a jam.',
            'Why are frogs so happy? They eat whatever bugs them.',
            'What do you call a guy with a rubber toe? Roberto.',
            'What do you call a bee that’s having a bad hair day? A frisbee.',
            "Why wouldn't the shrimp share his treasure? Because it was a little shellfish.",
            'If a seagull flies over the sea, what flies over the bay? A bagel.',
            'What happens to deposed kings? They get throne away.',
            'What kind of tree do fingers grow on? A palm tree.', 'What do you call a rabbit with fleas? Bugs Bunny.',
            'What happens to illegally parked frogs? They get toad away.',
            'What do you call a fish with no eyes? A fsh.', 'What do prisoners use to call each other? Cell phones.',
            "What happens when a clock's hungry? It goes back four seconds.",
            'How was Rome split in two? With a pair of Ceasars.',
            'What did the corn say in response to a compliment? Aw, shucks.',
            'What do you tell maize on graduation day? Corn-gratulations.',
            'What do you call a beautiful pumpkin? GOURDgeous.', 'What did the buffalo say to his son? Bison.',
            'What do you call a fake noodle? An impasta.', 'How do trees access the internet? They log on.',
            'What do you call a pirate who sells corn? A buccaneer.',
            'Want to hear a pizza joke? Actually never mind, it’s too cheesy.',
            "Why shouldn't you trust atoms? They make up everything.",
            "What do you call a pile of cats? A meow-ntain.",
            "An Italian chef has died. He pasta way.",
            "What kind of cup can't you drink out of? A cup-cake.",
            """Two antennas met on a roof, fell in love and got married. The ceremony wasn't much, but the reception was excellent.""",
            "An Irishman walks out of a bar.",
            "I was diagnosed with clinical depression the other day... Which made me sad.",
            "I spent five minutes fixing a broken clock yesterday. At least, I *think* it was five minutes...",
            "I once made a belt out of clocks. It was a waist of time.",
            "Learning how to collect trash wasn't hard. I just picked it up as I went along.",
            "What's red and bad for your teeth? A brick.",
            "I'd tell you my construction joke but I'm still working on it.",
            "Why do Norwegians build their own tables? No Ikea!",
            "There's been an explosion at a cheese factory in Paris. There's nothing left but de Brie.",
            "No matter how kind you are, German children are kinder.",
            """I've fallen in love with a pencil and we're getting married. I can't wait to introduce my parents to my bride 2B.""",
            "What did the baby corn say to the mama corn? 'Where is my pop corn?'",
            "Not all math puns are bad. Just sum.",
            "I went to the zoo the other day, there was only one dog in it. It was a shitzu...",
            "RIP boiled water. You will be mist.",
            """- Knock knock.
- Who's there?
- To.
- To who?
- To ***whom***.""",
            "Working in a bank must be awful. I bet it gets loanly in there sometimes."

        ])
        await ctx.send(randomjoke)

    @commands.command(aliases=['ask'])
    async def question(self, ctx):
        quest = random.choice([
            'Yes.', 'No.', 'Yes!', 'No!', 'What? No!', 'Probably not.', 'Maybe...', 'Always.', 'Never.', 'Sometimes...',
            'Almost certainly.', 'I hope not!', "I hope so!", 'Yep!', 'Yes...?', 'No...?', 'Always!', 'Never!',
            'Not sure...',
            'Of course!', 'Of course not!', 'Of course.', 'DUH!', 'Why not?', 'Why though?', "Absolutely not!",
            "Absolutely not.", "Perhaps.", "Who knows..."
        ])
        await ctx.send(quest)
        
    @commands.command(aliases=['sfr', 'spooniefriendlyrecipes'])
    async def spooniefriendlyrecipe(self, ctx):
        recipes = random.choice([
            """**SUPER EASY BANANA & CHOCO ICE CREAM**\n\n__Ingredients:__
A couple ripe bananas (they have to be at least brownish)
(Optional) Milk
(Optional) Cocoa powder, berries, pistachios, chocolate chips... etc\n\n1) Peel off and chop the bananas in small-ish pieces.
2) Put them in the fridge for a couple hours.
3) Put them in the blender, and blend until they have a soft-serve-like consistency. If your blender is having trouble add a bit of milk.
4) You can add cocoa powder, strawberries, chocolate chips, crushed pistachios, aromas or whatever you want!
And you're done!""",
            """**SIMPLE "ITALIAN SOUP"** by megalodont\n\n__Ingredients:__
Can of passata
¼ cup Frozen spinach
A cup of water
Garlic
Pepper
Olive oil
(Optional) Crusty bread
(Optional) Grated parmesan
Some salt (if needed)\n\n1) Chop a bit of garlic in tiny pieces.
2) Heat all ingredients on the stove except pepper and olive oil.
3) When they're hot enough, serve them in bowls and add a bit of pepper and olive oil, and if you want, some parmesan. Excellent to be eaten with crusty bread.
And you're done!""",
            """**EASY ORANGE CHICKEN** by no-more-ramen\n\n__Ingredients:__
Chicken breasts
Sweet orange jam/marmelade
1 cup of bbq sauce
2 tbsp of soy sauce
(Optional) Rice\n\n1) Cube or thinly slice the chicken.
2) Sauté with the orange jam and sauces until thoroughly cooked. 
3) Serve over rice if you have any. 
And you're done! This should be enough for 2-3 people.""",
            """Having guests over? Do they happen to be kids or to have a sweet tooth? 
Try out recipes from this video: https://www.youtube.com/watch?v=8JYNbNYqMTk""",
            """**TWO-INGREDIENTS CAKE** by deadbyday.tv\n\n__Ingredients:__
4 eggs
250 g Nutella
(Optional) A couple teaspoons of baking soda
\n\n1) Use an electric mixer/whipper to whisk the eggs.
2) Mix in the Nutella little by little, it'll be easier if you heat it up a bit beforehand. If you wish, add the baking soda.
3) Pour in a baking pan and let cook for 25 minutes 170° C.
And you're done!""",
            
            """**MACARONI AND CHEESE IN A MUG** by red-starr\n\n__Ingredients:__
Cheese
Butter
Instant noodles
Water
Salt
Milk\n\n1) Take a mug.
2) Take about a handful and a half of some elbow noodles. 
3) Fill mug with water to cover up the noodles and cook in the microwave to get the noodles soft! (5 minutes for my microwave) If you have alot of water, drain it but leave a tiny bit of water.
4) Okay now the fun part! Add cheese (I used sharp cheddar cut into cubes), butter (I used a garlic infused butter, but any butter is fine), a splash of milk, and some salt (I used smoked salt).
5) Cook until its all melted in the microwave! If it looks like soup you can drain a little and add more cheese, cook again make sure it's melted.
6) Let sit for about 2 minutes.
And that's it! You are done and it’s better than any Easy Mac!""",
            """**EASY AND LOW-COST SPICY TOMATO SOUP** by red-starr\n\n__Ingredients:__
1 bay leaf
A small amount of butter
Black pepper
Salt
Garlic powder
Onion powder
½ Can of coconut milk (or an entire can if it's too spicy for you)
1 can of condensed tomato soup
Havarti cheese (You can probably use Swiss cheese as a substitute)
A little Sriracha sauce
1 table spoon of Tikka seasoning
Croutons (topping, optional)\n\n1) Put everything in a pot on the stove and bring to a boil.
2) Let simmer for about fifteen minutes, adding the seasonings a little at a time - taste and make adjustments as you cook.
And you're done!""",
            """**EASY TACO SOUP** by no-more-ramen\n\n__Ingredients:__
1 lb ground beef
2 cans corn
2 cans diced tomatoes
2 cans chili beans
1 packet taco seasoning\n
1) Brown the beef, then put everything else in. 
2) Bring it to a boil. 
And you're done!""",
            """**SIMPLE FANCY TUNA FISH SALAD** by no-more-ramen\n\n__Ingredients for 2-3 servings:__
2 cans of oil packed tuna
1 jar of pesto
pre-sliced black olives
fresh spinach
crunch (I usually use celery, but that requires chopping, so you can add something else or skip this)
bread\n
1) Dump the tuna into a bowl without draining and mush with a fork.
2) Mix in pesto until it’s pretty well coated.  
3) Add in black olives and your crunch.  
3) Serve in a sandwich with a few spinach leaves.
And you're done!""",
            """**EASY and LOW-COST TUNA & WHITE BEAN SALAD** by Budget Bytes\n\n__Ingredients:__
1 5oz can of tuna
1 15oz can of white beans
1 Tbsp olive oil
juice of one lemon
2 whole green onions
salt and pepper to taste
Optional: dash of hot sauce\n
1) Drain the tuna and beans.
2) Put the tuna and beans into a mixing bowl
3) Chop the green onions
4) Add the green onions, lemon juice, olive oil, salt, and pepper to the mixing bowl. Mix to combine.
That’s it!"""
        ])
        await ctx.send(recipes)

    @commands.command(aliases=['randomdessert'])
    async def dessert(self, ctx):
        dessert = random.choice([
            "Here's your random dessert.\nhttps://giphy.com/gifs/animation-illustration-birthday-l0Iy4ppWvwQ4SXPxK",
            "Here's your random dessert.\nhttps://giphy.com/gifs/huffingtonpost-food-cake-dessert-QWS2I0L6UssF2",
            "Here's your random dessert.\nhttps://giphy.com/gifs/cake-food-anime-kfMGD3KwdIrpm",
            "Here's your random dessert.\nhttps://giphy.com/gifs/banana-pkBEq1dfFIT8A",
            "Here's your random dessert.\nhttps://giphy.com/gifs/food-delicious-cupcake-VW5GUg86EaX2E",
            "Here's your random dessert.\nhttps://giphy.com/gifs/shakingfoodgifs-food-kawaii-shaking-qLzDdOe6D483m",
            "Here's your random dessert.\nhttps://giphy.com/gifs/is-reasons-superior-UAzaYopok9PsQ",
            "Here's your random dessert.\nhttps://giphy.com/gifs/is-reasons-superior-oDJss7tbDEzZu",
            "Here's your random dessert.\nhttps://giphy.com/gifs/dessert-rpNkH3RAwkTXW",
            "Here's your random dessert.\nhttps://giphy.com/gifs/cake-dessert-43o1oy5xdOfL2",
            "Here's your random dessert.\nhttps://giphy.com/gifs/is-reasons-superior-E5efe2XtMUdTq",
            "Here's your random dessert.\nhttps://giphy.com/gifs/food-chocolate-dessert-111oCumklJpuJW",
            "Here's your random dessert.\nhttps://giphy.com/gifs/waffles-tDnKZAsxCZHRC",
            "Here's your random dessert.\nhttps://giphy.com/gifs/cake-cute-t0iiGOtn2oMak",
            "Here's your random dessert.\nhttps://giphy.com/gifs/cake-dessert-I8iWotgEu6O4g",
            "Here's your random dessert.\nhttps://giphy.com/gifs/l0HlyXQUez0jHop2g",
            "Here's your random dessert. (credits: therecipepantry)\nhttps://66.media.tumblr.com/61e537f1b6e8f3b3977da83545a1a5b9/tumblr_nlhylywKlY1tbiplio1_500.gif",
            "Here's your random dessert. (credits: khoroshavina)\nhttps://66.media.tumblr.com/a4f73299cae69351735248d138c6b5c8/tumblr_ngrultfmKH1r13qeyo1_500.gif",
            "Here's your random dessert. (credits: butteryplanet)\nhttps://66.media.tumblr.com/8ae304bf8bd727da46fcc84ad064b476/tumblr_p3vxq0icCz1u9ooogo1_500.gif",
            "Here's your random dessert. (credits: butteryplanet)\nhttps://66.media.tumblr.com/9cecff7312ba1fd96878900b7c74f3ff/tumblr_owqx81kdp71u4taepo1_500.gif",
            "Here's your random dessert.\nhttps://giphy.com/gifs/shakingfoodgifs-cookie-food-kawaii-INYRyEM6hPbcQ",
            "Here's your random dessert.\nhttps://giphy.com/gifs/fruit-7z4lmNtTmuREI",
            "Here's your random dessert.\nhttps://giphy.com/gifs/shakingfoodgifs-food-dessert-pie-pdfnRGpNQzePC",
            "Here's your random dessert.\nhttps://giphy.com/gifs/chocolate-cookie-food-4ji2aiquPipy0",
            "Here's your random dessert.\nhttps://giphy.com/gifs/artists-on-tumblr-loop-tx8emQv1s5AtO",
            "Here's your random dessert.\nhttps://giphy.com/gifs/food-gif-gifs-nQxAUnnkBuve0",
            "Here's your random dessert.\nhttps://giphy.com/gifs/custard-pudding-giga-UiYwzaq7GmViM",
            "Here's your random dessert.\nhttps://giphy.com/gifs/layer-creme-brulee-KKcuP3xXzs6pG",
            "Here's your random dessert.\nhttps://giphy.com/gifs/cheddar-food-ice-cream-SbL0eEWeNfQ0cOvrew",
            "Here's your random dessert.\nhttps://giphy.com/gifs/white-dessert-sphere-rczvneQ6Ziwx2",
            "Here's your random dessert.\nhttps://giphy.com/gifs/donut-drool-enchanting-arEGphwGhT7dC",
            "Here's your random dessert.\nhttps://giphy.com/gifs/dessert-ice-cream-food-ApRorrZknEPw4",
            "Here's your random dessert.\nhttps://78.media.tumblr.com/8a9b6cd2404af6c022d95159ea94956c/tumblr_oli85boOtG1tdnbbbo1_500.gif",
            "Here's your random dessert.\nhttps://78.media.tumblr.com/10f81a8d89154b697a71680b7ff6b43b/tumblr_oseeo7E0CQ1uxvvvzo1_500.gif",
            "Here's your random dessert.\nhttps://78.media.tumblr.com/9f4020f7a39d346a67ab38838d74d4c6/tumblr_om96xsl49Z1vj3zbeo1_500.gif"
        ])
        await ctx.send(dessert)


bot.add_cog(Info())
bot.add_cog(Fun())
bot.add_cog(MentalHealth())
bot.run(os.getenv('discord_client_key'))
