#!/usr/bin/env python3
import time, asyncio, sys, random


from telethon import TelegramClient, events, utils, Button

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'dexter'

bot_id = 'KampungMaifamxBot'
Area = input('Area = ')
Alat = input('Alat = ')

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, Area))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text


            if "Kamu berhasil" in pesan:
                time.sleep(2)
                await event.respond(Area)
                print(pesan)
                return

            elif "Kamu mendapat" in pesan:
                time.sleep(2)
                await event.respond(Area)
                print(pesan)
                return
                
            elif 'Kamu tidak memiliki' in pesan:
                time.sleep(2)
                await event.respond('/restore')
                print(time.asctime(), 'Isi Ulang Energi')
                return
                
            elif "Energi berhasil" in pesan:
                time.sleep(2)
                await event.respond(Area)
                print('Lanjut Gan')
                return
                
            elif 'Kamu tidak sedang' in pesan:
                time.sleep(2)
                await event.respond(Area)
                return
            
            else :
                time.sleep(2)
                await event.click(text=Alat)
                print(time.asctime(), 'Lempar pancingan')
                return
            
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')