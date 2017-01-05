from sanic.exceptions import ServerError

def parse_form(form, args=[]):
    try:
        result = {}
        for arg in args:
            if not form.get(arg) is None:
                result[arg] = form.get(arg)
        if set(result.keys()) != set(args):
            raise
        return result
    except:
        raise ServerError(f'Missing argument: {[arg for arg in list(set(args) - set(result.keys()))]}')


def jsonify(records):
    return [{key: value for key, value in
             zip(r.keys(), r.values())} for r in records]
