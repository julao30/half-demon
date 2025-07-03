from flask import Flask, render_template_string, request
from password_validator import is_valid_password

app = Flask(__name__)

form_html = """
<!DOCTYPE html>
<html>
<head><title>Walidacja hasła</title></head>
<body>
  <h1>Podaj hasło</h1>
  <form method="POST">
    <input type="password" name="password" />
    <input type="submit" value="Sprawdź" />
  </form>
  {% if result %}
    <p><strong>{{ result }}</strong></p>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form.get("password")
        if is_valid_password(password):
            result = "Hasło OK"
        else:
            result = "Hasło NIE spełnia wymagań."
    return render_template_string(form_html, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
