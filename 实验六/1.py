def count_developers(lst):
    return len(list(filter(lambda x: x['continent'] == 'Europe' and x['language'] == 'JavaScript', lst)))