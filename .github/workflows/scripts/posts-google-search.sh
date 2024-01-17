# relative filepath => relative URL path
# _posts/2022-03-20-hello-world.md => 2022/03/20/hello-world.html
function filenameToUrlSlug(){
filePath=$1
echo $filePath | \
awk -F. '{ print $1 }' | \
awk -F/ '{ print $2 }' | \
awk -F- '{ printf "%s/%s/%s/", $1, $2, $3 ; for(i=4; i<=NF; i++) { printf "%s", $i; if(i<NF){ printf "-" } else { printf ".html" } } }'
}

# echo Hello from custom file! 👋
# echo $ALL_CHANGED_POST_FILES

for file in ${ALL_CHANGED_POST_FILES[*]}; do
  postUrl=$(filenameToUrlSlug $file)
  echo -e "File: $file\nPost URL: $postUrl"
done
