#
# Make it so it has one, shared attribute with other items called"content"
#
class GithubItem:
    def __init__(self, event_type, payload):
        self.event_type = event_type
        self.payload = payload
        # print(f"{__class__.__name__} created!")
