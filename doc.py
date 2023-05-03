from bs4 import BeautifulSoup as bs
from element import Element

class Doc:
    """Represents a HTML document object.
        This class is simply a wrapper around
        bs4's 'soup' instance with some added 
        functionality
    """    
    
    def __init__(self, raw):
        """Creates an instance of 'Doc'

        Args:
            raw (string): the raw HTML data to parse into document
        """        
        
        self.__type__ = 'Doc'
        self.parsed = bs(raw, 'html.parser')
        
    def querySelector(self, sel):
        """Select element within the HTML by tagName, id or class

        Args:
            sel (string): a valid element selector

        Returns:
            Element | None: an instance of 'Element' (if found) or else 'None'
        """        
        if sel[0] == '#':
            try:
                return Element(self.parsed.find(id=sel[1:]))
            except Exception as e:
                return None
        if sel[0] == '.':
            try:
                return Element(self.parsed.find(class_=sel[1:]))
            except Exception as e:
                return None
        try:
            return Element(self.parsed.find(sel))
        except Exception as e:
            return None
        