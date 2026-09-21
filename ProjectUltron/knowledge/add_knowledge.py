from database.database import Database


db = Database()


db.add(
    "Artificial Intelligence",
    "Artificial Intelligence is the field of creating systems capable of performing tasks that normally require human intelligence."
)

db.add(
    "Machine Learning",
    "Machine Learning is a branch of Artificial Intelligence where systems learn patterns from data."
)

db.add(
    "Neural Networks",
    "Neural Networks are computational models inspired by interconnected biological neurons."
)

db.add(
    "Robotics",
    "Robotics is the field of designing, building and controlling robots."
)


print("Knowledge added successfully.")