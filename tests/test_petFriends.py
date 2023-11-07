import os
from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_post_new_friends(name='tuz', animal_type='dog', age='3', pet_photo='images/tuz.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_friends(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_post_new_friends_2(name='tuz', animal_type='dog', age='3', pet_photo='images/tuz.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_friends(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['animal_type'] == animal_type

def test_post_new_friends_3(name='tuz', animal_type='dog', age='3', pet_photo='images/tuz.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_friends(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['age'] == age

def test_post_new_friends_4(name='tuz', animal_type='dog', age='2', pet_photo='images/tuz.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_friends(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['pet_photo'] != pet_photo

def test_delete_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.post_new_friends(auth_key, "drug", "dog", "2", "images/drug.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()

def test_delete_pet_2(name='tuz', animal_type='star', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.put_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert name not in pet_id

def test_delete_pet_3(name='tuz', animal_type='star', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.put_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert animal_type not in pet_id

def test_put_self_pet_info(name='tuzdog', animal_type='dog', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.put_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_put_self_pet_info_2(name='tuz', animal_type='dog_dog', age='3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.put_pet_info(auth_key, my_pets['pets'][1]['id'], name, animal_type, age)
    assert status == 200
    assert result['animal_type'] == animal_type

def test_put_self_pet_info_3(name='tuz', animal_type='dog', age='700'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.put_pet_info(auth_key, my_pets['pets'][2]['id'], name, animal_type, age)
    assert status == 200
    assert result['age'] == age