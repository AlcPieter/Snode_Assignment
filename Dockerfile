FROM timberio/vector:0.34.0-alpine

WORKDIR /etc/vector

COPY vector.toml .

CMD ["--config", "/etc/vector/vector.toml"]