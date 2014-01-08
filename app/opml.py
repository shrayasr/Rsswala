import xml.etree.ElementTree as e

class OpmlParser:

    # Initialize the class with the path to the OPML file
    def __init__(self,opmlFilePath):

        # It parses the OPML file and stores the tree
        self.tree = e.parse(opmlFilePath)

        # Declare an empty list that holds the list of feedURLs within the
        # OPML file
        self.feedUrls = []

    # Parse the OPML file and return the list of links
    def parse(self):

        # From the tree, get the root of the XML
        root = self.tree.getroot()

        # Pick up the "body" tag
        body = root.findall('body')[0]

        # Get all instances of "outline" tags
        outlines = body.findall('outline')

        # Parse the outlines and get a list of feed urls
        self.feedUrls = self.parseOutlines(outlines)

        # Return the list of feed URLs
        return self.feedUrls
        
    # Parse the outlines. There can be outlines within outlines and hence this
    # is a RECURSIVE function
    def parseOutlines(self,outlineToParse):

        # A list to hold the feedURLs inside the individual outline tags
        outlineFeedURLs = []

        # Go through each of the outlines
        for outline in outlineToParse:

            # Get the children of the outlines
            outlineChildren = outline.getchildren()

            # If they have children,
            if len(outlineChildren) > 0:

                # Parse those children, and extend the current list of 
                # feedURLs with the one that is returned
                outlineFeedURLs.extend(self.parseOutlines(outline))

            # If they dont have children,
            else:
                    
                # If they have the attribute 'xmlUrl' in them
                if 'xmlUrl' in outline.attrib:
                    
                    # Append the xmlUrl value to the list of feedURLs
                    outlineFeedURLs.append(outline.attrib['xmlUrl'])
                        
        # Return the list of feedURLs
        return outlineFeedURLs
