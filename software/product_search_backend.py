import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#cred = credentials.Certificate('/Users/carolwang/Downloads/ikeaproducts-ba6c4-firebase-adminsdk-oea4f-cecb811593.json')  
cred = credentials.Certificate('/home/zetabeta/Downloads/ikeaproducts-ba6c4-firebase-adminsdk-oea4f-cecb811593.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# adds a product to the db
def add_product(document_id: str, name: str, aisle: int, bin: int):
    doc_ref = db.collection('IkeaProducts').document(document_id)
    doc_ref.set({
        'name': name,
        'aisle': aisle,
        'bin': bin
    })

# deletes a product from the db
def delete_product(document_id: str):
    doc_ref = db.collection('IkeaProducts').document(document_id)
    doc_ref.delete()

# edits the information of a product from the db
def edit_product(document_id: str, name: str, aisle: int, bin: int):
    doc_ref = db.collection('IkeaProducts').document(document_id)
    doc_ref.set({
        'name': name,
        'aisle': aisle,
        'bin': bin
    })

# gets all products from the db
def get_all_products():
    products_ref = db.collection('IkeaProducts')
    docs = products_ref.stream()
    return docs

# prints all documents in the db
'''
docs = get_all_products()
for doc in docs:
    print(f'{doc.id}: {doc.to_dict()}')
'''

# gets the aisle and bin that correspond to document_id to display on the ui
def find_aisle_bin(document_id: str):
    doc_ref = db.collection('IkeaProducts').document(document_id)
    doc = doc_ref.get()

    if doc.exists:
        data = doc.to_dict()
        aisle = data.get('aisle')
        bin = data.get('bin')
        return aisle, bin
    else:
        return None, None 
    
# gets the tag_id and bin that correspond to document_id for robot nagvigation
def find_tag_id_bin(document_id: str):
    doc_ref = db.collection('IkeaProducts').document(document_id)
    doc = doc_ref.get()

    if doc.exists:
        data = doc.to_dict()
        tag_id = data.get('tag_id')
        bin = data.get('bin')
        return tag_id, bin
    else:
        return None, None 

