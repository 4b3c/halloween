from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import json
from pathlib import Path

# Create Flask app with explicit template and static folders
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.urandom(24)

# Path to data file
DATA_FILE = Path(__file__).parent / 'data.json'

def load_participants():
    """Load participants from JSON file"""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_participants(participants):
    """Save participants to JSON file"""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(participants, f, indent=2)
    except IOError:
        print(f"Warning: Could not write to {DATA_FILE}")

@app.route('/')
def index():
    """Landing page where users enter their name"""
    return render_template('index.html')

@app.route('/join', methods=['POST'])
def join():
    """Process name submission and create session"""
    name = request.form.get('name', '').strip()
    
    if not name:
        return redirect(url_for('index'))
    
    # Create session for user
    session['name'] = name
    
    # Load participants, add if not already there
    participants = load_participants()
    if name not in participants:
        participants[name] = 0
        save_participants(participants)
    
    return redirect(url_for('counter'))

@app.route('/counter')
def counter():
    """Render drink counter page"""
    if 'name' not in session:
        return redirect(url_for('index'))
    
    name = session['name']
    participants = load_participants()
    count = participants.get(name, 0)
    return render_template('counter.html', name=name, count=count)

@app.route('/increment', methods=['POST'])
def increment():
    """Increment user's drink count"""
    if 'name' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    
    name = session['name']
    participants = load_participants()
    participants[name] = participants.get(name, 0) + 1
    save_participants(participants)
    return jsonify({'success': True, 'count': participants[name]})

@app.route('/decrement', methods=['POST'])
def decrement():
    """Decrement user's drink count (minimum 0)"""
    if 'name' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    
    name = session['name']
    participants = load_participants()
    current_count = participants.get(name, 0)
    participants[name] = max(0, current_count - 1)
    save_participants(participants)
    return jsonify({'success': True, 'count': participants[name]})

@app.route('/leaderboard')
def leaderboard():
    """Render leaderboard page"""
    return render_template('leaderboard.html')

@app.route('/api/participants')
def api_participants():
    """API endpoint returning all participants sorted by count"""
    participants = load_participants()
    # Sort by count (descending)
    sorted_participants = sorted(
        participants.items(), 
        key=lambda x: x[1], 
        reverse=True
    )
    
    # Convert to list of dicts for JSON
    result = [{'name': name, 'count': count} for name, count in sorted_participants]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

