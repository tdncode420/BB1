from bs4 import Tag

class Element:
    """Represents a HTML DOM Element object
        Used privately within lib, not recommended to use directly
    """

    def __init__(self, bs4_element_tag):
        """Creates an instance of 'Element'

        Args:
            bs4_element_tag (_type_): _description_
        """     
        self._ = bs4_element_tag

    def hasAttribute(self, attr):
        """Checks the element for a specific attribute

        Args:
            attr (string): the attribute to look for
        Returns:
            bool: Indicates whether or not the attribute was found or not
        """
        return attr in self._.attrs

    def getAttribute(self, attr):
        """Returns the value of the elements attribute (if available)

        Args:
            attr (string): the attribute to look for

        Returns:
            string | None: the value of the attribute or else None (if not found)
        """
        if self.hasAttribute(attr):
            return self._[attr]
        return None

    def hasChild(self, sel, recursive=False):
        """Check this element's children elements for an element
        specified by the passed in selector ('sel'). By default,
        this method only checks elements nested at the first level.
        To check all nested elements, pass in 'recursive=true'

        Args:
            sel (string): a valid element selector
            recursive (bool, optional): Search through all nested children elements. Defaults to False.

        Returns:
            bool: Indicates whether or not the child element was found or not
        """
        if recursive:
            eles = list(filter(lambda x: isinstance(
                x, Tag), self._.descendants))
        else:
            eles = list(filter(lambda x: isinstance(
                x, Tag), self._.contents))

        if sel[0] == '#':
            for ele in eles:
                if ele['id'] == sel[1:]:
                    return True
        elif sel[0] == '.':
            for ele in eles:
                if ele['class'] == sel[1:]:
                    return True
        else:
            for ele in eles:
                if ele.name.lower() == sel.lower():
                    return True
        return False

    def querySelector(self, sel):
        """Select element nested within this instances' 
            '_' property by tagName, id or class

        Args:
            sel (string): a valid element selector

        Returns:
            Element | None: an instance of 'Element' (if found) or else 'None'
        """
        eles = list(filter(lambda x: isinstance(
            x, Tag), self._.descendants))
        if sel[0] == '#':
            for ele in eles:
                if 'id' in ele and ele['id'] == sel[1:]:
                    return Element(ele)
        if sel[0] == '.':
            for ele in eles:
                if 'class' in ele and ele['class'] == sel[1:]:
                    return Element(ele)
        for ele in eles:
            if ele.name.lower() == sel.lower():
                return Element(ele)
        return None
