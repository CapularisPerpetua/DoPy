import re


def prefix_from_config() -> bool:
    return True


def add_prefix() -> str:
    in_dict = {"@": 'context',
               "+": 'project',
               "due:": 'due_date'}
    dict_out = {v: k for k, v in in_dict.items()}
    return dict_out


def metadata_from_config() -> dict:
    in_dict = {"@": 'context',
               "+": 'project',
               "due:": 'due_date'}

    out_dict = {}
    for key, value in in_dict.items():
        out_key = key
        if out_key == '+':
            out_key = re.compile(r'^\+')
        else:
            out_key = "^" + out_key
            out_key = re.compile(out_key.encode('unicode-escape').decode())
        out_dict.update({out_key: value})

    return out_dict


def parse_description(description_in: str) -> dict:
    description_out = {}
    meta_dict = metadata_from_config()
    desc_no_meta = []
    for token in description_in.split(' '):
        meta_match = False
        for meta_regex in meta_dict.keys():
            if meta_regex.match(token):
                meta_match = True
                new_token = re.sub(meta_regex, '', token)
                description_out.update({meta_dict[meta_regex]: new_token})
                break
        if not meta_match:
            desc_no_meta.append(token)
    desc_str_out = ' '.join(desc_no_meta)
    description_out.update({'description': desc_str_out})
    return description_out


def parse_from_txt(line_in: str) -> dict:
    item_out = {}
    split_line = line_in.split(' ')
    if split_line[0] == 'x':
        item_out.update({'completed': True})
        assert 'x' == split_line.pop(0)   
    else:
        item_out.update({'completed': False})

    prior = re.compile(r'^\([a-zA-Z]\)$')
    if prior.match(split_line[0]):
        item_out.update({'priority': split_line[0]})
        assert item_out['priority'] == split_line.pop(0)
    else:
        item_out.update({'priority': 'N/A'})

    if item_out['completed'] and prefix_from_config():
        item_out.update({'completion date': split_line[0]})
        assert item_out['completion date'] == split_line.pop(0)

    if prefix_from_config():
        item_out.update({'creation date': split_line[0]})
        assert item_out['creation date'] == split_line.pop(0)

    item_out.update(parse_description(' '.join(split_line)))

    return item_out


def to_txt(item_out: dict) -> str:
    output_list = []
    prefix_list = ['completed',
                   'priority',
                   'completion date',
                   'creation date',
                   'description']
    if item_out['completed']:
        output_list.append('x')

    if item_out['priority'] != 'N/A':
        output_list.append(item_out['priority'])
    if item_out['completed'] and prefix_from_config():
        output_list.append(item_out['completion date'])

    if prefix_from_config():
        output_list.append(item_out['creation date'])

    output_list.append(item_out['description'])

    for key in item_out.keys():
        if key not in prefix_list:
            output_list.append(add_prefix()[key] + item_out[key])

    return ' '.join(output_list)
