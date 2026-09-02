# Lab 2: URL Lister Solution

## Approach & Software Requirements
- **Language/Environment**: Python 3, Apache Hadoop Streaming
- **Mapper (`URLMapper.py`)**: Uses Python's `re` module with regular expression `href="([^"]+)"` to extract links from raw HTML, outputting KV pairs of `URL\t1`.
- **Reducer (`URLReducer.py`)**: Reads sorted input from STDIN, aggregates counts per URL, and filters for counts strictly greater than 5.

## Resources Used
- **Dataproc Cluster Configuration**:
gcloud dataproc clusters create test-dataproc \
    --project=lab2-470203-507403 \
    --region=us-east4 \
    --zone=us-east4-a \
    --master-machine-type=e2-standard-2 \
    --master-boot-disk-size=50GB \
    --worker-machine-type=e2-standard-2 \
    --worker-boot-disk-size=50GB \
    --num-workers=2/4 \
    --public-ip-address
- **Collaborators**: None

## Performance & Execution Time Comparison
- **2 Worker Nodes Execution Time**: 1m 40.735s
- **4 Worker Nodes Execution Time**: 1m 48.532s

### Discussion of Results
Adding two additional worker nodes caused the job runtime to increase by approximately 8 seconds instead of speeding up. 
Because the input dataset is tiny, the actual processing work took less than a second.

jovyan@jupyter-vrpa3077:~/(CSCI-5253)DatacenterScaleComputing/lab2-url-lister/input$ du -sh *
393K    file01
410K    file02

The extra time was spent on Hadoop's management overhead: 
1. A 4-node cluster had to split the data into 22 pieces (instead of 10)
2. Spin up more virtual workspaces across separate machines
3. Route data over the network between 4 computers instead of 2. 

This demonstrates that for small datasets, administrative setup time outweighs the performance gains of parallel processing.

Two Nodes:
real    1m40.735s
user    0m15.129s
sys     0m0.981s

Four Nodes:
real    1m48.532s
user    0m14.689s
sys     0m0.929s
