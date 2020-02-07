class StackOverflowItem:
    def __init__(self, content):
    	# TODO, parser here:
    	# - Creation date
    	# - link
    	# - display_name
    	# - event name (post type)
    	# - description(???)
    	self.created_at = content['creation_date']
    	self.link = content['link']
    	self.actor = content['owner']['display_name']
    	self.event_type = content['post_type']
    	self.description = ""
    	print(f"{__class__.__name__} created!")