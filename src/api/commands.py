
import click
from api.models import db, User, Vehicle
from api.data_models import DATA_INSTRUCTORS, DATA_VEHICLES

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    @app.cli.command("insert-test-users") # name of our command
    @click.argument("count") # argument of out command
    def insert_test_users(count):
        print("Creating test users")
        for x in range(1, int(count) + 1):
            user = User()
            user.email = "test_user" + str(x) + "@test.com"
            user.password = "123456"
            user.is_active = True
            db.session.add(user)
            db.session.commit()
            print("User: ", user.email, " created.")

        print("All test users created")

##

    @app.cli.command("insert-instructors")
    def insert_instructors():
        print("Creating instructors")

        for instructor_data in DATA_INSTRUCTORS:
            instructor = User(
                user_id=instructor_data["user_id"],
                email=instructor_data["email"],
                role=instructor_data["role"],
                first_name=instructor_data["first_name"],
                last_name=instructor_data["last_name"],
                phone_number=instructor_data["phone_number"],
            )
            instructor.set_password(instructor_data["password"])
            db.session.add(instructor)
        db.session.commit()
        print("All instructors created")


    @app.cli.command("insert-vehicles")
    def insert_instructors():
        print("Creating Vehicles")

        for vehicles_data in DATA_VEHICLES:
            vehicle = Vehicle(
                vehicle_type=vehicles_data["vehicle_type"],
                plate_number=vehicles_data["plate_number"],
                model=vehicles_data["model"],
                instructor_id=vehicles_data["instructor_id"],
            )
            db.session.add(vehicle)
        db.session.commit()
        print("All vehicles created")

