import socket, time

headersize = 10
accepted_answers = ['mel', 'den', 'pri', 'dis', 'siz']

def send_msg(content, conn):
    msg = f'{len(content):<{headersize}}' + content
    conn.send(bytes(msg, 'utf-8'))

def recv_msg(conn):
    header = conn.recv(headersize)
    try:
        msg_len = int(header.decode())
    except:
        return None
    msg = conn.recv(msg_len)
    return msg.decode()

def parse_input(conn):
    msg = recv_msg(conn)
    if msg == 'card':
        card = recv_msg(conn)
        print(card)
        send_msg('card received', conn)
    elif msg == 'request':
        while True:
            print('Choose a category:')
            category = input()
            if category[:3] in accepted_answers:
                send_msg(category, conn)
                break
            else:
                continue
    elif msg == 'wait':
        send_msg('wait received', conn)
        wait_msg = recv_msg(conn)
        print(wait_msg)
    elif msg == 'turn choice':
        choice_msg = recv_msg(conn)
        print(choice_msg)
    elif msg == 'result':
        result_msg = recv_msg(conn)
        print(result_msg)
    elif msg == 'eliminated':
        print('You have been eliminated.')
    elif msg == 'winner':
        print('You won!')
    

print('tobooo studios presents...\n')
time.sleep(1)
print('Top Trumps: Elements\n')
time.sleep(1)
s = socket.socket()
port = input('Enter port: ')
addr = input('IP address: ')
s.connect((addr, int(port)))
welcome_msg = recv_msg(s)
print(welcome_msg)
name = input()
send_msg(name, s)
wait_msg = recv_msg(s)
print(wait_msg)
intro_msg = recv_msg(s)
print(intro_msg)
while True:
    parse_input(s)
