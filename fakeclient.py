import socket

with socket.socket() as s:
    host = "0.0.0.0"
    port = 420

    s.bind((host, port))
    s.listen()

    while True:
        con, addr = s.accept()
        while con:
            data = con.recv(1024)
            if not data: break
            print("Found", str(data.decode('utf-8')))

    s.close()