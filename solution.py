from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = ("smtp.gmail.com", 25)

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)

    recv = clientSocket.recv(1024).decode()
    recv = recv.decode()
    print(recv)
    #print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = "MAIL FROM:<rgene2@gmail.com>\r\n"
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    recv2 = recv2.decode()
    print("MAIL FROM " + recv2)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCommand = "RCPT TO:<ramalaxmishah@gmail.com>\r\n"
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    recv3 = recv3.decode()
    print("RCPT TO " + recv3)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    recv4 = recv4.decode()
    print("DATA " + recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024).decode()
    print("DATA " + recv_msg.decode())
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv5 = clientSocket.recv(1024).decode()
    print("QUIT " + recv5.decode)
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')