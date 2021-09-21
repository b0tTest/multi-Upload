#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots

import asyncio, os, requests, time
from requests import post
from multiupload import anjana
from telethon.sync import events, Button
from multiupload.fsub import *
from multiupload.utils import downloader, humanbytes
from config import Config

@anjana.on(events.NewMessage(pattern='^/tsh'))
async def transfer(event):
	user_id = event.sender_id
	if event.is_private and not await check_participant(user_id, f'@{Config.CHNAME}', event):
		return
	if not event.reply_to_msg_id:
		return await event.edit("Please Reply to File")

	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(2)
	msg = await event.reply("**Processing...**")
	amjana = await event.get_reply_message()


	## LOGGING TO A CHANNEL
	xx = await event.get_chat()
	reqmsg = f'''Req User: [{xx.first_name}](tg://user?id={xx.id})
FileName: {amjana.file.name}
FileSize: {humanbytes(amjana.file.size)}
#TRANSFERSH'''
	await anjana.send_message(Config.LOG_CHANNEL, reqmsg)

	result = await downloader(
		f"downloads/{amjana.file.name}",
		amjana.media.document,
		msg,
		time.time(),
		f"**🏷 Downloading...**\n➲ **File Name:** {amjana.file.name}\n",
	)

	async with anjana.action(event.chat_id, 'document'):
		await msg.edit("Now Uploading to TransferSH")
		url = f"https://transfer.sh/"
		r = post(url, files={'file': open(f'{result.name}','rb')})
	await anjana.action(event.chat_id, 'cancel')

	hmm = f'''**File Uploaded successfully !!
Server: TransferSH**

**⍟ File name:** __{amjana.file.name}__
**⍟ File size:** __{humanbytes(amjana.file.size)}__

NOTE: Files will be deleted after 14 days.'''
	await msg.edit(hmm, buttons=(
		[Button.url('🔗 Download Link', r.text)],
		[Button.url('💭 Update Channel', 't.me/mytestbotz')]
		))

	os.remove(result.name)
