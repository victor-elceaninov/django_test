/**
* @apiDefine Category
*
* @apiHeaderExample {json} Authorization-Example:
*      {
*           "Authorization": "Bearer :token"
*      }
*
* @apiSuccessExample {json} Success-Response:
*     HTTP/1.1 200 OK
*       {
*           "id": 1,
*           "title": "Category 1",
*           "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
*           "total": 2,
*           "link": "http://127.0.0.1:8000/api/v1/categories/1/"
*       }
*
* @apiSuccess total Indicates the total number of related articles.
*
* @apiError {401} Unauthorized Authentication required.
*
* @apiDescription To build a Category Page you can use Categories endpoint and Articles endpoint with filter applied.
**/