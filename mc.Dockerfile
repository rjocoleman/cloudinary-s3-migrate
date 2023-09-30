FROM minio/mc as mc

FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y \
    curl \
    ca-certificates \
    passwd \
    util-linux \
    gzip \
    lsof \
    tar \
    net-tools \
    jq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=mc /usr/bin/mc /usr/bin/mc

CMD ["/bin/sh"]
