import sys
import zmq


def sync(connect_to: str) -> None:
    # use connect socket + 1
    sync_with = ':'.join(
        connect_to.split(':')[:-1] + [str(int(connect_to.split(':')[-1]) + 1)]
    )
    ctx = zmq.Context.instance()
    s = ctx.socket(zmq.REQ)
    s.connect(sync_with)
    s.send(b'READY')
    s.recv()
  

def main() -> None:
    if len(sys.argv) != 2:
        print('usage: subscriber <connect_to>')
        sys.exit(1)

    connect_to = sys.argv[1]

    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(connect_to)
    s.setsockopt(zmq.SUBSCRIBE, b'')

    sync(connect_to)

    while True:
        a = s.recv_pyobj()
        print(a)


if __name__ == "__main__":
    main()


