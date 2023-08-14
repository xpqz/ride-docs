



# Sample Configuration File


A .ini configuration file can be used to define settings for the RIDE_INIT configuration parameter.


Examples of the fields that you might want to include within the .ini configuration file are:
```
[RIDE]
Direction=Listen
Address=
Port=5002
MaxBlockSize=52428800
SSLValidation=0
Protocol=IPv4
Secure=Secure
PublicCertFile= C:\apps\d150U64\TCerts\server\localhost-cert.pem
PrivateKeyFile= C:\apps\d150U64\TCerts\server\localhost-key.pem
RootCertDir= C:\apps\d150U64\TCertss\ca
Priority=
AcceptCertDir= C:\apps\d150U64\TCerts\accept
```


where:

- `Direction`, `Address` and `Port` – as defined for the RIDE_INIT configuration parameter (see [Section ](ride_init.md#)). `Direction` in the .ini file is equivalent to `mode` in the RIDE_INIT configuration parameter and has possible values of `Listen` (equivalent to RIDE_INIT's `Serve`), `Connect`, `Poll` and `HTTP`. No defaults are defined for `Direction` and `Address`; the default for `Port` is `4502`. Overridden if defined in RIDE_INIT.
- `MaxBlockSize` is the maximum size (in bytes) allocated to the buffer that receives data transmissions. The default is 16,777,216.
- `SSLValidation` is the sum of the relevant TLS flags (see [Section ](tls_flags.md#)). The default is `0`. Validity depends on the value of the `Secure` field.
- `Protocol` is the communication protocol to use. Possible values are:`IPv4`: use the IPv4 connection protocol; if this is not possible then generate an error.`IPv6`: use the IPv6 connection protocol; if this is not possible then generate an error.<empty>: use the IPv6 connection protocol; if this is not possible then use the IPv4 connection protocol. This is the default.
- `IPv4`: use the IPv4 connection protocol; if this is not possible then generate an error.
- `IPv6`: use the IPv6 connection protocol; if this is not possible then generate an error.
- <empty>: use the IPv6 connection protocol; if this is not possible then use the IPv4 connection protocol. This is the default.
- `Secure` specifies the security of the connection. Possible values depend on the value of `Direction`:If `Direction` is `Listen`, then `Secure` can be:`Secure` – the connection is secure and certificates are provided. The `PublicCertFile`, `PrivateKeyFile`, `SSLValidation` and `Priority` fields are valid.<empty> – the connection is unencrypted. This is the default.If `Direction` is `Connect` or `Poll`, then `Secure` can be:`Secure` – the connection is secure and certificates are provided. The `PublicCertFile`, `PrivateKeyFile`, `SSLValidation` and `Priority` fields are valid.<empty> – the connection is unencrypted. This is the default.`Anonymous` – the connection is secure but no certificate is provided on the client side. The `SSLValidation` and `Priority fields` are valid.
- If `Direction` is `Listen`, then `Secure` can be:`Secure` – the connection is secure and certificates are provided. The `PublicCertFile`, `PrivateKeyFile`, `SSLValidation` and `Priority` fields are valid.<empty> – the connection is unencrypted. This is the default.
- `Secure` – the connection is secure and certificates are provided. The `PublicCertFile`, `PrivateKeyFile`, `SSLValidation` and `Priority` fields are valid.
- <empty> – the connection is unencrypted. This is the default.
- If `Direction` is `Connect` or `Poll`, then `Secure` can be:`Secure` – the connection is secure and certificates are provided. The `PublicCertFile`, `PrivateKeyFile`, `SSLValidation` and `Priority` fields are valid.<empty> – the connection is unencrypted. This is the default.`Anonymous` – the connection is secure but no certificate is provided on the client side. The `SSLValidation` and `Priority fields` are valid.
- `Secure` – the connection is secure and certificates are provided. The `PublicCertFile`, `PrivateKeyFile`, `SSLValidation` and `Priority` fields are valid.
- <empty> – the connection is unencrypted. This is the default.
- `Anonymous` – the connection is secure but no certificate is provided on the client side. The `SSLValidation` and `Priority fields` are valid.
- `PublicCertFile` is the fully-qualified path to, and name of, the file containing the public certificate. Empty by default. Validity depends on the value of the `Secure` field.
- `PrivateKeyFile` is the fully-qualified path to, and name of, the file containing the private key. Empty by default. Validity depends on the value of the `Secure` field.
- `RootCertDir` is the full path to (and name of) the directory that contains Certificate Authority root certificates. Empty by default (on the Microsoft Windows operating system, the RIDE uses the Microsoft certicate store).
- `Priority` is the GnuTLS priority string (for complete documentation of this, see http://www.gnutls.org/manual/gnutls.html#Priority-Strings). Empty by default. Validity depends on the value of the `Secure` field.
- `AcceptCertDir` is the full path to (and name of) the directory that contains the public certificates of all users that are allowed to connect. Empty by default.

Two additional sections can be included within the .ini configuration file to control the IP addresses that are allowed or denied access to the connection. These are:
```
[AllowEndPoints]
[DenyEndPoints]
```


For each of these, IPv6/IPv4 addresses and/or address ranges can be specified (multiple entries must be separated by commas). For example:
```
[AllowEndPoints]
IPV4=192.168.100.0/24,192.168.17.0/24,127.0.0.0/10
IPV6= fe80:ccbd:aa34:3cfb::0/64
```
```
[DenyEndPoints]
IPV4=212.0.0.0/8
IPV6= 2a02:2658:1012::35/64
```


If `AllowEndPoints` is not included, all IP addresses are allowed to access the connection unless explicitly denied access with the `DenyEndPoints` field.


