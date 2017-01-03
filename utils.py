def parse_form(form, args=[]):
    try:
        result = {}
        for arg in args:
            result[arg] = form.get(arg)
            if result[arg] == None:
                raise
        return result
    except:
        pass