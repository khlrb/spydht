import uuid
from spydht.spydht import DHT
import nacl.signing
host1, port1 = '176.9.147.116', 3000
key2 = nacl.signing.SigningKey.generate()
host2, port2 = '0.0.0.0', 3017
dht2 = DHT(host2, port2, key2, boot_host=host1, boot_port=port1)
unique_key = str(uuid.uuid4())
dht2[unique_key] = "new valuesdfsdfsdf"
dht2[unique_key] = "3333333"
print(dht2[unique_key])
dht2[unique_key] = "77777"
print(dht2[unique_key])
