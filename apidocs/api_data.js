define({ "api": [
  {
    "version": "1.0.0",
    "group": "News",
    "type": "",
    "url": "",
    "filename": "api/news/views.py",
    "groupTitle": "News",
    "name": ""
  },
  {
    "version": "1.0.0",
    "group": "News",
    "type": "",
    "url": "",
    "filename": "api/news/views.py",
    "groupTitle": "News",
    "name": ""
  },
  {
    "type": "get",
    "url": "/articles/:id",
    "title": "Article",
    "version": "1.0.0",
    "name": "Article_Details",
    "group": "News",
    "filename": "api/apidoc_js_defines/News/ArticlesPage.js",
    "groupTitle": "News",
    "header": {
      "examples": [
        {
          "title": "Authorization-Example:",
          "content": "{\n     \"Authorization\": \"Bearer :token\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 2,\n    \"category_id\": 1,\n    \"title\": \"News 1\",\n    \"slug\": \"news-1\",\n    \"short_description\": \"Short description of news 1\",\n    \"description\": \"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\",\n    \"posted\": \"2020-02-17\",\n    \"link\": \"http://127.0.0.1:8000/api/v1/article/2/\",\n    \"likes\": 0,\n    \"is_liked\": false\n}",
          "type": "json"
        }
      ],
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "likes",
            "description": "<p>Indicates the total number of likes per article.</p>"
          },
          {
            "group": "Success 200",
            "optional": false,
            "field": "is_liked",
            "description": "<p>This field indicates whether the current user liked the article or not.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>Authentication required.</p>"
          }
        ]
      }
    }
  },
  {
    "type": "get",
    "url": "/category/:id",
    "title": "Category",
    "version": "1.0.0",
    "name": "Category_Details",
    "group": "News",
    "filename": "api/apidoc_js_defines/News/CategoriesPage.js",
    "groupTitle": "News",
    "header": {
      "examples": [
        {
          "title": "Authorization-Example:",
          "content": "{\n     \"Authorization\": \"Bearer :token\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n  {\n      \"id\": 1,\n      \"title\": \"Category 1\",\n      \"description\": \"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\",\n      \"total\": 2,\n      \"link\": \"http://127.0.0.1:8000/api/v1/categories/1/\"\n  }",
          "type": "json"
        }
      ],
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "total",
            "description": "<p>Indicates the total number of related articles.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>Authentication required.</p>"
          }
        ]
      }
    },
    "description": "<p>To build a Category Page you can use Categories endpoint and Articles endpoint with filter applied.</p>"
  },
  {
    "type": "get",
    "url": "/articles/",
    "title": "Articles",
    "version": "1.0.0",
    "group": "News",
    "filename": "api/apidoc_js_defines/News/ArticlesPage.js",
    "groupTitle": "News",
    "name": "GetArticles",
    "header": {
      "examples": [
        {
          "title": "Authorization-Example:",
          "content": "{\n     \"Authorization\": \"Bearer :token\"\n}",
          "type": "json"
        }
      ]
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "size": "1..",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Pagination page.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "category_id",
            "description": "<p>Filtering articles by category id.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"count\": 2,\n    \"next\": \"http://127.0.0.1:8000/api/v1/articles?page=2\",\n    \"previous\": null,\n    \"results\": [\n        {\n            \"id\": 2,\n            \"category_id\": 1,\n            \"title\": \"News 1\",\n            \"slug\": \"news-1\",\n            \"short_description\": \"Short description of news 1\",\n            \"description\": \"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\",\n            \"posted\": \"2020-02-17\",\n            \"link\": \"http://127.0.0.1:8000/api/v1/article/2\",\n            \"likes\": 0,\n            \"is_liked\": false\n        }\n    ]\n}",
          "type": "json"
        }
      ],
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "likes",
            "description": "<p>Indicates the total number of likes per article.</p>"
          },
          {
            "group": "Success 200",
            "optional": false,
            "field": "is_liked",
            "description": "<p>This field indicates whether the current user liked the article or not.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>Provided values for filtering doesn't match any data.</p>"
          },
          {
            "group": "Error 4xx",
            "type": "401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>Authentication required.</p>"
          }
        ]
      }
    },
    "description": "<p>Page limit is set to 1</p>"
  },
  {
    "type": "get",
    "url": "/categories/",
    "title": "Categories",
    "version": "1.0.0",
    "group": "News",
    "filename": "api/apidoc_js_defines/News/CategoriesPage.js",
    "groupTitle": "News",
    "name": "GetCategories",
    "header": {
      "examples": [
        {
          "title": "Authorization-Example:",
          "content": "{\n     \"Authorization\": \"Bearer :token\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n  [\n      {\n          \"id\": 1,\n          \"title\": \"Category 1\",\n          \"description\": \"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\",\n          \"link\": \"http://127.0.0.1:8000/api/v1/categories/1/\",\n          \"total\": 2\n      },\n      {\n          \"id\": 2,\n          \"title\": \"Category 2\",\n          \"description\": \"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).\",\n          \"link\": \"http://127.0.0.1:8000/api/v1/categories/2/\",\n          \"total\": 0\n      },\n      {\n          \"id\": 3,\n          \"title\": \"Category 3\",\n          \"description\": \"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \\\"de Finibus Bonorum et Malorum\\\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \\\"Lorem ipsum dolor sit amet..\\\", comes from a line in section 1.10.32.\",\n          \"link\": \"http://127.0.0.1:8000/api/v1/categories/3/\",\n          \"total\": 0\n      }\n  ]",
          "type": "json"
        }
      ],
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "total",
            "description": "<p>Indicates the total number of related articles.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>Authentication required.</p>"
          }
        ]
      }
    },
    "description": "<p>To build a Category Page you can use Categories endpoint and Articles endpoint with filter applied.</p>"
  },
  {
    "type": "post",
    "url": "/articles/:id/like/",
    "title": "Like/Unlike",
    "version": "1.0.0",
    "group": "News",
    "filename": "api/apidoc_js_defines/News/ArticlesPage.js",
    "groupTitle": "News",
    "name": "PostArticlesIdLike",
    "header": {
      "examples": [
        {
          "title": "Authorization-Example:",
          "content": "{\n     \"Authorization\": \"Bearer :token\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Like-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"message\": \"You have liked current article!\"\n}",
          "type": "json"
        },
        {
          "title": "Unlike-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"message\": \"You have unliked current article!\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>Authentication required.</p>"
          }
        ]
      }
    },
    "description": "<p>Like/Unlike will be determined depending on whether the current user liked the article before or not (the is_liked parameter).</p>"
  },
  {
    "type": "post",
    "url": "/auth/login",
    "title": "Login",
    "name": "Login",
    "group": "User",
    "version": "1.0.0",
    "filename": "api/api/views.py",
    "groupTitle": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Username. Required</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>User password. Required</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"user\": {\n        \"first_name\": \"Jhon\",\n        \"last_name\": \"Doe\",\n        \"username\": \"jhondoe\",\n        \"email\": \"jhon@doe.com\"\n    },\n    \"tokens\": {\n        \"refresh\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4MDgwNTkxOSwianRpIjoiZGVkYjliZWU0OWVjNDk4YjkyMTA5NWIwODhmYTAyOTEiLCJ1c2VyX2lkIjoxOX0.Rx639CfHKpWSdG6oC0BQBXSlVXsx5f6mvpj1ychNYCc\",\n        \"access\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgwNzE5ODE5LCJqdGkiOiJhM2RkODc4ODU5ZTE0OWI4YmI1NmM1Y2U1ZjY1MGI1OSIsInVzZXJfaWQiOjE5fQ.-eYnIYLwnJwEl9S2qxkz7jbjUad8p-d5PeAFbPUzAAI\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>Authentication required.</p>"
          }
        ]
      }
    }
  },
  {
    "type": "post",
    "url": "/auth/register",
    "title": "Registration",
    "name": "Registration",
    "group": "User",
    "version": "1.0.0",
    "filename": "api/api/views.py",
    "groupTitle": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>User first name. Required</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>User last name. Required</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Username. Required</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>User email. Required</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>User password. Required</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"User\": {\n        \"first_name\": \"Jhon\",\n        \"last_name\": \"Doe\",\n        \"username\": \"jhondoe\",\n        \"email\": \"jhon@doe.com\"\n    },\n    \"tokens\": {\n        \"refresh\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4MDgwNTkxOSwianRpIjoiZGVkYjliZWU0OWVjNDk4YjkyMTA5NWIwODhmYTAyOTEiLCJ1c2VyX2lkIjoxOX0.Rx639CfHKpWSdG6oC0BQBXSlVXsx5f6mvpj1ychNYCc\",\n        \"access\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgwNzE5ODE5LCJqdGkiOiJhM2RkODc4ODU5ZTE0OWI4YmI1NmM1Y2U1ZjY1MGI1OSIsInVzZXJfaWQiOjE5fQ.-eYnIYLwnJwEl9S2qxkz7jbjUad8p-d5PeAFbPUzAAI\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>Bad request.</p>"
          }
        ]
      }
    }
  }
] });
