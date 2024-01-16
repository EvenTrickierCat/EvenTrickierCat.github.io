# filename => path
# _posts/2022-03-20-hello-world.md => 2022/03/20/hello-world.html
function filenameToUrlSlug(){
$fileName=$1

# echo $s | awk -F/ '{ print $2 }'
# echo $s | awk -F. '{ print $1 }' | awk -F/ '{ print $2 }' | awk -F- '{ print $1"/"$2"/"$3"/" }'
# echo $s | awk -F. '{ print $1 }' | awk -F/ '{ print $2 }' | awk -F- '{ printf "%s/%s/%s/", $1, $2, $3 ; for(i=4; i<=NF; i++) { printf "%s", $i; if(i<NF){ printf "-" } else { printf ".html" } } }'

echo $fileName | awk -F. '{ print $1 }' | awk -F/ '{ print $2 }' | awk -F- '{ printf "%s/%s/%s/", $1, $2, $3 ; for(i=4; i<=NF; i++) { printf "%s", $i; if(i<NF){ printf "-" } else { printf ".html" } } }'

}

echo Hello from custom file! 👋
echo $ALL_CHANGED_POST_FILES


