def retry_request(url):
    while True:
        response = fetch(url)
        if response == 200:
            break