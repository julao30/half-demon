from flask import Flask

main = Flask(__name__)

@main.route("/")
def hello():
    return "Dzień dobry, Git!<br>Fajnie, że wpadłeś!"

if __name__ == "__main__":
    main.run(debug=True)

