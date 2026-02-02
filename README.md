# Lab Activity: Flask Login + Profile (Web + JSON API)

## Overview
Build a Flask app that supports:
- Session-based authentication
- Profile creation/editing with validation
- HTML forms and a JSON REST API for the same data

You will practice Flask routing, form handling, session management, validation, and JSON responses.

## Prerequisites
- Python 3.10+ and pip
- Basic understanding of Flask and HTTP methods

## Installation
1. Clone or download this repository.
2. Install Flask:
   ```
   pip install flask
   ```
   Or install all dependencies from `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

## Getting Started
1. Open `app.py` — this is where you'll write code.
2. You'll find 5 TODOs marking incomplete functions and routes.
3. HTML templates are already provided in `templates/`.

## Your Tasks (Required Coding)

### Task 1: Implement helper functions (15 min)
**In `app.py`, implement these three helper functions:**

1. **`get_current_user()`**
   - Check the Flask session for a logged-in user.
   - Return the username if logged in, otherwise return `None`.

2. **`validate_profile_data(first_name, last_name, student_id)`**
   - Return `None` if all fields are valid.
   - Return an error message string if:
     - Any field is empty
     - `student_id` is not numeric
   - Example error: `"Student ID must be numeric."`

3. **`normalize_profile_data(first_name, last_name, student_id)`**
   - Return a dictionary with trimmed strings.
   - Convert `student_id` to string.

### Task 2: Implement the profile route (20 min)
**Complete the `profile()` route to handle both GET and POST:**

- **GET**: Render `profile.html` with the user's existing profile data (if any).
- **POST**: 
  - Get form data: `first_name`, `last_name`, `student_id`.
  - Validate using `validate_profile_data()`.
  - If valid: save to `profiles[username]` and redirect to home.
  - If invalid: re-render `profile.html` with the error message and form data.

### Task 3: Implement the JSON API (25 min)
**Complete the `api_profile()` route to handle GET and POST with JSON:**

- **Authentication**: Return `401` with error if user is not logged in.
- **GET**: Return current user's profile as JSON.
  - Example response: `{"username": "student", "profile": {...}}`
- **POST**: 
  - Check `Content-Type` is `application/json` (return `415` if not).
  - Parse JSON payload.
  - Validate using `validate_profile_data()`.
  - If valid: save and return `200` with message and profile.
  - If invalid: return `400` with error message.

### Task 4: Test your implementation (10 min)
Once complete, run:
```
python app.py
```

**Via browser:**
1. Go to http://127.0.0.1:5000.
2. Log in with: `student` / `secret`.
3. Create a profile. Try invalid data to test validation.

**Via JSON API (use curl, Postman, or Python requests):**
1. Login first in the browser to create a session.
2. POST to `/api/profile` with `{"first_name": "Ada", "last_name": "Lovelace", "student_id": "12345"}`.
3. GET `/api/profile` to retrieve the stored profile.

## Hints if You Get Stuck
Refer to the comments in each TODO section. Think about:
- How Flask's `session` object works
- How to use `.strip()` and type conversions
- What HTTP status codes mean (401, 400, 415, 200)

## Additional Resources

### HTTP Status Codes Used
- `200` — OK (successful)
- `400` — Bad Request (validation error)
- `401` — Unauthorized (not logged in)
- `415` — Unsupported Media Type (wrong Content-Type)

### Testing the JSON API with curl
After logging in via the browser:
```bash
# GET request
curl -b cookies.txt http://127.0.0.1:5000/api/profile

# POST request
curl -b cookies.txt -X POST -H "Content-Type: application/json" \
  -d '{"first_name":"Ada","last_name":"Lovelace","student_id":"12345"}' \
  http://127.0.0.1:5000/api/profile
```

**Why cookies?** When you log in via the browser, Flask creates a **session cookie** that stores your login state. The `-b cookies.txt` flag tells curl to send this cookie with each request, so the server recognizes you. Without it, the API returns 401 (unauthorized) because it has no way to know who you are.

## Stretch Goals (Optional)
- Add a DELETE endpoint to clear a profile.
- Implement password hashing with bcrypt.
- Persist profiles to a JSON file or TinyDB database.

## Troubleshooting
- **401 error from /api/profile**: You are not logged in. Use the browser to log in first.
- **Profile data disappears on restart**: Profiles are stored in memory. See stretch goal #4 for persistence.
- **Validation errors not showing**: Check that `profile.html` has an error display block.
