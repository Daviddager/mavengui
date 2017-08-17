#bin/bash
echo "Deleting containers"
docker ps -aq -f status=exited
docker ps -aq --no-trunc | xargs docker rm
docker images -q --filter dangling=true | xargs docker rmi

