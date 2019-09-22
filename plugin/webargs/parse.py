import functools
from webargs.flaskparser import use_args

parse_reqs = use_args

parse_query = functools.partial(parse_reqs, locations=("query",))
parse_body = functools.partial(parse_reqs, locations=("json", "form", "query"))
parse_data = functools.partial(parse_reqs, locations=("form",))
parse_json = functools.partial(parse_reqs, locations=("json",))
parse_files = functools.partial(parse_reqs, locations=("files",))
parse_headers = functools.partial(parse_reqs, locations=("headers",))
