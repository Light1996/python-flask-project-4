from app import create_app

app = create_app()

from app.db.models import User
import pytest


@pytest.fixture(scope='module')
def createnewuser():
    user = User('noor', 'noor@gmail.com', '12345')
    return user


@pytest.fixture(scope='module')
def testingclient():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!
