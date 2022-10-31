from datetime import date, time, datetime

from flask.json import JSONEncoder


class LayoutPI:
    website_name = "Website name"
    short_website_name = "Short website name"

    def __init__(self, title):
        self.title = title


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                return obj.strftime("%Y-%m-%d %H:%M")
            elif isinstance(obj, date):
                return obj.strftime("%Y-%m-%d")
            elif isinstance(obj, time):
                return obj.strftime("%H:%M")
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def add_parameters_to_url(url, parameters):
    if "?" in url:
        url += "&"
    else:
        url += "?"
    for key, value in parameters.items():
        url += str(key) + "=" + str(value) + "&"
    url = url[:-1]
    return url


def get_next_url(args, parameters={}, default_url=""):
    next_url = args.get("next", default_url)
    if next_url:
        next_url = add_parameters_to_url(next_url, parameters)
    return next_url


def get_updated_fields(new_values, db_object):
    ret = {}
    old_values = db_object.to_dict()
    for key, value in new_values.items():
        if key in old_values.keys() and value != old_values[key]:
            ret[key] = {"new": value, "old": old_values[key]}
    return ret


def set_parameters_of_url(url, parameters: dict):
    url_args = []
    if "?" in url:
        args_part = url[url.find("?") + 1:]
        url = url[:url.find("?")]
        url_args = [a.split("=") for a in args_part.split("&")]
    url += "?"

    for key, value in url_args:
        if key not in parameters.keys():
            url += f"{key}={value}&"

    for key, value in parameters.items():
        url += f"{key}={value}&"

    url = url[:-1]
    return url
