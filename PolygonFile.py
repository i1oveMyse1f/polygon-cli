class PolygonFile:
    def __init__(self):
        self.name = None
        self.type = None
        self.date = None
        self.size = None
        self.remove_link = None
        self.download_link = None
        self.edit_link = None

    def __repr__(self):
        return str(self.__dict__)

    def by_dict(self, data):
        for key in data.keys():
            if key != '__type':
                setattr(self, key, data[key])

    def normalize(self, session):
        """

        :type session: problem.ProblemSession
        """
        assert self.remove_link
        assert self.download_link
        assert self.edit_link
        self.remove_link = session.make_link(self.remove_link, ssid=True)
        self.download_link = session.make_link(self.download_link, ssid=True)
        self.edit_link = session.make_link(self.edit_link, ssid=True)
