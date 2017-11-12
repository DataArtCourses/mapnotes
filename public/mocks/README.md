# Mocks for project Mapified

**All files has been created by [JSON Generator](https://next.json-generator.com/)**

**The DATABASE SCHEMA is [here](https://app.quickdatabasediagrams.com/#/schema/GCs1EATVp02Z9RyqVBMrSg)**

## Users with profiles `_users.json`

```js
[
  {
    'repeat(100)': {
    userId: '{{index(1001)}}',
    firstName: '{{ firstName() }}',
    surname: '{{ surname() }}',
    avatarUrl: 'http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png',
    phone:'{{ phone() }}',
    bio: '{{ lorem(1, "paragraphs") }}',
    friends: [{
     'repeat(4, 10)': {
     userId: '{{integer(1001, 1100)}}'
     }
    }],
    isActive: '{{ integer(0, 1) }}',
    statusRelations: '{{ integer(0, 1) }}'
   }
  }
]
```

## Pins `_pins.json`

```js
[
  {
    'repeat(100)': {
     pinId: '{{ index(101) }}',
     pinInfo: '{{lorem(5, "words")}}',
     pinLatLng: ['{{floating(46.45, 46.52, 4)}}', '{{floating(30.67, 30.77, 4)}}'],
     totalComments: '{{ integer(1, 10) }}',
     totalPhotos: '{{integer(5)}}',
     pinStatus: '{{integer(1,3)}}'
    }
  }
]
```

## Pin content
```js

```

## Pin gallery
```js
[
  {
    'repeat(20)': {
     photoId: '{{index(1)}}',
     photoUrl: 'http://lorempixel.com/600/480',
     likes: '{{ integer(1, 10) }}',
     liked: '{{ random(true, false) }}',
     comments: [
       {
        'repeat(20)': {
        liked: '{{ random(true, false) }}',
        likes: '{{ integer(1, 10) }}',
        time: '{{date(new Date(2017, 10, 15), new Date(2017, 10, 30))}}',
        author: {
          userName: '{{ firstName() }} {{ surname() }}',
          avatarUrl: "http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png",
          userId: '{{integer(1081, 1100)}}'
        },
        commentBody: '{{lorem(3, "sentences")}}',
        commentId: '{{integer(1, 20)}}'
       }
      }
     ]
    }
  }
]
```


## Chats `_chats.json`

```js
[
  {
    'repeat(15)': {
    chatId: '{{index(10)}}',
    chatWith: {
      userId: '{{ index(1001) }}',
      userName: '{{ firstName() }}',
      avatarUrl: 'http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png'
    },
    lastMessage: {
      body: '{{lorem(3, "words")}}',
      time: '{{date(new Date(2017, 10, 15), new Date(2017, 10, 30))}}'
    },
    unread: '{{ integer(0, 5) }}'
   }
  }
]
```

## Chat `_chat<id>.json`

```js
[
  {
    'repeat(20)': {
     message_id: '{{index(1)}}',
     message_body: '{{ lorem(3, "sentences") }}',
     user_id: '{{ random(1001, 1100) }}',
     time: '{{date(new Date(2017, 9, 20), new Date(2017, 10, 8))}}',
     status: 1
    }
  }
]
```