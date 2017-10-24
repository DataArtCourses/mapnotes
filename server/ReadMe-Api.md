# API Documentation

## <a id="start">List of all endpoints</a>

|# | Endpoint                | Methods          | Detail                                  |
---|-------------------------| :--------------: |---------------------------------------- |
 1 | `/api`                  | GET              | [Main](#main)                           |
 2 | `api/registration`      | POST             | [Registration](#registration)           |
 3 | `api/login`             | POST             | [Login](#login)                         |
 4 | `api/users`             | GET              | [Users](#users-list)                    |        
 5 | `api/users/<user>`      | GET, POST        | [Take and change profile](#profile)     |
 6 | `api/pins`              | GET, POST        | [Pins list, add new](#pins-list)        |
 7 | `api/pins/<pin>`        | GET, POST        | [Pin info, add comment or photo](#pin)  |
 8 | `api/comments`          | GET,             | [Get comments](#comments-list)          |
 9 | `api/comments/<comment>`| PUT, DELETE      | [Comment add, edit, del](#comment)      |
 10| `api/photos`            | GET              | [Get photos](#photos-list)              |
 11| `api/photos/<photo>`    | GET, POST, DELETE| [Get,add, del photo](#photo)            |
 12| `api/chats`             | GET, POST        | [Chats list, add new](#chats)           |
 13| `api/chats/<chat>`      | GET, POST, DELETE| [Chat manipulations](#chat)             |
 14| `api/help`              | GET              | [Help](#help)                           |    


## <a id="main">`api/`</a> [&uarr;](#start)

**`GET`** if user have been registered, response should be:

```json
{
  "text": "Wellcome to the Mapfied. For detail info, please make GET request to api/help"
}
```

Any other methods response should be with status 405:

```json
{
  "text": "Method not allowed. For detail info, please make GET request to api/help"
}
```

## <a id="registration">`api/registration`</a> [&uarr;](#start)

**`POST`** with json data:

```json
{
  "email": "example@some.com",
  "password": "secret"
}
```

if this `email` is alredy exist in the base response should be with status `403`:

```json
{
  "text": "this email already exist. Please try another one"
}
```

If registration is OK:

```json
{
  "text": "Some text"
}
```

All other request should be response with status `405`:

```json
{
  "text": "Method not allowed. For detail info, please make GET request to api/help"
}
```

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

## <a id="users-list">`api/users`</a> [&uarr;](#start)

**`GET`** method:

```json
[
  {
    "user_id": "some_id",
    "user_avatar_url": "<url>",
    "user_online": 1, // 1 - ONLINE, 0 - OFFLINE
    "user_name": "User name"
  },
  {
    "user_id": "some_id",
    "user_avatar_url": "<url>",
    "user_online": 0, // 1 - ONLINE, 0 - OFFLINE
    "user_name": "User name"
  }
  ...
]
```

All other request should be response with status 405:

```json
{
  "text": "Method not allowed. For detail info, please make GET request to api/help"
}
```

## <a id="profile">`api/users/<user_id>`</a> [&uarr;](#start)

**`GET`** method response:

```json
{
  "user_info": {
    "user_id": "some_id",
    "user_avatar_url": "<url>",
    "user_name": "User name",
    "user_last_name": "Last Name",
    "user_phone": "000000000000",
    "bio": "User info"
  },
  "user_status": 1, // 1 - ONLINE, 0 - OFFLINE
}
```

User can change own information by **`POST`** request

```json
{
  "user_id": "some_id",
  "user_avatar_url": "<url>",
  "user_name": "User name",
  "user_last_name": "Last Name",
  "bio": "User info",
  "user_phone": "000000000000"
}
```

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

## <a id="pins-list">`api/pins`</a> [&uarr;](#start)

**`GET`** response:

```json
[
  {
    "pin_info":
    {
      "pin_id": "some_id",
      "pin_long_lat": [112.89, 13.88],
      "total_comments": 10,
      "total_photo": 20,
      "likes": 0   // ?????? 
    },
    "pin_status": 0 // 0 - simple, 1 - hot, 2 - ...
  },
  ...
]
```

**`POST`** request:

```json
{
  "pin_long_lat": [112.89, 13.88],
  "comment": "Lorem Ipsum",
  "comment_status": 0, // 0 - public, 1 - private
  "photo": "url",
  "photo_status": 0 // 0 - public, 1 - private
}
```


## <a id="pin-info">`api/pins/<pin>`</a> [&uarr;](#start)

**`GET`** response:

```json
{
  "pin_id": "some_id",
  "pin_long_lat": [112.89, 13.88],
  "comments": [
    {
      "commet_id": "some_id",
      "comment_text": "Lorem ipsum",
      "author": {
        "name": "user_name",
        "avatar_url": "<url>",
      },
      "likes": 0,  // ????????
      "time_created": "Summertimes"
    },
  ...
  ],
  "photo_galery": {
    "cover_1": "<url>",
    "cover_2": "<url>",
    "cover_3": "<url>",
    "album_url": "<url>"
  }
}
```


## <a id="comments-list">`api/comments`</a> [&uarr;](#start)

**`GET`** response:



## <a id="comment">`api/comments/<comment>`</a> [&uarr;](#start)

**`GET`** response:


**`POST, PUT, DELETE`** requests:


## <a id="photos-list">`api/photos`</a> [&uarr;](#start)

**`GET`** response:


## <a id="photo">`api/photos/<photo>`</a> [&uarr;](#start)

**`GET`** response:


**`POST, PUT, DELETE`** requests:


## <a id="chats">`api/chats`</a> [&uarr;](#start)

**`GET`** response:


## <a id="chat">`api/chats/<chat>`</a> [&uarr;](#start)

**`POST, PUT, DELETE`** requests:


## <a id="help">`api/help`</a> [&uarr;](#start)

**`GET`** response:
