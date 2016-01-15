Hipster
=======

Simple Python module for the HipChat API

Description
-----------

Simple Python library for the `HipChat API <https://www.hipchat.com/docs/api>`. 

Dependencies
------------
Standart library and urllib3

Python version
------------
 2.6, 2.7

Usage
-----

Install::

```bash
git clone https://github.com/a2design-company/hipster
python setup.py install
````

Instantiate::
```python
from hipster import Hipster
# Provide optional proxy url or alternate API url if you are behind a
# proxy and/or have a self-hosted HipChat server, e.g.
hipchat = Hipster(Your token, [[proxy=PROXY_URL], [api_url=API_URL]])
```

Call API methods::

```python
hipchat.create_room(name='My room', owner_user_id=1, topic='Hello, room!')
```
or

```python
hipchat.create_room({
 'name': 'My another room',
 'owner_user_id': 1,
 'topic': 'Hello, room!'
})
```
Attention:: In methods `send_messages()` and `set_room_topic()` use the 'sender' argument instead 'from': `

```python
hipchat.send_messages(room_id='your room id', sender='your user id', message='Hello, room!')
```
or
```python
hip.send_messages({
    'sender':'your user id', 
    'message':'Hello world!', 
    'room_id':'your room id'})
```

All available API methods::

```python
create_room()
delete_room()
get_messages()
get_rooms_list()
send_messages()
set_room_topic()
get_room_details()
create_user()
delete_user()
get_users_list()
get_users_details()
undelete_user()
update_user_info()

