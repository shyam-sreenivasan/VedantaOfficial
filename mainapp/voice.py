from mediawiki import MediaWiki
from .data import get_chapter, get_next

def query_wiki(name, query_str):
    response = {"context": name, 'meta': {}}
    wikipedia = MediaWiki()
    p = wikipedia.page(name)
    if 'who' in query_str:
        response['speechText'] = p.summary
        response['sections'] = p.sections
        images = [img for img in p.images if img.endswith('png') or img.endswith('jpg')]
        if len(images) > 8:
            images = images[:8]
        response['meta']['images'] = images
    else:
        sections = p.sections
        for s in sections:
            print ('checking {} and {}'.format(s.lower(), query_str.lower()))
            if s.lower() == query_str.strip().lower():
                query_str = s
                break
        # response['meta']['images'] = [ img for img in p.images if img.endswith('png') or img.endswith('jpg')]
        response['speechText'] = p.section(query_str)
        response['sections'] = sections
    return response


def query_story(name, query_str):
    story = {
        "speechText": "Abraham Lincoln was born on February 12, 1809, the second child of Thomas Lincoln and Nancy Hanks Lincoln, in a log cabin on Sinking Spring Farm near Hodgenville, Kentucky. He was a descendant of Samuel Lincoln, an Englishman who migrated from Hingham, Norfolk, to its namesake, Hingham, Massachusetts, in 1638. The family then migrated west, passing through New Jersey, Pennsylvania, and Virginia. Lincoln's paternal grandparents, his namesake Captain Abraham Lincoln and wife Bathsheba (née Herring) moved the family from Virginia to Jefferson County, Kentucky.[b] The captain was killed in an Indian raid in 1786.[7] His children, including eight-year-old Thomas, Abraham's father, witnessed the attack.Thomas then worked at odd jobs in Kentucky and Tennessee before the family settled in Hardin County, Kentucky, in the early 1800s.  The heritage of Lincoln's mother Nancy remains unclear, but it is widely assumed that she was the daughter of Lucy Hanks. Thomas and Nancy married on June 12, 1806, in Washington County, and moved to Elizabethtown, Kentucky.[11] They had three children: Sarah, Abraham, and Thomas, who died as infant.",
        "command": "python parser.py clipify 'Abraham Lincoln' 'Early life' -p 'Hodgenville, Kentucky':'Hingham, Massachusetts':'Hardin County, Kentucky':'Elizabethtown, Kentucky':Indiana:'Little Pigeon Creek Community' -i 'Nancy'",
        "clips": get_chapter(name),
        "next" : get_next(name)
    }

    return story
