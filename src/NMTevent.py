class NMTevent:
    """each instantiation of this class represents ONE event"""
    name = "no name given"
    date = "no date given"
    time = "no time given"
    description = "no description given"
    URL = "no url given"
    location = "no location given"

    def __init__(self, raw_event, link, date):
        """"initialize an event obj given the raw html, url, and ugly date string"""
        self.name = self.parse_name(raw_event)
        self.date = date.split(",")[0]  # TODO: split this a different way and then call datetime
        self.time = date.split(",")[1]
        self.description = self.parse_des(raw_event)
        self.url = link
        self.location = "NMT"   #temp

    def parse_name(self, raw_event):
        """"get the name of the event"""
        text = raw_event.a['title']
        return text.split("::")[0]

    def parse_des(self, raw_event):
        """"get the description of the event"""
        text = raw_event.a['title']
        return text.split("::")[1]

    def pretty(self):
        """"debugging purposes, pretty print"""
        print "name:        ", self.name
        print "description: ", self.description
        print "date:        ", self.date
        print "time:        ", self.time
