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

    github_file_url = 'https://github.com/username/repo/blob/main/file_name.ext'

    github_repo_url = 'https://github.com/username/repo'

