docker build -t build_entrypoint_test .
docker run --rm build_entrypoint_test

# entrypoint cannot be override, so this doesn't works as expected
docker run --rm build_entrypoint_test /bin/bash
