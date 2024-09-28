from flask import Flask, render_template_string

# Create a Flask application
app = Flask(__name__)

# HTML content embedded in Python using render_template_string
html_code = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deploy app on amazon ec-2 using jenkins and github webhooks</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        h1 { color: #333; }
        button { padding: 10px 20px; background-color: #007BFF; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <h1>Welcome to Flask with HTML!</h1>
    <p>Click the button to see a message:</p>
    <button onclick="displayMessage()">Click Me</button>
    <p id="message"></p>

    <script>
        function displayMessage() {
            document.getElementById("message").innerHTML = "Hello, World!";
        }
    </script>
</body>
</html>
'''

# Route for the home page
@app.route('/')
def home():
    return render_template_string(html_code)

# Run the application and bind it to 0.0.0.0
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Bind to 0.0.0.0 to allow external access
