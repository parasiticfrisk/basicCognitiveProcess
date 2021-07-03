<div align="center">

# Networking Essentials (CSCI 240)

![school-badge]
[![license-badge]][LICENSE]

</div>

<!-- badge info -->
[school-badge]:https://img.shields.io/badge/MJC-CSci%20240-silver?labelColor=darkblue&style=for-the-badge
[license-badge]:https://img.shields.io/github/license/parasiticfrisk/basic-cognitive-process?color=success&&style=for-the-badge
[LICENSE]:LICENSE "MIT License"

<br>

## Course Description:
Concepts of networking technologies. Includes networking standards and the OSI model, transmission  basics  and  media,  TCP/IP  protocols,  topologies  and  Ethernet  standards,  hardware,  WANs  and  remote  connectivity,  wireless  networking,  network  operating  systems, voice and video over IP, network security, network troubleshooting, integrity and availability of networks, and network management. Designed to assist individuals preparing for various certifications. Hands-on computer assignments required.

<br>

| <h3 align="center">Lab</h3> | <h3 align="center">Files</h3> | <h3 align="center">Goal</h3>                                                                                                                                                                               |
| --------------------------: | :---------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                          00 | [webget]                      | Use OS suppport to create a TCP stream socket, connect to a Web server, and fetch a page                                                                                                                   |
|                          00 | [byte_stream]                 | Create a flow-controlled in-memory byte stream                                                                                                                                                             |
|                          01 | [stream_reassembler]          | Create a stream reassembler that accepts a sequence of substrings—all excerpted from the same byte stream—and reassemble them back into the original stream                                                |
|                          02 | [wrapping_integers]           | Create a 32-bit wrapping integer—expressed relative to an arbitrary initial sequence number—used to express TCP sequence and acknowledgment numbers                                                        |
|                          02 | [tcp_receiver]                | Create the receiver part of a TCP implementation                                                                                                                                                           |
|                          03 | [tcp_sender]                  | Create the sender part of a TCP implementation                                                                                                                                                             |
|                          04 | [tcp_connection]              | Create an implementation of a TCP connection                                                                                                                                                               |
|                          05 | [network_interface]           | Create an implementation of a network interface that that translates from {IP datagram, next hop address} to link-layer frame, and from link-layer from to IP datagram                                     |
|                          06 | [router]                      | Create an implementation of an IP router using network_interface, which given an incoming Internet datagram, can decide (1) which interface to send it out on, and (2) what next hop address to send it to |
|                          07 | [lab7]                        | Combine all previous labs to create a network stack to communicate with another student's network stack                                                                                                    |

<!-- lab quick links -->
[webget]:sponge/apps/webget.cc
[byte_stream]:sponge/libsponge/byte_stream.cc
[stream_reassembler]:sponge/libsponge/stream_reassembler.cc
[wrapping_integers]:sponge/libsponge/wrapping_integers.cc
[tcp_receiver]:sponge/libsponge/tcp_receiver.cc
[tcp_sender]:sponge/libsponge/tcp_sender.cc
[tcp_connection]:sponge/libsponge/tcp_connection.cc
[network_interface]:sponge/libsponge/network_interface.cc
[router]:sponge/libsponge/router.cc
[lab7]:sponge/apps/lab7.cc

<br>

---
#### Notice
By viewing and/or interacting with these files as a current or future student of computer science, computer electronics, computer information systems, or related field of study, you agree to the terms of the [Academic Honesty Policy].

[Academic Honesty Policy]:../academic_honesty_policy
