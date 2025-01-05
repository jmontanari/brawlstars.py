- make a .env file with your `brawl_api_key=X`
- Download the latest swagger doclet from brawlstars. Run download_swagger.py

- To generate Clients
  download latest swagger-codegen jar
  from https://mvnrepository.com/artifact/io.swagger/swagger-codegen-cli/latest
  ```
  java -jar swagger-codegen-cli-2.4.44.jar generate -l python  -i swagger.yaml -o ../ --additional-properties packageName=brawlstars.generated -l python
- ```