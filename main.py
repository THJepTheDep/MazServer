from time import sleep
from progress.bar import Bar
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = input("IPV4: ")
PORT = 9999

login_or_signup = input("Login or sign up login/signup: ")
if login_or_signup == "login":
    print("Login Page:")
elif login_or_signup == "signup":
    print("Signup Page")
else:
    print("Please Enter Either login or signup with lowercase letters")

password_correct = "Password Correct!"

if login_or_signup == "signup":
    print("----------------------------------------------------")
    print("                     Sign Up                        ")
    print("----------------------------------------------------")

    name = input("Name: ")
    password = input("Password: ")

    print("Are these values correct?")
    print("Name=" + name)
    print("Password=" + password)

    continue1 = input("Continue Y/N: ")
    if continue1 == "Y":
        print("Loading...")
    elif continue1 == "y":
        print("Loading...")
    else:
        print("Stopped.")


elif login_or_signup == "login":
    print("----------------------------------------------------")
    print("                     Log in                         ")
    print("----------------------------------------------------")

    name = input("Name: ")
    password = input("Password: ")
    print(password_correct)
else:
    print("Login Cancelled")

if password_correct == "Password Correct!":
    print("            ")
    print("_______________________________________________________________________________")
    print("          www.mazanius.eu                         Github: THJepTheDep          ")
    print("_______________________________________________________________________________")
    print("Starting client. This can take a while because its starting up a local server. ")
    print("_______________________________________________________________________________")

    with Bar('Loading', fill='¤', suffix='%(percent).1f%% - %(eta)ds') as bar:
        for i in range(100):
            sleep(0.02)
            bar.next()

    class NeuralHTTP(BaseHTTPRequestHandler):

        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes('<!DOCTYPE html><html><head> <title>Login 3dtogo.dk</title> <style> body { background-color: #505050; font-family: Arial, sans-serif; } form { display: flex; justify-content: center; align-items: center; height: 40vh; flex-wrap: wrap; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.2); width: 300px; /* added */ } label { width: 100%; text-align: left; margin-bottom: 10px; font-weight: bold; /* added */ } input[type="text"], input[type="password"] { width: 100%; padding: 12px 20px; margin: 8px 0; box-sizing: border-box; border-radius: 5px; border: 1px solid #ccc; } input[type="button"] { width: 100%; background-color: #4CAF50; color: white; padding: 14px 20px; margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; } input[type="button"]:hover { background-color: #45a049; } </style></head><body> <form> <label for="username">Brugernavn:</label> <input type="text" id="username" name="username"> <br> <label for="password">Adgangskode:</label> <input type="password" id="password" name="password"> <br> <input type="button" value="Login" onclick="checkCredentials()"> </form> <script> function checkCredentials() { var username = document.getElementById("username").value; var password = document.getElementById("password").value; if (username == "theo" && password == "ma3de69TJ") { window.location.href = "www.mazanius.eu"; } else { alert("Forkert brugernavn eller adgangskode. Prøv venligst igen."); } } </script></body></html>', "utf-8"))


server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server Now Running On HOST:", HOST, "PORT:", PORT, "| Copy Paste:",HOST,":",PORT)
print("Paste without spaces")

server.serve_forever()
server.server_close()
print("Server Now Closed!")
