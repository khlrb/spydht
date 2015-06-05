spydht
==========

forked from [isaaczafuta/pydht](https://github.com/isaaczafuta/pydht)


Python 2 and Python 3 implementation of the Kademlia DHT data store.

Useful for distributing a key-value store in a decentralized manner.

Nodes only update values, if they're signed with the same key.

Example: a two node DHT

```python
from spydht.spydht import DHT

import nacl.signing

key1 = nacl.signing.SigningKey.generate()

host1, port1 = 'localhost', 3000
dht1 = DHT(host1, port1, key1)


key2 = nacl.signing.SigningKey.generate()

host2, port2 = 'localhost', 3001
dht2 = DHT(host2, port2, key2, boot_host=host1, boot_port=port1)

dht1["test"] = ["My", "json-serializable", "Object"]


print(dht2["test"])
```

See remote_example.py for bootstrapping from a remote DHT.
