#!/bin/bash
	analyze_size () {
	local item=$1
	du -h --max-depth=0 "$item"
}
main() {
	temp_file=$(mktemp)
	for item in *; do
	  if [[ -d $item ]]; then
            analyze_size "$item" >> "$temp_file"
           fi
        done
	echo "Sorted analyses of directory sizes:"
	sort -hr "$temp_file"
	rm "$temp_file"
}
main 
