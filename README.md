# Api News

Steps to run this project:

1. Run `virtualenv venv` command
2. Run `pip install -r requirements.txt` command


## Endpoint:

### Status da API
| Methods  | Actions                   | Url                                         |
|:--------:|:--------------------------|:--------------------------------------------|
| GET      | status da api             | {{url}/                                     |


### News
| Methods  | Actions                   | Url                                         |
|:--------:|:--------------------------|:--------------------------------------------|
| GET      | gives a list of all news  | {{url}}/news                                |
| POST     | creates a new news        | {{url}}/news                                |
| GET      | shows a single news       | {{url}}/news/{{id}}                         |
| PUT      | updates a single news     | {{url}}/news/{{id}}                         |
| DELETE   | deletes a single news     | {{url}}/news/{{id}}                         |
