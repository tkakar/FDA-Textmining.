
class DataElement(object):
    
    def __init__(self,extractedField=None, charOffset=None, extractorName=None):
        self.extractedField = extractedField
        self.charOffset = charOffset
        self.extractorName = extractorName

    def getExtractedField(self):
        return self.extractedField

    def setExtractedField(self,extractedField):
        self.extractedField = extractedField

    def getCharOffset(self):
        return self.charOffset

    def setCharOffset(self,charOffset):
        self.charOffset = charOffset

    def getExtractorName(self):
        return self.extractorName

    def setExtractorName(self,extractorName):
        self.extractorName = extractorName