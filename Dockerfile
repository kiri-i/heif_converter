FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
RUN pip3 install \
    Pillow \
    pyheif \
    fire \
    tqdm
CMD ["/bin/bash"]