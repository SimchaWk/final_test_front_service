from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Data Search and Analysis Interface</title>
    <meta charset="utf-8">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .section {
            margin-bottom: 30px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        h2 {
            color: #333;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"], 
        input[type="number"],
        input[type="date"] {
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            width: 200px;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 8px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .link-button {
            display: inline-block;
            margin: 5px;
            padding: 8px 15px;
            background-color: #28a745;
            color: white;
            text-decoration: none;
            border-radius: 4px;
        }
        .link-button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Data Search and Analysis Interface</h1>

        <div class="section">
            <h2>Terror Events Analysis</h2>

            <form action="http://127.0.0.1:5000/terror_events/casualties_by_region" method="get" target="_blank">
                <div class="form-group">
                    <label>Casualties by Region:</label>
                    <input type="number" name="top" placeholder="Number of results" value="30">
                    <input type="checkbox" name="include_map" value="true" checked>
                    <label>Include Map</label>
                    <button type="submit">Show Results</button>
                </div>
            </form>

            <form action="http://127.0.0.1:5000/terror_events/attack_change_by_region_2" method="get" target="_blank">
                <div class="form-group">
                    <label>Attack Changes by Region:</label>
                    <input type="checkbox" name="include_map" value="true" checked>
                    <label>Include Map</label>
                    <button type="submit">Show Results</button>
                </div>
            </form>

            <form action="http://127.0.0.1:5000/terror_events/terror_hotspots" method="get" target="_blank">
                <div class="form-group">
                    <label>Terror Hotspots:</label>
                    <select name="time_period">
                        <option value="5_years" selected>5 years</option>
                        <option value="10_years">10 years</option>
                        <option value="20_years">20 years</option>
                    </select>
                    <input type="number" name="start_year" placeholder="Start year" value="1990">
                    <input type="checkbox" name="include_map" value="true" checked>
                    <label>Include Map</label>
                    <button type="submit">Show Results</button>
                </div>
            </form>
        </div>

        <div class="section">
            <h2>Graph Analysis</h2>
            <a href="http://127.0.0.1:5000/graph_events/high-group-activity" class="link-button" target="_blank">High Group Activity</a>
            <a href="http://127.0.0.1:5000/graph_events/attack-strategies" class="link-button" target="_blank">Attack Strategies</a>
            <a href="http://127.0.0.1:5000/graph_events/shared-targets" class="link-button" target="_blank">Shared Targets</a>
        </div>

        <div class="section">
            <h2>Search</h2>

            <form action="http://localhost:5000/asearch/keywords" method="get" target="_blank">
                <div class="form-group">
                    <label>Keyword Search:</label>
                    <input type="text" name="q" placeholder="Search term" value="bombing">
                    <input type="number" name="limit" placeholder="Result limit" value="10">
                    <button type="submit">Search</button>
                </div>
            </form>

            <form action="http://localhost:5000/search/news" method="get" target="_blank">
                <div class="form-group">
                    <label>News Search:</label>
                    <input type="text" name="q" placeholder="Search term" value="terror">
                    <button type="submit">Search</button>
                </div>
            </form>

            <form action="http://localhost:5000/search/historic" method="get" target="_blank">
                <div class="form-group">
                    <label>Historic Search:</label>
                    <input type="text" name="q" placeholder="Search term" value="attack">
                    <input type="number" name="limit" placeholder="Result limit" value="5">
                    <button type="submit">Search</button>
                </div>
            </form>

            <form action="http://localhost:5000/search/combined" method="get" target="_blank">
                <div class="form-group">
                    <label>Combined Search:</label>
                    <input type="text" name="q" placeholder="Search term" value="explosion">
                    <input type="date" name="start_date" value="2010-01-01">
                    <input type="date" name="end_date" value="2020-12-31">
                    <button type="submit">Search</button>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    app.run(port=5001)