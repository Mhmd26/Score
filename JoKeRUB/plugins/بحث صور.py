import asyncio
import aiohttp
import os
import shutil
import time
from bs4 import BeautifulSoup
from datetime import datetime
from telethon.utils import guess_extension
from urllib.parse import urlencode

from JoKeRUB import l313l
from ..Config import Config

ZELZAL_APP_ID = "6e65179ed1d879f3d905e28ef8803625"

def get_extension(content_type):
    ext = guess_extension(content_type)
    return ext if ext else ".jpg"  # تعيين ".jpg" كقيمة افتراضية إذا كانت القيمة None

@l313l.ar_cmd(pattern="صور (.*)")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("**✎┊‌ جـاري البحث عن الصـور **")
    zedthon = event.pattern_match.group(1)
    wzed_dir = os.path.join(
        Config.TMP_DOWNLOAD_DIRECTORY,
        zedthon
    )
    if not os.path.isdir(wzed_dir):
        os.makedirs(wzed_dir)
    input_url = "https://bots.shrimadhavuk.me/search/"
    headers = {"USER-AGENT": "UseTGBot"}
    url_lst = []
    async with aiohttp.ClientSession() as requests:
        data = {
            "q": zedthon,
            "app_id": ZELZAL_APP_ID,
            "p": "GoogleImages"
        }
        reponse = await requests.get(
            input_url,
            params=data,
            headers=headers
        )
        response = await reponse.json()
        for result in response["results"]:
            if len(url_lst) > 9:
                break
            caption = result.get("description")
            image_url = result.get("url")
            image_req_set = await requests.get(image_url)
            image_file_name = str(time.time()) + "" + get_extension(
                image_req_set.headers.get("Content-Type")
            )
            image_save_path = os.path.join(
                wzed_dir,
                image_file_name
            )
            with open(image_save_path, "wb") as f_d:
                f_d.write(await image_req_set.read())
            url_lst.append(image_save_path)
    if not url_lst:
        await event.edit(f"**✎┊‌ اووبـس .. لم استطـع ايجـاد صـور عـن {zedthon} ؟!**\n**✎┊‌ حـاول مجـدداً واكتـب الكلمـه بشكـل صحيح**")
        return
    await event.reply(
        file=url_lst,
        parse_mode="html",
        force_document=True
    )
    for each_file in url_lst:
        os.remove(each_file)
    shutil.rmtree(wzed_dir, ignore_errors=True)
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit(
        f"**✎┊‌ اكتمـل البحث عـن {zedthon} في {ms} ثانيـه ✓**",
        link_preview=False
    )
    await asyncio.sleep(5)
    await event.delete()

@l313l.ar_cmd(pattern="خلفيات (.*)")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("**✎┊‌ جـاري البحث عن خلفيـات**")
    zedthon = event.pattern_match.group(1)
    wzed_dir = os.path.join(
        Config.TMP_DOWNLOAD_DIRECTORY,
        zedthon
    )
    if not os.path.isdir(wzed_dir):
        os.makedirs(wzed_dir)
    input_url = "https://bots.shrimadhavuk.me/search/"
    headers = {"USER-AGENT": "UseTGBot"}
    url_lst = []
    async with aiohttp.ClientSession() as requests:
        data = {
            "q": zedthon,
            "app_id": ZELZAL_APP_ID,
            "p": "GoogleImages"
        }
        reponse = await requests.get(
            input_url,
            params=data,
            headers=headers
        )
        response = await reponse.json()
        for result in response["results"]:
            if len(url_lst) > 9:
                break
            caption = result.get("description")
            image_url = result.get("url")
            image_req_set = await requests.get(image_url)
            image_file_name = str(time.time()) + "" + get_extension(
                image_req_set.headers.get("Content-Type")
            )
            image_save_path = os.path.join(
                wzed_dir,
                image_file_name
            )
            with open(image_save_path, "wb") as f_d:
                f_d.write(await image_req_set.read())
            url_lst.append(image_save_path)
    if not url_lst:
        await event.edit(f"**✎┊‌ اووبـس .. لم استطـع ايجـاد خلفيـات عـن {zedthon} ؟!**\n**✎┊‌ حـاول مجـدداً واكتـب الكلمـه بشكـل صحيح**")
        return
    await event.reply(
        file=url_lst,
        parse_mode="html",
        force_document=True
    )
    for each_file in url_lst:
        os.remove(each_file)
    shutil.rmtree(wzed_dir, ignore_errors=True)
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit(
        f"**✎┊‌ اكتمـل البحث عـن {zedthon} في {ms} ثانيـه ✓**",
        link_preview=False
    )
    await asyncio.sleep(5)
    await event.delete()
    
