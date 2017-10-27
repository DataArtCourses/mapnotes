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

## Pins with content 

```js
[
  {
    'repeat(100)': {
     pinId: '{{ index(101) }}',
     pinLatLng: ['{{floating(46.45, 46.52, 4)}}', '{{floating(30.67, 30.77, 4)}}'],
     totalComments: '{{ integer(1, 10) }}',
     totalPhotos: '{{integer(5)}}',
     pinStatus: '{{integer(1,3)}}',
     comments: [{
       'repeat(1, 10)': {
       commetId: '{{objectId()}}',
       commentBody: '{{lorem(1, "paragraphs")}}',
       author: {
         userId: '{{integer(1001, 1100)}}'
          },
       likes: '{{ integer() }}',
       timeCreated: '{{date(new Date(2017, 9, 27), new Date(2017, 12, 15))}}'
         }
       }],
      photoGalery: {
        cover_1: '',
        cover_2: '',
        cover_3: '',
        albumUrl: '/photos/search?photo={{index(101)}}'
      }
    }
  }
]

```