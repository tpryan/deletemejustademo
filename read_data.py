import firebase_admin
from google.cloud import firestore

db = firestore.Client()

def add_document(employee, walk_count):
    walkers_ref = db.collection(u'dog_walkers')

    walkers_ref.add({
        u'employee': employee,
        u'walk_count': walk_count
    })
    
def add_data():
    walkers_ref = db.collection(u'dog_walkers')

    walkers_ref.document(u'jen_doc').set({
        u'employee': u'Jen',
        u'walk_count': 2
    })

    add_document('Alex', 6)
    add_document('Priyanka', 2)
    add_document('Jen', 1)
    add_document('Terry', 5)
    add_document('Yufeng', 3)

add_data()
