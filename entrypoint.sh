#!/bin/sh
set -e

# run init.sh
init.sh &

# extract the node information
OUTPUTFILE=${1:-"/tmp/output.json"}
echo -n > "$OUTPUTFILE"
until cat "$OUTPUTFILE" | grep '{'; do
    curl -sf localhost:8188/object_info |
        jq 'to_entries 
            | map(select(.value.python_module == "custom_nodes.'$CUSTOM_NODE_NAME'")) 
            | if length > 0 then from_entries else "" end' |
        tee "$OUTPUTFILE"
    sleep 1
done