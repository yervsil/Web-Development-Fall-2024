FROM golang:1.23 as builder

WORKDIR /app

COPY . .

RUN go build -o hello .

FROM alpine:latest

WORKDIR /app

COPY --from=builder /app/hello .

CMD ["./hello"]