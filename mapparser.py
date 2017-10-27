import xml.etree.cElementTree as ET
from collections import defaultdict

# return a dictionary of top level tags and their counts
def count_tags(filename):
        tags_dict = defaultdict(int)

        # iteratively parse the file
        for event, elem in ET.iterparse(filename):
            tags_dict[elem.tag] += 1
        return tags_dict