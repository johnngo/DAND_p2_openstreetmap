
"""
Udacity Quiz: Improving Street Names
"""

from audit import street_type_re
import re

street_type_mapping = { "Rd.": "Road",
                        "Rd": "Road",
                        "St": "Street",
                        "St.": "Street" }

def update_street_name(value):
    """Clean street name values based on mapping.
    Args:
        value (str): raw street name value.
    Returns:
        value (str): cleaned street name value.
        None if data does not match expected format.
    """
    m = street_type_re.search(value)
    if m:
        if m.group() in street_type_mapping:
            startpos = value.find(m.group())
            value = value[:startpos] + street_type_mapping[m.group()]
        return value
    else:
        return None

