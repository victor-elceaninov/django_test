/**
* @apiDefine Articles
*
* @apiHeaderExample {json} Authorization-Example:
*      {
*           "Authorization": "Bearer :token"
*      }
*
* @apiParam {Number{1..}} [page=1] Pagination page.
* @apiParam {Number} [category_id] Filtering articles by category id.
*
* @apiSuccessExample {json} Success-Response:
*     HTTP/1.1 200 OK
*     {
*         "count": 2,
*         "next": "http://127.0.0.1:8000/api/v1/news/articles?page=2",
*         "previous": null,
*         "results": [
*             {
*                 "id": 2,
*                 "category_id": 1,
*                 "title": "News 1",
*                 "slug": "news-1",
*                 "short_description": "Short description of news 1",
*                 "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
*                 "posted": "2020-02-17",
*                 "link": "http://127.0.0.1:8000/api/v1/news/article/2",
*                 "likes": 0,
*                 "is_liked": false
*             }
*         ]
*     }
*
* @apiError {401} Unauthorized Authentication required.
* @apiError {400} BadRequest Bad request.
*
* @apiDescription Page limit is set to 1
**/