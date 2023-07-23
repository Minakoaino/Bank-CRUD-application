import pytest
from app import app, db
from app.models import Bank

# Set up testing client and database
@pytest.fixture(scope='module')
def test_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
        yield testing_client  # this is where the testing happens!
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_create_bank(test_client):
    # Mock form data
    mock_form_data = {
        'name': 'Test Bank',
        'location': 'Test Location'
    }
    response = test_client.post('/bank/create', data=mock_form_data)
    assert response.status_code == 302  # Should redirect to the list of banks

def test_list_banks(test_client):
    response = test_client.get('/banks')
    assert response.status_code == 200
    assert b'Test Bank' in response.data  # Check that the bank created in the previous test is present

def test_view_bank(test_client):
    # Get the first bank in the database (this should be the bank created in test_create_bank)
    bank = Bank.query.first()
    response = test_client.get(f'/bank/{bank.id}')
    assert response.status_code == 200
    assert b'Test Bank' in response.data  # Check that the correct bank is being displayed

def test_update_bank(test_client):
    # Get the first bank in the database (this should be the bank created in test_create_bank)
    bank = Bank.query.first()
    # Mock form data
    mock_form_data = {
        'name': 'Updated Bank',
        'location': 'Updated Location'
    }
    response = test_client.post(f'/bank/update/{bank.id}', data=mock_form_data)
    assert response.status_code == 302  # Should redirect to the view of the updated bank
