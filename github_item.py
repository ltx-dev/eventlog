#
# Implement some sort of parser?
#
class GithubItem:
    def __init__(self, content):
        # TODO, parser here:
        # - created_at
        # - link (repo -> url)
        # - actor (display login)
        # - type (event name)
        # - description(commit message)
        self.created_at = content['created_at'] # needs converting to one date format
        self.link = content['payload']['commits'][0]['url'] # need to convert to html version
        self.actor = content['actor']['display_login']
        self.event_type = content['type']
        self.description = content['payload']['commits'][0]['message']
        print(f"{__class__.__name__} created!")


    def print_all():
        print("Print called")
        print(self.created_at)        
        print(self.link)        
        print(self.actor)        
        print(self.type)        
        print(self.description)        
