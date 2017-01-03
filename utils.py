def parse_form(form, args=[]):
    try:
        result = {}
        for arg in args:
            result[arg] = form.get(arg)
            if result[arg] is None:
                raise
        return result
    except:
        pass


def jsonify(records):
    return [{key: value for key, value in
             zip(r.keys(), r.values())} for r in records]
