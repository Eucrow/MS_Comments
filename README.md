# Comments microservice from WellDone
This is the **comments** microservice from WellDone: the KeepCoding Bootcamp final practise

To install dependences, with the environment activate:
```pip install -r requirements.txt```

#### API ENDPOINTS

The next endpoints are available to use in **comments** microservice:

##### Create comment
###### /comment/ (POST)
	* post_id: the post_id what the comment reply
	* comment
	* response_to: In case that the comment is a reply to another comment, the comment_id replied
	* comment_author

Return:
```
{
  "id": 17,
  "post_id": 1,
  "comment": "this is the comment",
  "response_to": 0,
  "publication_datetime": "2017-05-29T21:41:56.494217Z",
  "comment_author": "Pepito"
}
```

##### Get list of comments from certain post
###### /comment/id_post (GET)

Return:
```
[
  {
    "id": 17,
    "post_id": 1,
    "comment": "A comment",
    "response_to": 0,
    "publication_datetime": "2017-05-29T21:41:56.494217Z",
    "comment_author": "Pepito"
  },
  {
    "id": 16,
    "post_id": 1,
    "comment": "More comments...",
    "response_to": 0,
    "publication_datetime": "2017-05-29T21:41:34.296569Z",
    "comment_author": "Pepito"
  }
]
```
##### Get the number of comments from a post
###### /comment/number/post_id (GET)

Return:
```
{
  "number_of_comments": 6
}
```
