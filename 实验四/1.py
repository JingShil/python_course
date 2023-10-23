def naughty_or_nice(data):
    naughty_count = 0
    nice_count = 0

    for month in data.values():
        for day in month.values():
            if day == 'Naughty':
                naughty_count += 1
            elif day == 'Nice':
                nice_count += 1

    if naughty_count > nice_count:
        return "Naughty!"
    elif nice_count > naughty_count:
        return "Nice!"
    else:
        return "Nice!"