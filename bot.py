#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from time import sleep

def send(url,paylod,header,acc):
    r = requests.post(url, data=paylod, headers=header)
    return f'Message for {acc}sent'
def main():
    #ID accs
    id_first_account = input('ID first_acc:')
    id_second_account = input('ID second_acc:')
    first_acc = f"<@{id_first_account}>"
    second_acc = f"<@{id_second_account}>"



    #MESSAGES
    data_for_first_account = [f"{second_acc} Hello,Bro!"] #Message example
    data_for_second_account = [f"{first_acc} Hi!"]#Message example
    #TOKENS
    token1 = input('Token for the first account: ')
    token2 = input('Token for the second account: ')

    #NOTIFICATION
    Send_notification = input('Send notification?(y/N)')
    #HEADERS
    header1 = {
        'authorization': token1
    }
    header2 = {
        'authorization': token2
    }
    #Timeouts#
    break_between_messages = int(input('Break between messages: '))
    timeout = input('Enter timeout: ')
    #id_chat and url
    id_chat = input('ID chat:')
    url = f"https://discord.com/api/v9/channels/{id_chat}/messages"
    count = 0
    while count <= len(data_for_first_account):
        paylod1 ={
        'content':data_for_first_account[count]
        }
        paylod2 = {
            'content': data_for_second_account[count]
        }
        try:
            notification = send(url,paylod1,header1,'first_acc')
            if Send_notification in ('y','Y'):
                print(notification)
        except:
            print(f'Message on first account not sent')
        sleep(break_between_messages)
        try:
            notification = send(url,paylod2,header2,'second_acc')
            if Send_notification in ('y','Y'):
                print(notification)
        except:
            print(f'Message on second account not sent')
        count = count + 1
        if count == len(data_for_first_account):
            count = 0
        sleep(int(timeout))
if __name__ == '__main__':
    main()
