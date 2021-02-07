# *-* coding: utf-8 *-*

import pytest
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(name="asdsd", header="asdasdfsd", footer="asdsdafadsd")
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(name="", header="", footer="")
    app.logout()


if __name__ == '__main__':
    pytest.main()
