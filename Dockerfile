FROM ubuntu:20.04

WORKDIR /app 
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
 && pip3 install -r ./requirements.txt
CMD ["/bin/bash"]