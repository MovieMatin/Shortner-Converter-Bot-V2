from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START_MESSAGE = '''**Hello, {}
I Am MPlaylink.com, Bulk Link Converter. I Can Convert Links Directly From Your MPlaylink Account,
    
1. Go To 👉 https://MPlaylink.com/member/tools/api  
2. Than Copy API Key
3. Than Type /api than give a single space and than paste your API Key (see example to understand more...)**

**/api(space)API Key 
(See Example.👇)
Example:** `/api de21dbefae7a07cd1f767ca60b6fa0be8c0eeecf `

**➕ Hit** 👉 /Features To Know More Features Of This Bot.
**💁‍♀️ Hit** 👉 /help To Get Help.
**➕ Hit** 👉 /channel Command To Get Help About Adding your channel to bot.
**➕ Hit** 👉 /footer To Get Help About Adding your Custom Footer to bot.

**- Message @Md_Matin_Ashraf For More Help -**
'''

HELP_MESSAGE = '''**Hello, {}
I Am MPlaylink, Bulk Link Converter Bot. I Can Convert Links Directly From Your MPlaylink Account,**
    
1. Go To 👉 https://MPlaylink.com/member/tools/api  
2. Than **Copy API** Key
3. Than Type **/api** than give a **single space** and than **paste** your **API** Key (**see example** to understand more...)

**/api(space)API Key 
(See Example.👇)
Example:** `/api de21dbefae7a07cd1f767ca60b6fa0be8c0eeecf `

**➕ Hit** 👉 /Features To Know More Features Of This Bot.
**💁‍♀️ Hit** 👉 /help To Get Help.
**➕ Hit** 👉 /channel Command To Get Help About Adding your channel to bot.
**➕ Hit** 👉 /footer To Get Help About Adding your Custom Footer to bot.

**- Message @Md_Matin_Ashraf For More Help -**
'''

ABOUT_TEXT = '''**Hey! My name is @MPlaylinkBot. I am MPlaylink Link Converter Bot.**

**⚡Features⚡**

• I can **Convert any** links or posts to your **MPlaylink** link / post. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)

• I Can **auto** add custom **footer text** to your every post. Hit 👉 /footer To know more...

• I Can **auto** add custom **Header text** to your every post. Hit 👉 /Header To know more...

• I Can **replace / remove** other's **channel links** with **your channel** link. Hit 👉 /channel To know More...

• I Can **Automatically Replace** Your ***Banner** Image To images in the post. Hit  👉/banner_image To Know More... 

• **No** need to share **password or email** to convert links.**

**- Message @Md_Matin_Ashraf For More Help -**

**Click On Custom Alias To Create Custom Link**
'''

CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/MPlayLink | MPlaylink"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""

ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf')
        
    ],


])

HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('More Features', callback_data=f'about_command')
        
    ],


])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Get Api', url=f'https://MPlaylink.com/member/tools/api')
    ]
])



BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """
- Website: [{base_site}](https://mplaylink.com/ref/MdMatinAshraf)

- Site Link {base_site} Current Linked API: {shortener_api}

- Replace Channel Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/set_api [api]`
            
Ex: `/api de21dbefae7a07cd1f767ca60b6fa0be8c0eeecf `

Get API From [{base_site}](https://mplaylink.com/ref/MdMatinAshraf)

Current {base_site} API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \n
To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """**Reply to the Footer Text You Want**

This Text will be added to the **bottom** of every message **caption** or text

For adding **line break** use \n
To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """**Hello Md Matin Ashraf, I am MPlaylink.com, Bulk Link Converter Bot From Linked MPlaylink.com Account,**

**🌟 Type** /channel (channel link or username)

**example:**
/channel @MPlayLink
Or
/channel https://t.me/MPlayLink

**🤘 Hit** 👉 /features To Know More Features Of This Bot.

**- Message @Md_Matin_Ashraf For More Help -**"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://telegra.ph/file/5e96340a91470256b387a.jpg`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
