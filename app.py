from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.Date, nullable=False, default=date.today)
    
@app.route("/delete_task/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"status": "ok"})
    except:
        return jsonify({"status": "error"}), 500
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks/<string:date_str>")
def tasks_by_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    tasks = Task.query.filter_by(due_date=date_obj).all()
    return jsonify([{"id": t.id, "content": t.content} for t in tasks])

@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.get_json()
    task = Task(content=data["content"], due_date=datetime.strptime(data["due_date"], "%Y-%m-%d").date())
    db.session.add(task)
    db.session.commit()
    return jsonify({"status": "ok"})

@app.route("/events")
def events():
    tasks = Task.query.all()
    events = [{"title": t.content, "start": str(t.due_date)} for t in tasks]
    return jsonify(events)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
