from flask.ext.wtf import Form
from wtforms import StringField, SelectField, validators
from wtforms.validators import ValidationError

from sender import mongo


class NoChoicesSelectField(SelectField):
    def pre_validate(self, form):
        """We need to overwrite this to overpass the fact that we don't load
        this field's choices at init time
        """
        pass


class SendEmailForm(Form):
    first_name = StringField('first_name', [validators.data_required()])
    last_name = StringField('last_name', [validators.data_required()])
    email = StringField('email', [validators.email(), validators.data_required()])
    confirm_email = StringField('confirm_email', [validators.equal_to('email')])
    country = SelectField('country', [validators.data_required()])
    city = NoChoicesSelectField('city', [validators.data_required()])

    def validate_city(self, field):
        """We have to check that this city belongs to the selected country
        """
        cities = mongo.db.cities.find({'country': self.country.data})
        choices = [c['name'] for c in cities]
        if field.data not in choices:
            raise ValidationError('Invalid choice')
