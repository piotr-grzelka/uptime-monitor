from ..models import Service


def test_service_unicode():
    model = Service(name="testowa")
    assert str(model) == "testowa"
