from typing import Mapping


def parse_request_parameters_into_mongo_filter(request) -> dict:
    filters = {}
    for parameter, value in request.items():
        open_bracket = parameter.find("[")
        if open_bracket != -1:
            close_bracket = parameter.find("]")
            key = parameter[:open_bracket]
            filter_key = parameter[open_bracket + 1:close_bracket]
            filter = {key: {"$" +filter_key: float(value)}}
        else:
            filter = {parameter: value}
        filters.update(filter)
    return filters

