from flask import Flask, render_template_string, request

app = Flask(__name__)

# Mechanical Engineering Tools Data
tools = {
    "Vernier Caliper": {
        "use": "Used to measure internal and external dimensions accurately.",
        "range": "0-150 mm"
    },
    "Micrometer": {
        "use": "Used for precise measurement of small dimensions.",
        "range": "0-25 mm"
    },
    "Torque Wrench": {
        "use": "Used to apply specific torque to nuts and bolts.",
        "range": "10-200 Nm"
    },
    "Dial Gauge": {
        "use": "Used to measure alignment and small distances.",
        "range": "0-10 mm"
    },
    "Hammer": {
        "use": "Used for striking mechanical components.",
        "range": "General Tool"
    }
}

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Mechanical Engineering Tools</title>

    <style>
        body {
            font-family: Arial;
            background-color: #f4f4f4;
            padding: 20px;
        }

        h1 {
            text-align: center;
            color: #222;
        }

        .card {
            background: white;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            box-shadow: 0px 0px 5px gray;
        }

        input {
            padding: 10px;
            width: 250px;
        }

        button {
            padding: 10px;
            background: blue;
            color: white;
            border: none;
            border-radius: 5px;
        }
    </style>
</head>

<body>

<h1>Mechanical Engineering Tools Web App</h1>

<form method="POST">
    <input type="text" name="tool" placeholder="Search Tool">
    <button type="submit">Search</button>
</form>

{% if result %}
<div class="card">
    <h2>{{ tool_name }}</h2>
    <p><strong>Use:</strong> {{ result['use'] }}</p>
    <p><strong>Range:</strong> {{ result['range'] }}</p>
</div>
{% endif %}

<h2>Available Tools</h2>

{% for name, info in tools.items() %}
<div class="card">
    <h3>{{ name }}</h3>
    <p><strong>Use:</strong> {{ info['use'] }}</p>
    <p><strong>Range:</strong> {{ info['range'] }}</p>
</div>
{% endfor %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    tool_name = ""

    if request.method == "POST":
        search = request.form["tool"]

        for name, info in tools.items():
            if search.lower() == name.lower():
                result = info
                tool_name = name

    return render_template_string(
        html,
        tools=tools,
        result=result,
        tool_name=tool_name
    )

if __name__ == "__main__":
    app.run(debug=True)
