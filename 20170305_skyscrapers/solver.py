def solve_scrapers(hints):
    pass


def visible_count(view):
    top = view[0]
    view_ct = 0
    for building in view:
        if building >= top:
            view_ct += 1
            top = building
    return view_ct