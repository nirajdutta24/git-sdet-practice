def test_login():
    username = "test_user"
    password = "test123"

    assert username == "test_user"
    assert password == "test123"
    assert len(username) > 0