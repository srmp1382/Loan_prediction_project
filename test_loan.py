from loan_prediction import app
import pytest
@pytest.fixture
def client():
    return app.test_client()
def test_home(client):
    resp=client.get('/')
    assert resp.text=="This is my nice home page\n I am still learning it"
def test_new(client):
    resp=client.get('/test_page')
    assert resp.text=="This is a test page\nCheck if this works"
def test_pred(client):
    data_test={
        "Gender":"Male",
        "Married":"Yes",
        "Dependents":2,
        "Education":"Graduate",
        "Self_Employed":"No",
        "ApplicantIncome":70,
        "CoapplicantIncome":5.0,
        "Loan_Amount":700000.0,
        "Loan_Amount_Term":360.0,
        "Credit_History":1,
        "Property_Area":"Urban"
    }
    resp=client.post('/display', json=data_test)
    assert resp.text=="rejected"
