def render_fields_list(*items):
    ret = '\n Available fields:\n'
    for item in items:
        ret += '%s \n' % item
    return ret
