## Install

```sh
pip install -r requirements.txt
```

## Run

```sh
python app.py
```

## API

```sh
GET     /list              ->  Get instances retrieved from AWS
POST    /add               ->  Add anew AWS API keys
{
	"accessKeyId": "accessKey",
	"secretAccessKey": "secretKey",
	"region": "us-west-2"
}

```