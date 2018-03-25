docker build -t build_cmd_entrypoint_test .
docker run --rm build_cmd_entrypoint_test
docker run --rm build_cmd_entrypoint_test "John"

# Only parameters can be overrided, so this doesn't work as expected
docker run --rm build_cmd_entrypoint_test /bin/bash
