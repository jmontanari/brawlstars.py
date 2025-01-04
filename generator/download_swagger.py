import os

from dotenv import load_dotenv

load_dotenv()

import aiohttp


async def download_openapi_spec(url, token, output_file):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            data = await response.json()
            with open(output_file, "w") as file:
                file.write(data.text)


def main():
    openapi_url = "https://api.brawlstars.com/v1/#/definitions"

    # Bearer token for authentication
    token = os.getenv('brawl_api_key')

    # Output file for the downloaded OpenAPI spec
    openapi_file = "swagger.yaml"

    # Output directory for the generated client
    output_dir = os.getcwd()

    # Download the OpenAPI spec
    download_openapi_spec(openapi_url, token, openapi_file)


if __name__ == "__main__":
    main()
