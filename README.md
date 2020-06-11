# PortScanner
A port scanner that checks the status of TCP ports using Python's socket library. It can be used for diagnostics and making sure a certain port is open for specified use.
socket library was used, a socket is first created using socket library “socket” function, where it uses “AF_INET “ address family(IPv4) and socket type as “SOCK_STREAM” for TCP connections. “gethostbyname” function was used to translate the host name to IPv4 address format. Finally, it checks the ports status by trying to connect to each of the specified ports, this is done using “connect_ex” function to connect to an address with specified port, the function returns error indicator 0 if operation is successful, if not it returns “errono” value. This process keeps looping for the port range specified.
