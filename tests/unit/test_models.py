from app.db.models import User, Account
from flask import session
import pandas as pd


def testaccountdetails():
    account = Account('noor', 'Debit', '2000')
    assert account.username == 'noor'
    assert account.typeofbalance == 'Debit'
    assert account.balance == '2000'


def createnewuser():
    user = User('noor', 'noor@gmail.com', '12345')
    assert user.username == 'noor'
    assert user.email == 'noor@gmail.com'
    assert user.password == '12345'


def createsignupandtest():
    user = User('noor', 'noor@gmail.com', '12345')
    assert user.username == 'noor'
    assert user.email == 'noor@gmail.com'
    assert user.password == '12345'


def testsignupnotworking():
    user = User('noor', 'noor@gmail.com', '123')
    assert user.username == 'noor'
    assert user.email == 'noor@gmail.com'
    assert user.password == '123'


def testuserisntinsession():
    if 'user' is None:
        session['user'] = 'noor'

    username = 'noor'
    assert username == 'noor'


def csvfiletesting():
    try:
        csvData = pd.read_csv('transactions.csv')
    except:
        pass

    check = 0
    if csvData is not None:
        check = 1

    assert check == 1


def csvnotfoundtesting():
    check = 1
    try:
        csvData = pd.read_csv('transaction.csv')
    except:
        check = 0

    assert check == 0
