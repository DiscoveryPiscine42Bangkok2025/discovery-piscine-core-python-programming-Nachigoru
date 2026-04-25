import sys

if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]

    print(f"Parameters: {len(params)}")

    for p in params:
        print(f"{p}: {len(p)}")