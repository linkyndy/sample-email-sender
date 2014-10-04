from flask.ext.script import Manager, Server

from sender import app, mongo


manager = Manager(app)
manager.add_command("runserver", Server())


@manager.command
def bootstrap():
    # Wipe everything out
    mongo.db.countries.drop()
    mongo.db.cities.drop()

    # Add some data to MongoDB
    countries = [{'name': 'Romania', 'abbrev': 'ro'},
                 {'name': 'France', 'abbrev': 'fr'},
                 {'name': 'Germany', 'abbrev': 'de'},
                 {'name': 'Italy', 'abbrev': 'it'}]
    cities = [{'name': 'Timisoara', 'country': 'ro'},
              {'name': 'Constanta', 'country': 'ro'},
              {'name': 'Paris', 'country': 'fr'},
              {'name': 'Nice', 'country': 'fr'},
              {'name': 'Nantes', 'country': 'fr'},
              {'name': 'Berlin', 'country': 'de'},
              {'name': 'Rome', 'country': 'it'},
              {'name': 'Pisa', 'country': 'it'}]
    mongo.db.countries.insert(countries)
    mongo.db.cities.insert(cities)


if __name__ == "__main__":
    manager.run()
