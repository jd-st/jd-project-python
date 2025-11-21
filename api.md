# Shared Types

```python
from jd_project.types import Order
```

# Pets

Types:

```python
from jd_project.types import (
    Category,
    Pet,
    PetFindByStatusResponse,
    PetFindByTagsResponse,
    PetUploadImageResponse,
)
```

Methods:

- <code title="post /pet">client.pets.<a href="./src/jd_project/resources/pets.py">create</a>(\*\*<a href="src/jd_project/types/pet_create_params.py">params</a>) -> <a href="./src/jd_project/types/pet.py">Pet</a></code>
- <code title="get /pet/{petId}">client.pets.<a href="./src/jd_project/resources/pets.py">retrieve</a>(pet_id) -> <a href="./src/jd_project/types/pet.py">Pet</a></code>
- <code title="put /pet">client.pets.<a href="./src/jd_project/resources/pets.py">update</a>(\*\*<a href="src/jd_project/types/pet_update_params.py">params</a>) -> <a href="./src/jd_project/types/pet.py">Pet</a></code>
- <code title="delete /pet/{petId}">client.pets.<a href="./src/jd_project/resources/pets.py">delete</a>(pet_id) -> None</code>
- <code title="get /pet/findByStatus">client.pets.<a href="./src/jd_project/resources/pets.py">find_by_status</a>(\*\*<a href="src/jd_project/types/pet_find_by_status_params.py">params</a>) -> <a href="./src/jd_project/types/pet_find_by_status_response.py">PetFindByStatusResponse</a></code>
- <code title="get /pet/findByTags">client.pets.<a href="./src/jd_project/resources/pets.py">find_by_tags</a>(\*\*<a href="src/jd_project/types/pet_find_by_tags_params.py">params</a>) -> <a href="./src/jd_project/types/pet_find_by_tags_response.py">PetFindByTagsResponse</a></code>
- <code title="post /pet/{petId}">client.pets.<a href="./src/jd_project/resources/pets.py">update_by_id</a>(pet_id, \*\*<a href="src/jd_project/types/pet_update_by_id_params.py">params</a>) -> None</code>
- <code title="post /pet/{petId}/uploadImage">client.pets.<a href="./src/jd_project/resources/pets.py">upload_image</a>(pet_id, image, \*\*<a href="src/jd_project/types/pet_upload_image_params.py">params</a>) -> <a href="./src/jd_project/types/pet_upload_image_response.py">PetUploadImageResponse</a></code>

# Petstore

Types:

```python
from jd_project.types import PetstoreListInventoryResponse
```

Methods:

- <code title="get /petstore/inventory">client.petstore.<a href="./src/jd_project/resources/petstore/petstore.py">list_inventory</a>() -> <a href="./src/jd_project/types/petstore_list_inventory_response.py">PetstoreListInventoryResponse</a></code>

## Orders

Methods:

- <code title="post /petstore/order">client.petstore.orders.<a href="./src/jd_project/resources/petstore/orders.py">create</a>(\*\*<a href="src/jd_project/types/petstore/order_create_params.py">params</a>) -> <a href="./src/jd_project/types/shared/order.py">Order</a></code>
- <code title="get /petstore/order/{orderId}">client.petstore.orders.<a href="./src/jd_project/resources/petstore/orders.py">retrieve</a>(order_id) -> <a href="./src/jd_project/types/shared/order.py">Order</a></code>
- <code title="delete /petstore/order/{orderId}">client.petstore.orders.<a href="./src/jd_project/resources/petstore/orders.py">delete</a>(order_id) -> None</code>

# Users

Types:

```python
from jd_project.types import User, UserLoginResponse
```

Methods:

- <code title="post /user">client.users.<a href="./src/jd_project/resources/users.py">create</a>(\*\*<a href="src/jd_project/types/user_create_params.py">params</a>) -> <a href="./src/jd_project/types/user.py">User</a></code>
- <code title="get /user/{username}">client.users.<a href="./src/jd_project/resources/users.py">retrieve</a>(username) -> <a href="./src/jd_project/types/user.py">User</a></code>
- <code title="put /user/{username}">client.users.<a href="./src/jd_project/resources/users.py">update</a>(existing_username, \*\*<a href="src/jd_project/types/user_update_params.py">params</a>) -> None</code>
- <code title="delete /user/{username}">client.users.<a href="./src/jd_project/resources/users.py">delete</a>(username) -> None</code>
- <code title="post /user/createWithList">client.users.<a href="./src/jd_project/resources/users.py">create_with_list</a>(\*\*<a href="src/jd_project/types/user_create_with_list_params.py">params</a>) -> <a href="./src/jd_project/types/user.py">User</a></code>
- <code title="get /user/login">client.users.<a href="./src/jd_project/resources/users.py">login</a>(\*\*<a href="src/jd_project/types/user_login_params.py">params</a>) -> str</code>
- <code title="get /user/logout">client.users.<a href="./src/jd_project/resources/users.py">logout</a>() -> None</code>
