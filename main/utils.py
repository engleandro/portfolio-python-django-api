from subprocess import run as subprocess_run
from typing import Dict, List

from django.urls import get_resolver, reverse
from requests import get as requests_get


def read_from_system_command(
    command: List[str] = ["pwd"], encoding: str = "utf-8"
) -> str:
    return subprocess_run(command, capture_output=True).stdout.decode(encoding).strip()


def get_aws_public_ip() -> str:
    command = ["wget", "http://checkip.amazonaws.com"]
    return read_from_system_command(command=command)


def get_all_viewnames() -> Dict[str, str]:
    return get_resolver().reverse_dict


def get_urls_by_viewname(viewname: str) -> List[str]:
    return reverse(viewname)


def get_ping(
    protocol: str = "http",
    hostname: str = "localhost",
    port: int = 8000,
    url: str = "ping/",
) -> str:
    try:
        response = requests_get(
            f"{protocol}://{hostname}:{port}/{url}",
            timeout=5,
            allow_redirects=False,
        )
    except Exception:
        return False

    if response.status_code == 200 and response.text == "pong!":
        return True
    return False
