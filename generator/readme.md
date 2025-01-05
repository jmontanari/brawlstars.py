- make a .env file with your `brawl_api_key=X`
- Download the latest swagger doclet from brawlstars. Run download_swagger.py

- To generate Clients
  download latest swagger-codegen jar
  from https://mvnrepository.com/artifact/io.swagger.codegen.v3/swagger-codegen-cli/latest
  `
  java -jar openapi-generator-cli-7.10.0.jar generate -g python-pydantic-v1 -i swagger.yaml --strict-spec false -o ../
  --package-name brawlstars.generated --git-user-id jmontanari --git-repo-id=brawlstars.py -p
  projectName=brawlstars.py,packageVersion=1.0.3`
