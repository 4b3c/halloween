# Setup Guide - Halloween Drink Counter

## Quick Start

Follow these steps to get the application running:

### 1. Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 2. Install Dependencies (if not already done)
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python halloween/app.py
```

The server will start on `http://localhost:5001`

### 4. Open in Browser

Navigate to: **http://localhost:5001**

You should see the Halloween-themed join page!

## How to Use

1. **Join**: Enter your name and click "Join the Party!"
2. **Count Drinks**: Use the + and - buttons to track your drinks
3. **View Leaderboard**: Click "View Leaderboard" to see all participants ranked by drink count

## Development Tips

- The app runs in debug mode by default
- All data is stored in memory (resets on server restart)
- Multiple users can join from different browsers
- Each user gets their own session

## Troubleshooting

**Port already in use:**
- Change the port in `halloween/app.py` line: `app.run(debug=True, host='0.0.0.0', port=5001)`

**Import errors:**
- Make sure the virtual environment is activated
- Run `pip install -r requirements.txt` again

**Static files not loading:**
- Check that the directory structure matches the design doc
- Ensure Flask can find the `static` and `templates` folders

## Stopping the Server

Press `Ctrl+C` in the terminal to stop the Flask server

