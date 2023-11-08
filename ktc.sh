echo_if_not_empty() {
    [[ ${#1} -gt 0 ]] && echo $1
}

tmp_file_path="$(dirname $0)/tmp.jar"

echo_if_not_empty $(kotlinc $(realpath $1) -include-runtime -d $tmp_file_path)
echo $(java -jar $tmp_file_path)
echo_if_not_empty $(rm -rf $tmp_file_path)