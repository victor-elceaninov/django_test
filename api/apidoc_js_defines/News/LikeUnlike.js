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
* @apiDescription Like/Unlike will be determined depending on whether the current user liked the article before or not (the is_liked parameter).
**/