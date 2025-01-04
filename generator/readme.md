- make a .env file with your `brawl_api_key=X`
- Download the latest swagger doclet from brawlstars. Run download_swagger.py

- To generate Clients
  download latest swagger-codegen jar
  from https://mvnrepository.com/artifact/io.swagger.codegen.v3/swagger-codegen-cli/latest
  ` 
  java -jar swagger-codegen-cli-3.0.66.jar generate -i swagger.yaml -l python -o ../ -DpackageName=brawlstars.generated
  `

