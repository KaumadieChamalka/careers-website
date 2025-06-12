from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': '10,00,000',
    'currency': 'Rs'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': '15,00,000',
    'currency': 'Rs'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '120,000',
    'currency': '$'
}]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


@app.route("/job/<id>")
def show_job(id):
    job = JOBS[int(id) - 1]
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    job = JOBS[int(id) - 1]
    return render_template('application_submitted.html',
                           application=data,
                           job=job)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
