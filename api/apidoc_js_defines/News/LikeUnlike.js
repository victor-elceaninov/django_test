/**
* @apiDefine LikeUnlike
*
* @apiHeaderExample {json} Authorization-Example:
*      {
*           "Authorization": "Bearer :token"
*      }
*
* @apiSuccessExample {json} Like-Response:
*     HTTP/1.1 200 OK
*     {
*         "message": "You have liked current article!"
*     }
*
* @apiSuccessExample {json} Unlike-Response:
*     HTTP/1.1 200 OK
*     {
*         "message": "You have unliked current article!"
*     }
*
* @apiError {401} Unauthorized Authentication required.
* @apiDescription Like/Unlike will be determined based on whether the article was liked or not. For more info about was specific article liked or not you can access `Article` and `Articles` endpoints (`is_liked` param).
**/