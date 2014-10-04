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
    countries = [{'name': 'Romania'},
                 {'name': 'France'},
                 {'name': 'Germany'},
                 {'name': 'Italy'}]
    cities = [{'name': 'Timisoara', 'country': 'Romania'},
              {'name': 'Constanta', 'country': 'Romania'},
              {'name': 'Paris', 'country': 'France'},
              {'name': 'Nice', 'country': 'France'},
              {'name': 'Nantes', 'country': 'France'},
              {'name': 'Berlin', 'country': 'Germany'},
              {'name': 'Rome', 'country': 'Italy'},
              {'name': 'Pisa', 'country': 'Italy'}]
    mongo.db.countries.insert(countries)
    mongo.db.cities.insert(cities)


if __name__ == "__main__":
    manager.run()
