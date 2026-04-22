from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Read report
    with open("report.txt", "r") as f:
        report = f.readlines()

    # Read blocked IPs
    with open("blocked_ips.txt", "r") as f:
        blocked_ips = f.readlines()

    return render_template("index.html", report=report, blocked_ips=blocked_ips)

if __name__ == "__main__":
    app.run(debug=True)