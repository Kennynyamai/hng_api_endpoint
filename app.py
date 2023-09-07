from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    current_day = datetime.datetime.now().strftime('%A')

    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = 'https://github.com/Kennynyamai/hng_api_endpoint/blob/main/app.py'

    github_repo_url = 'https://github.com/Kennynyamai/hng_api_endpoint'

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    return jsonify(response_data)

from waitress import serve
serve(app, host="0.0.0.0", port=8080)



