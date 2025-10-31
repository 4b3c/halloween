# Halloween Drink Counter App - Design Document

## Overview
A Flask-based web application for tracking drinks in a Halloween party setting. Users enter their name (Kahoot-style) and can increment or decrement their drink counter. A Halloween-themed leaderboard displays all participants ranked by their drink count.

## Application Structure

```
halloween/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── index.html        # Landing/join page
│   ├── counter.html      # Drink counter interface
│   └── leaderboard.html  # Leaderboard with graph
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Halloween-themed styles
│   └── js/
│       └── main.js       # Client-side JavaScript
└── requirements.txt      # Python dependencies
```

## Features

### 1. Landing/Join Page (`/`)
- **Purpose**: Welcome page where users enter their name
- **UI Elements**:
  - Halloween-themed header/logo
  - Large input field for name entry
  - "Join the Party" button
  - Kahoot-style entry experience
- **Functionality**:
  - Validates non-empty name input
  - Creates a unique session for the user
  - Redirects to drink counter page upon successful join
- **Backend**: 
  - In-memory storage of participants (dictionary mapping names to drink counts)
  - Session management for user tracking

### 2. Drink Counter Page (`/counter`)
- **Purpose**: Main interface for tracking individual drinks
- **UI Elements**:
  - User's name displayed prominently
  - Large "+" button for incrementing drinks
  - Large "-" button for decrementing drinks
  - Current drink count display
  - "View Leaderboard" button
  - User-specific view only (shows their own count)
- **Functionality**:
  - Increment and decrement drink count with buttons
  - Count cannot go below 0
  - Real-time updates to in-memory storage
  - Navigation to leaderboard
- **Backend**:
  - POST endpoint to increment drinks
  - POST endpoint to decrement drinks
  - Session-based user identification

### 3. Leaderboard Page (`/leaderboard`)
- **Purpose**: Display all participants ranked by drink count
- **UI Elements**:
  - Halloween-themed title (e.g., "Halloween Drinking Champions")
  - Bar graph visualization (HTML/CSS/JavaScript)
  - Bars ordered by drink count (highest first)
  - Each bar shows:
    - Participant name
    - Number of drinks
    - Halloween-themed colors (orange, black, purple)
  - "Return to Counter" button
- **Functionality**:
  - Fetches all participants from backend
  - Sorts by drink count (descending)
  - Renders animated bar chart
  - Updates in real-time when returning from counter
- **Backend**:
  - GET endpoint returning all participants sorted by count

## Technical Specifications

### Backend (Flask)
- **Framework**: Flask (Python web framework)
- **Session Management**: Flask sessions with secret key
- **Data Storage**: In-memory Python dictionary (stateless across server restarts)
- **Endpoints**:
  - `GET /`: Render join page
  - `POST /join`: Process name submission, create session
  - `GET /counter`: Render drink counter page
  - `POST /increment`: Increment user's drink count
  - `POST /decrement`: Decrement user's drink count (min 0)
  - `GET /leaderboard`: Render leaderboard page
  - `GET /api/participants`: JSON API for all participants

### Frontend
- **HTML**: Semantic HTML5 structure
- **CSS**: Halloween theme with:
  - Dark backgrounds (black/dark purple)
  - Halloween colors (orange #FF6B35, purple #9D4EDD)
  - Smooth animations and transitions
  - Responsive design principles
- **JavaScript**:
  - Vanilla JavaScript (no frameworks)
  - Fetch API for AJAX requests
  - Dynamic DOM manipulation for bar chart
  - Input validation

### Dependencies
```
Flask==3.0.0
```

### Session Management
- Users identified by session cookie
- Session stores: `{ 'name': 'user_name' }`
- Server-side storage: `{ 'name': drink_count }`

## User Flow

1. User visits `/` → lands on join page
2. User enters name and clicks "Join the Party"
3. System creates session and adds to participants dictionary
4. User redirected to `/counter`
5. User clicks "+" or "-" buttons to adjust drink count
6. User clicks "View Leaderboard" → redirected to `/leaderboard`
7. User sees all participants ranked by drinks
8. User can return to counter via button
9. Session persists across page navigation

## Halloween Theme Design

### Color Palette
- **Primary Background**: Dark purple/black (#1a0d33, #0a0a0a)
- **Accent Colors**: 
  - Orange: #FF6B35 (pumpkins, warmth)
  - Purple: #9D4EDD (mystery, spooky)
  - Gray: #4a4a4a (neutrals)
- **Text**: White (#ffffff) for contrast

### Visual Elements
- Spooky, friendly Halloween aesthetic
- Smooth animations on interactions
- Large, clickable buttons (mobile-friendly)
- Glowing effects on buttons and bars
- Pumpkin/bat-themed icons (optional unicode: 🎃 🦇)

### Typography
- Sans-serif fonts (system defaults)
- Bold headings for hierarchy
- Large font sizes for readability

## Edge Cases & Validation

1. **Duplicate Names**: Allow multiple users with same name (distinguished by session)
2. **Negative Counts**: Prevent drinks from going below 0
3. **Empty Name**: Client and server-side validation
4. **Session Expiry**: Graceful redirect to join page
5. **Backend Reset**: All data lost on server restart (expected behavior)
6. **Special Characters**: Sanitize HTML to prevent XSS

## Future Enhancements (Out of Scope)
- Persistent database storage
- User authentication/login
- Multiple party rooms
- Admin controls to reset counts
- Charts with Chart.js library
- Real-time WebSocket updates
- Mobile app version

## Deployment Notes
- Run Flask in development mode with debugging
- Use `app.run(debug=True)` for development
- For production, use proper WSGI server (gunicorn, uwsgi)
- Environment variables for configuration
- Consider adding rate limiting for production use

## Setup Instructions

1. Create virtual environment: `python -m venv venv`
2. Activate venv: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run application: `python halloween/app.py` or use `./run.sh` (macOS/Linux)
5. Open browser to `http://localhost:5001`

**Quick Start:** Just run `./run.sh` to start the app!

## Testing Strategy
- Manual testing of all user flows
- Test increment/decrement functionality
- Verify leaderboard sorting
- Test edge cases (negative counts, empty names)
- Cross-browser compatibility check

