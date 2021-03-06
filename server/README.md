# API Documentation

## <a id="start">List of all endpoints</a>

|# | Endpoint                       | Methods               | Detail                                               |
---|--------------------------------| :-------------------: |----------------------------------------------------- |
 1 | `/api`                         | GET                   | [Main](#main)                                        |
 2 | `api/registration`             | POST                  | [Registration](#registration)                        |
 3 | `api/login`                    | POST                  | [Login](#login)                                      |
 4 | `api/users`                    | GET                   | [Users](#users-list)                                 |
 5 | `api/users/friends`            | GET, POST             | [Friends list, add friend](#friends-list)            |
 6 | `api/users/friends/<user>`     | DELETE                | [Delete friend](#delete-friends)                     |
 7 | `api/users/<user>`             | GET, POST, DELETE     | [Get and change profile, ban](#profile)              |
 8 | `api/users/<user>/comments`    | GET                   | [Get all user comments](#user-comments-list)         |
 9 | `api/users/<user>/photos`      | GET                   | [Get all user photos](#user-photos-list)             |
 10| `api/pins`                     | GET, POST             | [Pins list, add new](#pins-list)                     |
 11| `api/pins/<pin>`               | GET, POST             | [Pin info, add comment or photo](#pin)               |
 12| `api/pins/<pin>/likes`         | GET, POST             | [Get pin likes, add, remove like](#pin-likes)        |
 13| `api/pins/<pin>/comments`      | GET, POST             | [Get pin comments, add comment](#pin-comments)       |
 14| `api/pins/<pin>/photos`        | GET                   | [Get pin photos](#pin-photos)                        |
 15| `api/comments/<comment>`       | PUT, DELETE           | [Comment add, edit, del](#comment)                   |
 16| `api/comments/<comment>/likes` | GET, POST             | [Get comment likes, add, remove like](#comment-likes)|
 17| `api/photos/<photo>`           | GET, POST, DELETE     | [Get,add, del photo](#photo)                         |
 18| `api/photos/<photo>/likes`     | GET, POST             | [Get photo likes, add, remove like](#photo-likes)    |
 19| `api/photos/<photo>/comments`  | GET, POST             | [Get photo comments, add comment](#photo-comments)   |
 20| `api/chats`                    | GET, POST             | [Chats list, add new](#chats)                        |
 21| `api/chats/<chat>`             | GET, POST, PUT, DELETE| [Chat manipulations](#chat)                          |
 22| `api/help`                     | GET                   | [Help](#help)                                        |    


## <a id="main">`api/`</a> [&uarr;](#start)

**`GET`** if user have been registered, response should be:

```json
{
  "text": "Wellcome to the Mapfied. For detail info, please make GET request to api/help"
}
```
<details>
<summary>Errors</summary>
Any other methods response should be with status 405:

```json
{
  "text": "Method not allowed. For detail info, please make GET request to api/help"
}
```
</details>

## <a id="registration">`api/registration`</a> [&uarr;](#start)

**`POST`** with json data:

```json
{
  "email": "example@some.com",
  "password": "secret"
}
```
If registration is OK response should be:

```json
{
  "text": "Some text"
}
```

<details>
<summary>Errors</summary>
if this `email` is alredy exist in the base response should be with status `403`:

```json
{
  "text": "this email already exist. Please try another one"
}
```

All other request should be response with status `405`:

```json
{
  "text": "Method not allowed. For detail info, please make GET request to api/help"
}
```
</details>

## <a id="login">`api/login`</a> [&uarr;](#start)

**`POST`** with json data:

```json
{
  "email": "example@some.com",
  "password": "secret"
}
```

If password and email is OK

Call back should be `jwtToken`

```json
{
  "user_id": "SomeName",
  "token": "supersecret"
}
```

<details>
<summary>Errors</summary>
If password or email isn't correct response should be `401`:

```json
{
  "text": "username(email) or password is incorect"
}

```

If json format isn't correct - `400`

```json
{
  "text": "Wrong json. For detail info, please make GET request to api/help"
}
```

All other request should be response with status `405`:

```json
{
  "text": "Method not allowed. For detail info, please make GET request to api/help"
}
```
</details>

## <a id="users-list">`api/users`</a> [&uarr;](#start)

**`GET`** method:

```json
[
  {
    "userId": "some_id",
    "userFirstName": "User name",
    "avatarUrl": "<url>",
    "isActive": 1, // 1 - ONLINE, 0 - OFFLINE
    "statusRelations": 1 // 0 - Without, 1 - Friends,
  },
  {
    "userId": "some_id",
    "userFirstName": "User name",
    "avatarUrl": "<url>",
    "isActive": 0, // 1 - ONLINE, 0 - OFFLINE
    "statusRelations": 1 // 0 - Without, 1 - Friends
  }
  ...
]
```
<details>
<summary>Errors</summary>
All other request should be response with status 405:

```json
{
  "text": "Method not allowed. For detail info, please make GET request to api/help"
}
```
</details>

## <a id="friends-list">`api/users/friends`</a> [&uarr;](#start)

**`GET`** response:

**`POST`** requests:

## <a id="delete-friend">`api/users/friends/<user>`</a> [&uarr;](#start)

**`DELETE`** requests:

## <a id="profile">`api/users/<user>`</a> [&uarr;](#start)

**`GET`** method response:

```json
{
  "userId": "some_id",
  "avatarUrl": "<url>",
  "userFirstName": "User name",
  "userSurname": "Last Name",
  "phone": "000000000000",
  "bio": "User info",
  "friends": [
    {
      "userId": "some_id",
      "userFirstName": "User_name",
      "avatarUrl": "<url>"
    },
    {
      "userId": "some_id",
      "userFirstName": "User_name",
      "avatarUrl": "<url>"
    }
    ...
  ],
  "isActive": 1, // 1 - ONLINE, 0 - OFFLINE
}
```

User can change his own information by **`POST`** request

```json
{
  "userId": "some_id",
  "avatarUrl": "<url>",
  "userFirstName": "User name",
  "userSurname": "Last Name",
  "bio": "User info",
  "phone": "000000000000"
}
```

## <a id="user-comments-list">`api/<user>/comments`</a> [&uarr;](#start)

**`GET`** response:

For get all user comments, request should be:

```http
api/user/<user>/comments
```

## <a id="user-photos-list">`api/<user>/photos`</a> [&uarr;](#start)

For get all user photos, request should be:

```http
api/users/<user>/photos
```

<details>
<summary>Error</summary>
If `json` format isn't correct - `400`

```json
{
  "text": "Wrong json. For detail info, please make GET request to api/help"
}
```

All other request should be response with status 405:

```json
{
  "text": "Method not allowed. For detail info, please make GET request to api/help"
}
```
</details>

## <a id="pins-list">`api/pins`</a> [&uarr;](#start)

**`GET`** response:

```json
[
  {
    "pinId": "some_id",
    "pinInfo": "someInfo",
    "pinLatLng": [112.89, 13.88],
    "comments": 10,
    "photos": 20,
    "likes": 0,
    "pinStatus": 0 // 0 - simple, 1 - hot, 2 - ...
  },
  ...
]
```

**`POST`** request:

```json
{
  "pinLatLng": [112.89, 13.88],
  "comment": "Lorem Ipsum",
  "commentStatus": 0, // 0 - public, 1 - private
  "photo": "url",
  "photoStatus": 0 // 0 - public, 1 - private
}
```


## <a id="pin">`api/pins/<pin>`</a> [&uarr;](#start)

**`GET`** response:

```json
{
  "pinId": "some_id",
  "pinLatLng": [112.89, 13.88],
  "comments": [
    {
      "commetId": "some_id",
      "commentBody": "Lorem ipsum",
      "author": {
        "name": "user_name",
        "avatarUrl": "<url>",
      },
      "likes": 0,
      "timeCreated": "Summertimes"
    },
  ...
  ],
  "photoGalery": {
    "cover_1": "<url>",
    "cover_2": "<url>",
    "cover_3": "<url>",
  }
}
```
## <a id="pin-likes">`api/pins/<pin>/likes`</a> [&uarr;](#start)

**`GET`** requests:

**`POST`** requests:

## <a id="pin-comments">`api/pins/<pin>/comments`</a>[&uarr;](#start)

**`GET`** requests:

## <a id="pin-photos">`api/pins/<pin>/photos`</a>[&uarr;](#start)

**`GET`** requests:


## <a id="comment">`api/comments/<comment>`</a> [&uarr;](#start)

**`GET`** response:


**`POST, PUT, DELETE`** requests:

## <a id="comment-likes">`api/comments/<comment>/likes`</a> [&uarr;](#start)

**`GET`** response:


**`POST`** requests:


## <a id="photo">`api/photos/<photo>`</a> [&uarr;](#start)

**`GET`** response:


**`POST, PUT, DELETE`** requests:


## <a id="chats">`api/chats`</a> [&uarr;](#start)

**`GET`** response:


## <a id="chat">`api/chats/<chat>`</a> [&uarr;](#start)

**`POST, PUT, DELETE`** requests:


## <a id="help">`api/help`</a> [&uarr;](#start)

**`GET`** response:
