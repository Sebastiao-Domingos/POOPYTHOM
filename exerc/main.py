from repository import Repository
from databases import PostgesDB


db_con = PostgesDB()

rep = Repository()

print("==="*15)

rep.insert(db_con)
print("==="*15)
rep.delete(db_con)
print("==="*15)
rep.select(db_con)