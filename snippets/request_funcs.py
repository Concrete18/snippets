import requests, time
import datetime as dt


def request_url(self, url, headers=None, second_try=False):
    """
    Quick data request with check for success.
    """
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        if second_try:
            return False
        msg = "Connection Error: Internet can't be accessed"
        self.error_log.warning(msg)
        time.sleep(5)
        self.request_url(url, headers, second_try=True)
        return False
    if response.status_code == requests.codes.ok:
        return response
    elif response.status_code == 500:
        msg = "Server Error: make sure your api key and steam id is valid."
        self.error_log.warning(msg)
    elif response.status_code == 404:
        msg = f"Server Error: 404 Content does not exist. URL: {url}"
        self.error_log.warning(msg)
    elif response.status_code == 429:
        msg = "Server Error: Too Many reqeuests made. Waiting to try again."
        self.error_log.warning(msg)
        self.error_log.warning(response)
        time.sleep(5)
        self.request_url(url, headers)
    else:
        msg = f"Unknown Error: {response.status_code}"
        self.error_log.warning(msg)
    return False


def api_sleeper(self, api, sleep_length=0.5, api_calls={}) -> None:
    """
    Delays delays for a set period of time if the `api` was run too recently.
    Delay length is set by `sleep_length`.
    """
    cur_datetime = dt.datetime.now()
    if api in api_calls.keys():
        if api_calls[api] + dt.timedelta(seconds=sleep_length) > cur_datetime:
            time.sleep(sleep_length)
    api_calls[api] = cur_datetime
