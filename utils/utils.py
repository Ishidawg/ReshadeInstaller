import urllib.request
import ssl
import certifi


def generic_download(url: str, directory: str) -> None:
    context: ssl.SSLContext = ssl.create_default_context(
        cafile=certifi.where())
    req: urllib.request.Request = urllib.request.Request(
        url, headers={'User-Agent': 'Chrome/120.0.0.0'})

    try:
        with urllib.request.urlopen(req, context=context) as res:
            with open(directory, "wb") as file:
                file.write(res.read())
    except Exception as e:
        raise IOError(f"Failed to download: {e}") from e
