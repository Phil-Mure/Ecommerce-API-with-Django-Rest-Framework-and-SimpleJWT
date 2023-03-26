import uuid


#Creating Slug
def slug_config(tracenumber):
    someuuid1 = str(uuid.uuid4())[9:13]
    someuuid2 = str(uuid.uuid4())[-1]
    slug = "{a}{b}{c}".format(a=tracenumber, b=someuuid1, c=someuuid2)
    return slug