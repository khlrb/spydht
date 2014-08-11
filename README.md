pydht
==========

forked from [isaaczafuta/pydht](https://github.com/isaaczafuta/pydht)


Python implementation of the Kademlia DHT data store.

Useful for distributing a key-value store in a decentralized manner.

Example: a two node DHT

```python
from pydht import DHT

import nacl.signing

key1 = nacl.signing.SigningKey.generate()

host1, port1 = 'localhost', 3000
dht1 = DHT(host1, port1, key1)


key2 = nacl.signing.SigningKey.generate()

host2, port2 = 'localhost', 3001
dht2 = DHT(host2, port2, boot_host=host1, boot_port=port1)

dht1["my_key"] = [u"My", u"json-serializable", u"Object"]


print dht2["my_key"]
```
