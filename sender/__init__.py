from flask import (Flask, render_template, request, redirect, url_for,
                   session, jsonify, flash)
from flask.ext.pymongo import PyMongo
from sendgrid import SendGridClient, Mail, SendGridError


app = Flask(__name__)
app.config.from_object('config')
mongo = PyMongo(app)
sendgrid = SendGridClient(app.config['SENDGRID_USERNAME'],
                          app.config['SENDGRID_PASSWORD'],
                          raise_errors=True)


from forms import SendEmailForm


DEFAULT_EMAIL_TEXT = """This is an e-mail sent from sample-email-sender

Here is the sent info:
first_name: %s
last_name: %s
country: %s
city: %s

Goodbye!"""


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SendEmailForm()

    # Dynamically set choices as they are fetched from MongoDB
    form.country.choices = [('', 'Select...')] + [(c['name'], c['name'])
        for c in mongo.db.countries.find()]
    form.city.choices = []

    # Since cities are loaded via AJAX, the following must be done to ensure
    # the options are preserved on the field
    if form.country.data:
        cities = mongo.db.cities.find({'country': form.country.data})
        form.city.choices = [(c['name'], c['name']) for c in cities]

    if form.validate_on_submit():
        session['form'] = form.data
        return redirect(url_for('confirm'))
    return render_template('index.html', form=form)


@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if 'form' not in session:
        flash('You should fill out the form first...')
        return redirect(url_for('index'))
    if request.method == 'POST':
        data = session['form']
        text = DEFAULT_EMAIL_TEXT % (data['first_name'], data['last_name'],
                                     data['country'], data['city'])
        message = Mail(to=data['email'],
                       subject='E-mail from sample-email-sender',
                       text=text,
                       from_email=app.config['DEFAULT_FROM_EMAIL'])
        try:
            sendgrid.send(message)
        except SendGridError:
            flash('Oups, an error stopped us from sending your e-mail!')
        else:
            flash('Hooray, your e-mail has been sent!')
        # Be sure to wipe the session data since it is no longer needed
        del session['form']
        return redirect(url_for('index'))
    return render_template('confirm.html', data=session['form'])


@app.route('/_get_cities/<country>')
def _get_cities(country):
    cities = mongo.db.cities.find({'country': country})
    return jsonify(cities=[c['name'] for c in cities])
