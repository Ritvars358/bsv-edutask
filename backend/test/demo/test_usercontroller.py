import pytest
from unittest.mock import Mock
from src.controllers.usercontroller import UserController


def testGetUserByEmailUserExists():
    dao = Mock()
    dao.find.return_value = [{"email": "test@mail.com"}]

    controller = UserController(dao)
    result = controller.get_user_by_email("test@mail.com")

    assert result == {"email": "test@mail.com"}


def testGetUserByEmailUserNotFound():
    dao = Mock()
    dao.find.return_value = []

    controller = UserController(dao)
    result = controller.get_user_by_email("missing@mail.com")

    assert result is None


def testGetUserByEmailMultipleUsers():
    dao = Mock()
    dao.find.return_value = [
        {"email": "test@mail.com", "name": "User 1"},
        {"email": "test@mail.com", "name": "User 2"}
    ]

    controller = UserController(dao)
    result = controller.get_user_by_email("test@mail.com")

    assert result == {"email": "test@mail.com", "name": "User 1"}


def testGetUserByEmailInvalidEmail():
    dao = Mock()
    controller = UserController(dao)

    with pytest.raises(ValueError):
        controller.get_user_by_email("invalidemail")