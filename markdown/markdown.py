import re

def parse(markdown):
    # Get each line which is separated by \n.
    lines = markdown.split('\n')
    
    output = ''
    # All tags start at the beginning. So re.match() is the go to function.
    # Only two starting tags exist, headers and lists. If they don't exist, then do <p> tag.

    for line in lines:
        line = ApplyHeader(line)
        line = ApplyList(line)

def ApplyHeader(line):
    if re.match('###### (.*)', line):
            return '<h6>' + line[7:] + '</h6>'
    elif re.match('## (.*)', line):
        return '<h2>' + line[3:] + '</h2>'
    elif re.match('# (.*)', line):
        return '<h1>' + line[2:] + '</h1>'
    else:
        return line

def ApplyList(line):
    if re.match(r'\* (.*)', line):
        pass
    return line

def ApplyStrong(line):
    return line

def ApplyEmphasis(line):
    return line

def old_parse(markdown):
    # Splits given input by newline
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False

    # For every line in lines, find certain tags.
    for i in lines:
        # This applies header tags to the line.
        # Search criteria is if the line is preceded by a certain number of pound signs.
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'

        # This applies list tags to the line.
        # Criteria to search is if the line is preceded with a *
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        # This looks for <h, <ul, <p, <li tags. If none are found, then <p> tags are added.
        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        # This looks for double under scores. If found, <strong> tags are added.
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        # This looks for single under scores. If found, <em> tags are added.
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        # Added <ul> tag if the line is a list item
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        # Holds the line.
        res += i
        # Applies the final <ul> tag if its a list.
    if in_list:
        res += '</ul>'
        # Returns the final markup.
    return res
