import requests
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru/",
        help="Request url"
    )

    parser.addoption(
        "--status",
        default=200,
        help="response status code"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_status_code(request):
    return request.config.getoption("--status")
