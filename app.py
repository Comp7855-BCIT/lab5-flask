import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")

# A dummy user for the login. In production, store hashed passwords in a database.
dummy_user = {
    "username": "student",
    "password": "secret"
}

# In-memory storage for profiles (dict of username -> profile data)
profiles = {}

# TODO 1: Implement this helper function
# It should return the logged-in username from session, or None if not logged in
def get_current_user():
    pass

# TODO 2: Implement this validation function
# It should check:
#   - first_name, last_name, student_id are all provided (non-empty)
#   - student_id is numeric
# Return None if valid, or an error message string if invalid
def validate_profile_data(first_name, last_name, student_id):
    pass

# TODO 3: Implement this normalization function
# It should return a dict with trimmed and normalized profile data
def normalize_profile_data(first_name, last_name, student_id):
    pass

@app.route("/")
def home():
    # If the user is logged in, show a welcome message; otherwise prompt them to log in.
    current_user = get_current_user()
    if current_user:
        return render_template("dashboard.html", username=current_user)
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")  # Show the login form

    # If POST, process the login form
    username = request.form.get("username")
    password = request.form.get("password")

    # Validate credentials
    if username == dummy_user["username"] and password == dummy_user["password"]:
        session["logged_in"] = True
        session["username"] = username
        return redirect(url_for("home"))
    else:
        # Invalid credentials
        return render_template("login.html", error="Invalid credentials. Try again.")

@app.route("/logout")
def logout():
    session.clear()  # Clear all session data
    return redirect(url_for("login"))

@app.route("/profile", methods=["GET", "POST"])
def profile():
    # TODO 4: Implement the profile route handler
    # GET: Show the profile form (prefill with existing data if available)
    # POST: Validate the form data, save it, and redirect to home on success
    #       On validation error, re-render the form with the error message
    pass

# TODO 5: Implement the JSON API endpoint for /api/profile
# Support GET and POST methods
# GET: Return the current user's profile as JSON
# POST: Accept JSON payload, validate it, save it, and return the result
# Handle authentication (401 if not logged in) and validation errors (400)
@app.route("/api/profile", methods=["GET", "POST"])
def api_profile():
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5000)
