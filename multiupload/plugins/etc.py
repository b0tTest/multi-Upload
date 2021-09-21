#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots

import os
import asyncio, random
from config import Config
from telethon import events, Button
from multiupload.fsub import *
from multiupload import anjana

s = ["CAADBAADxgkAAjQF0VL5yl4Td0utTgI",
	"CAADBAADoAsAAv3iYFGE3u_w4y_1zgI",
	"CAADBAADMggAAq0Q0FK1ZIUPLNxGcAI",
	"CAADBAAD7AoAAr8i2VGALarwosnJIgI",
	"CAADBAADrQoAAmzO0VFDq1aGz7rGHgI",
	"CAADBAADbQgAAhI40VH51AABGZuwl74C"]

@anjana.on(events.NewMessage(pattern='^/start'))
async def start(event):
	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(3)
	user_id = event.sender_id
	xx = await event.get_chat()
	if event.is_private and not await check_participant(user_id, f'@{Config.CHNAME}', event):
		return
	else:
		await anjana.send_file(event.chat_id, random.choice(s), reply_to=event)
		await event.reply(f"Hey [{xx.first_name}]({xx.id}),\n I am **MultiUploader** bot which can upload file to many cloud services \n\n**✦ Powered By [MyTestBotZ](https://telegram.me/MyTestBotZ) \n ✦ Made with ♥️ by @OO7ROBot**", buttons=[
				Button.url('💭Channel', 't.me/mytestbotz')
			])


@anjana.on(events.NewMessage(pattern='^/help'))
async def help(event):
	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(3)
	user_id = event.sender_id
	xx = await event.get_chat()
	if event.is_private and not await check_participant(user_id, f'@{Config.CHNAME}', event):
		return
	else:
		helpmsg = '''
⚙ **Help Menu | MultiUpload Bot**

➠** Send me a File or Video
    • Reply with Suitable command**

● `/gofile` - Upload files to GoFile

● `/anonfile` - Upload files to AnonFile

● `/ufile` - Upload files to UFile

● `/bayfiles` - Upload files to BayFiles

● `/tsh` - Upload files to TransferSH

● `/tninja` - Upload files to TmNinja

● `/fileio` - Upload files to FileIO

● `/mixdrop` - Upload files to MixDrop

✦ **Powered By [MyTestBotZ]**(https://telegram.me/MyTestBotZ)
✦ Made with ♥️ by @OO7ROBot'''
		await event.reply(helpmsg, buttons=[
				Button.url('💭 channel', 'telegram.me/MyTestBotZ')
			], link_preview=False)

		
		
#### about ######
@anjana.on(events.NewMessage(pattern='^/about'))
async def about(event):
	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(3)
	user_id = event.sender_id
	xx = await event.get_chat()
	if event.is_private and not await check_participant(user_id, f'@{Config.CHNAME}', event):
		return
	else:
		aboutmsg = '''**
Hey👋, I'm a MultiUploadBot Created for [Him](https://telegram.me/OO7ROBOT)...

● Channel : [MyTestBotZ](https://telegram.me/MyTestBotZ)

● Language : [Python](https://www.python.org/)

● Library : [Pyrogram 1.2.9](https://docs.pyrogram.org/)

● Server : [Heroku](https://Heroku.com)

● Build Version : [Beta V1](https://t.me/Multiuploadbot)

**'''
		await event.reply(aboutmsg, buttons=[
				Button.url('💭 channel', 'telegram.me/MyTestBotZ')
			], link_preview=False)
