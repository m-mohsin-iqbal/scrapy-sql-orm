from database.connection import db
from database.models import AllData

class BooksPipeline(object):
    def process_item(self, item, spider):
            # create a new SQL Alchemy object and add to the db session
            record = AllData(title=item['title'],
                             description=item['description'],
                             price=item['price'],
                             image=item['image'],
                             imageurl=item['imageurl'])
            db.add(record)
            db.commit()
            return item
