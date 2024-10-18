# GeekTrac
## How to run

1) Create couchdb_config.ini file with the contents of admin username and password.
2) Create a directory named `secret` with the secrets specified on the docker-compose.yaml file ( currently requires
   
       couchdb_passwd.txt - couchdb login password,
   
       couchdb_uname.txt - couchdb login username,
   
       secret_key.txt - jwt HS256 key )
   
4) if using docker with compose plugin, type

    ```docker compose up```

    if using docker-compose, type

    ```docker-compose up```
