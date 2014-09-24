from pydht.pydht import DHT

import nacl.signing

key1 = nacl.signing.SigningKey.generate()

host1, port1 = 'localhost', 3000
dht1 = DHT(host1, port1, key1)


key2 = nacl.signing.SigningKey.generate()

host2, port2 = 'localhost', 3001
dht2 = DHT(host2, port2, key2, boot_host=host1, boot_port=port1)

dht1["test"] = "abcde"
print dht2["test"]
