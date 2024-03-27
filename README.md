# Node Service in Python
This is an example of a simple CRUD service implemented using Flask, a web framework in Python. I built this  because 

1. so many of my recent interview take-home assignments have had me implement some logic running on a simple HTTP service that can be queried
2. it's a nifty template that can be reused across many possible side projects.

Feel free to fork and use this as you will.

## Running the service

From this directory execute 

`flask --app NodeService --debug run --port 3001`

You can also run `make run`.

This should start the service. 

## Example URL for GET request
`/api/node?id=1`

## Example POST requests using `curl`

```
curl --header "Content-Type: application/json"   --request POST   --data '{"title": "1984", "content": "It was a bright cold day in April"}' http://0.0.0.0:3001/api/node

curl -X DELETE http://0.0.0.0:3001/api/node/1
```

Note to readers: Why 0.0.0.0 instead of localhost? I typically run this service on replit which runs services on 0.0.0.0.
