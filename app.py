from flask import Flask, render_template, request, redirect
from content import *

app = Flask(__name__)


@app.route("/")
def entries():
    return render_template('index.html', entries=get_all_entries())

@app.route("/entry/<name>")
def entry(name):
    return render_template('entry.html', entry=get_entry(name))

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/admin/add", methods=['POST', 'GET'])
@app.route("/admin/edit/<name>", methods=['POST', 'GET'])
def add_entry(name=None):
    if request.method == 'POST':
        save_entry(
            request.form['name'],
            request.form['title'],
            request.form['content']
        )
        return redirect('/entry/{}'.format(request.form['name']))
    if name:
        entry = get_entry(name)
    else:
        entry = None
    return render_template('entry_form.html', entry=entry)

@app.route("/admin/delete/<name>", methods=['POST', 'GET'])
def delete_entry(name):
    if request.method == 'POST':
        delete_file_entry(name)
        return redirect('/')
    entry = get_entry(name)
    return render_template('entry_delete.html', entry=entry)