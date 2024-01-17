from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import os

GOOGLE_SEARCH_INDEXING_API = {
    'SCOPES' : [ "https://www.googleapis.com/auth/indexing" ],
    'ENDPOINT': "https://indexing.googleapis.com/v3/urlNotifications:publish",
    'KEYFILE': None
}

try:
    GOOGLE_SEARCH_INDEXING_API['KEYFILE'] = os.environ['GOOGLE_SEARCH_INDEXING_API_KEYFILE']
    ALL_CHANGED_POST_FILES = os.environ['ALL_CHANGED_POST_FILES'].split(' ')
    BASE_URL = os.environ['BLOG_BASE_URL']

    print(f'Keyfile: {GOOGLE_SEARCH_INDEXING_API["KEYFILE"]}')
    print(f'Files: {ALL_CHANGED_POST_FILES}')
    print(f'Base URL: {BASE_URL}')

    # Drop trailing slash if any
    if BASE_URL[-1] == '/':
        BASE_URL = BASE_URL[:-1]


    
except KeyError:
    print(f'Some required env vars were not resolved.')
    exit()

# _posts/2022-03-20-hello-world.md => 2022/03/20/hello-world.html
def postFilePathToUrlPath(s: str):
    return (s.replace('_posts/', '')
            .replace('-', '/', 3)
            .replace('.md', '.html'))


# print(SOME_SECRET)

# SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
# ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# service_account_file.json is the private key that you created for your service account.
# JSON_KEY_FILE = "/search_console/blog-project.json"
# credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

credentials = ServiceAccountCredentials.from_json(GOOGLE_SEARCH_INDEXING_API['KEYFILE'], scopes=GOOGLE_SEARCH_INDEXING_API['SCOPES'])
http = credentials.authorize(httplib2.Http())

# Define contents here as a JSON string.
# This example shows a simple update request.
# Other types of requests are described in the next step.

# content = """{
#   \"url\": \"https://google.com/2023/11/08/onyx-boox-max-battery-replacement-episode-2.html\",
#   \"type\": \"URL_UPDATED\"
# }"""

# response, content = http.request(ENDPOINT, method="POST", body=content)

# print('\n================================\n')
# print(response)
# print('\n================================\n')
# print(content)

def submitRequest(absoluteUrl: str):
    reqBody = f"""{{
  "url": "{absoluteUrl}",
  "type": "URL_UPDATED"
}}"""
    print(reqBody)
    # respHeaders, respBody = http.request(GOOGLE_SEARCH_INDEXING_API['ENDPOINT'], method="POST", body=reqBody)
    # print('\n================================\n')
    # print(respHeaders)
    # print('\n================================\n')
    # print(respBody)


# a = ["_posts/2022-03-20-hello-world.md", '_posts/2022-03-20-goodbye-world.md']
# for file in a:

for file in ALL_CHANGED_POST_FILES:
    relativeUrl = postFilePathToUrlPath(file)
    print(relativeUrl)
    absoluteUrl = f'{BASE_URL}/{relativeUrl}'
    submitRequest(absoluteUrl)