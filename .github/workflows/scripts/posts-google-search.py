from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import os
import json

GOOGLE_SEARCH_INDEXING_API = {
    'SCOPES' : [ "https://www.googleapis.com/auth/indexing" ],
    'ENDPOINT': "https://indexing.googleapis.com/v3/urlNotifications:publish",
    'KEYFILE': None
}

try:
    GOOGLE_SEARCH_INDEXING_API['KEYFILE'] = json.loads(os.environ['GOOGLE_SEARCH_INDEXING_API_KEYFILE'])
    ALL_CHANGED_POST_FILES = os.environ['ALL_CHANGED_POST_FILES'].split(' ')
    BASE_URL = os.environ['BLOG_BASE_URL']

    # print(f'Keyfile: {GOOGLE_SEARCH_INDEXING_API["KEYFILE"]}')
    # print(f'Files: {ALL_CHANGED_POST_FILES}')
    # print(f'Base URL: {BASE_URL}')

    # Drop trailing slash if any
    if BASE_URL[-1] == '/':
        BASE_URL = BASE_URL[:-1]

except KeyError:
    print(f'Some required env vars were not resolved 👿')
    exit(-1)

# '_posts/2022-03-20-hello-world.md' => '2022/03/20/hello-world.html'
def postFilePathToUrlPath(s: str):
    return (s.replace('_posts/', '')
            .replace('-', '/', 3)
            .replace('.md', '.html'))

credentials = ServiceAccountCredentials.from_json_keyfile_dict(GOOGLE_SEARCH_INDEXING_API['KEYFILE'], scopes=GOOGLE_SEARCH_INDEXING_API['SCOPES'])
http = credentials.authorize(httplib2.Http())

def submitRequest(absoluteUrl: str):
    reqBody = f"""{{
  "url": "{absoluteUrl}",
  "type": "URL_UPDATED"
}}"""
    print(f'Request to be submitted:\n{reqBody}')
    # respHeaders, respBody = http.request(GOOGLE_SEARCH_INDEXING_API['ENDPOINT'], method="POST", body=reqBody)
    # print(f'Response headers: {respHeaders}')
    # print(f'Response body: {respBody}')

for file in ALL_CHANGED_POST_FILES:
    if not file: continue

    relativeUrl = postFilePathToUrlPath(file)
    absoluteUrl = f'{BASE_URL}/{relativeUrl}'
    
    print(f'File: {file}')
    print(f'Relative URL: {relativeUrl}')
    print(f'Absolute URL: {absoluteUrl}')
    
    submitRequest(absoluteUrl)

    print('\n-----------------\n')