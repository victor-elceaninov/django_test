/**
* @apiDefine UserLogin
*
* @apiParam {String} username Username. Required
* @apiParam {String} password User password. Required
*
* @apiSuccessExample {json} Success-Response:
*     HTTP/1.1 200 OK
*     {
*         "user": {
*             "first_name": "Jhon",
*             "last_name": "Doe",
*             "username": "jhondoe",
*             "email": "jhon@doe.com"
*         },
*         "tokens": {
*             "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4MDgwNTkxOSwianRpIjoiZGVkYjliZWU0OWVjNDk4YjkyMTA5NWIwODhmYTAyOTEiLCJ1c2VyX2lkIjoxOX0.Rx639CfHKpWSdG6oC0BQBXSlVXsx5f6mvpj1ychNYCc",
*             "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgwNzE5ODE5LCJqdGkiOiJhM2RkODc4ODU5ZTE0OWI4YmI1NmM1Y2U1ZjY1MGI1OSIsInVzZXJfaWQiOjE5fQ.-eYnIYLwnJwEl9S2qxkz7jbjUad8p-d5PeAFbPUzAAI"
*         }
*     }
*
* @apiError {401} Unauthorized Authentication required.
*/
