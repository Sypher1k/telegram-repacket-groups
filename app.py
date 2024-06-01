from telethon import TelegramClient
import configparser
import re

config = configparser.ConfigParser()
config.read('config.ini')

api_id = config['API']['Id']
api_hash = config['API']['Hash']
phone_number = config['SETTINGS']['PhoneNumber']
group_name = config['SETTINGS']['GroupName']
message_limit = int(config['SETTINGS']['MessageLimit'])
last_read_id_file = config['FILES']['LastReadId']
code_output = config['FILES']['CodeOutput']
session_name = config['SETTINGS']['SessionName']

message_list = []
raw_code_list = []
id_list = []

try:
    last_read_id = int(open(last_read_id_file,'r').readline())
except Exception as e:
    print(e)
    last_read_id = 0

client = TelegramClient(session_name, api_id, api_hash)

async def get_last_message(group_name):
    await client.start(phone_number)
    async for message in client.iter_messages(group_name, limit = message_limit, min_id=last_read_id):
        id_list.append(message.id)
        message_text = message.text
        # print(f"Last message in {group_name}: {message.text} -> {message.id}")
        try:
            if '1111111' in message_text: continue
            else: message_list.append(message_text.replace("`",""))
        except:
            continue

def is_valid_code(word):
    return word.isalnum() and len(word) == 8 and re.search(r'[A-Za-z]', word) and re.search(r'\d', word)

def extract_codes(message_list):
    for message in message_list:
        words = message.split()
        for word in words:
            if is_valid_code(word):
                raw_code_list.append(word)

def remove_duplicates(original_list):
    new_set = set(original_list)
    print(len(new_set),"Codes Found")
    return list(new_set)

def last_id_to_file(id):
    with open(last_read_id_file,'w') as file:
        file.write(str(id))

def codes_to_file(code_list):
    with open(code_output,'w') as file:
        for line in code_list:
            file.write(line+"\n")

def clear_file():
    with open(code_output,'w') as file:
        pass

def main():

    with client:
        client.loop.run_until_complete(get_last_message(group_name))

    try:
        last_id_to_file(id_list[0])
    except:
        print("No new codes Detected...")
        clear_file()
        exit()

    extract_codes(message_list)
    new_codes = remove_duplicates(raw_code_list)
    codes_to_file(new_codes)

    print("Last Message ID : ", id_list[0])

if __name__ == "__main__":
    main()


