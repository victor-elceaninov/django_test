/**
* @apiDefine ArticlesPage
**/

/**
* @api {get} /articles/ Articles
* @apiVersion 1.0.0
* @apiGroup News
* @apiUse Articles
*/

/**
*
* @api {get} /articles/:id Article
* @apiVersion 1.0.0
* @apiName Article Details
* @apiGroup News
* @apiUse Article
**/

/**
* @api {post} /articles/:id/like/ Like/Unlike
* @apiVersion 1.0.0
* @apiGroup News
* @apiUse LikeUnlike
*/