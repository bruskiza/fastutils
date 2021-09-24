from smartsutils import main

def test_main(event_loop):
    resp = event_loop.run_until_complete(main.root())
    assert resp is not None

def test_ping(event_loop, fake_process):
    fake_process.register_subprocess(
        "ping -c 1 127.0.0.1".split(" "), stdout="fake ping"
    )
    resp = event_loop.run_until_complete(main.ping())
    assert resp is not None

def test_snmpwalk(event_loop, fake_process):
    fake_process.register_subprocess(
        "snmpwalk -v 2c -c public 127.0.0.1".split(" "), stdout="it worked!"
    )
    resp = event_loop.run_until_complete(main.snmpwalk())
    assert resp is not None
