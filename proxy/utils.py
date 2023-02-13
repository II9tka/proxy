import re


def retry_if_connection_error(exception):
    return isinstance(exception, ConnectionError)


def update_html(html: bytes):
    patterns = (
        ('BlackHub', re.compile('black', re.IGNORECASE)),
        ('Games', re.compile('russia', re.IGNORECASE))
    )

    html = html.decode()

    for phrase, pattern in patterns:
        html = pattern.sub(phrase, html)

    return html.encode()
