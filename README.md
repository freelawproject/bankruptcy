Bankruptcy Microservice from Free Law Project
---------------------------------------------

## Notes

This is a microservice of for extracting bankruptcy data from digitally native bankruptcy forms.

## Quick Start

Assuming you have docker installed run:

    docker-compose -f docker-compose.yml up --build -d

or 

    docker-compose -f docker-compose.dev.yml up --build -d

This will expose the endpoints on port 5050, which can be modified in the nginx/nginx.conf file and points to the django server running on port 8000.

For more options and configuration of nginx checkout https://nginx.org/en/docs/.

After the compose file has finished you should be able to test that you have a working environment by running

    curl 0.0.0.0:5050
    curl http://localhost:5050

Should return and HTTP Response containing Heartbeat detected.

If connecting via the docker network you can test by running

    curl http://http://bankruptcy:5050

## Endpoints (Coming Soon)

