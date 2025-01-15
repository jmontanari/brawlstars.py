- make a .env file with your `brawl_api_key=X`
- Download the latest swagger doclet from brawlstars. Run download_swagger.py

- To generate Clients
  download latest openapi-generator-cli jar
  from https://mvnrepository.com/artifact/org.openapitools/openapi-generator-cli/latest

```
java -jar openapi-generator-cli-7.10.0.jar generate -i swagger.yaml -g python --package-name brawlstars --skip-validate-spec --global-property modelTests=false --global-property apiTests=false -o ../ --additional-properties packageVersion=1.1.0,projectName=brawlstars.py
```