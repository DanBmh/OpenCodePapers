# Testing

Build container with testing tools:

```bash
docker build --progress=plain -f tests/dockerfile -t testing_ocp .

docker run --network host --rm \
  --volume `pwd`/:/OpenCodePapers/ \
  -it testing_ocp
```

For syntax tests, check out the steps in the [gitlab-ci](../.gitlab-ci.yml#L76) file.
