# CS240 - Changelog

<br>
All noteable changes to this course will be documented in this file.

<br>

## [Unreleased]

<br>

## [Lab 07] - 2017.12.06
### Changed
- apps
  - `CMakeLists.txt`

### Added
- apps
  - `lab07.cc`

<br>

## [Lab 06] - 2017.11.22
### Changed
- apps
  - `CMakeLists.txt`

### Added
- apps
  - network_simulator
- libsponge
  - `router.hh`
  - `router.cc`

<br>

## [Lab 05] - 2017.11.08
### Changed
- apps
  - `CMakeLists.txt`
- tests
  - `CMakeLists.txt`

### Added
- apps
  - tcp_ip_ethernet
- libsponge
  - tcp_helpers
    - arp_message
    - ethernet_frame
    - ethernet_header
- tests
  - net_interface
  - network_interface_test_harness
- `tap.sh`

<br>

## [Lab 04] - 2017.10.25
### Changed
- apps
  - `CMakeLists.txt`
  - `webget.cc`
- etc
  - `tests.cmake`
- libsponge
  - `byte_stream.hh`
  - `byte_stream.cc`
  - `tcp_sender.hh`
  - `tcp_sender.cc`
- tests
  - `CMakeLists.txt`

### Added
- apps
  - bidirectional_stream_copy
  - tcp_benchmark
  - tcp_ipv4
  - tcp_native
  - tcp_udp
  - tun
  - udp_tcpdump
- libsponge
  - tcp_helpers
    - fd_adapter
    - ipv4_datagram
    - ipv4_header
    - lossy_fd_adapter
    - tcp_over_ip
    - tcp_sponge_socket
    - tuntap_adapter
  - `tcp_connection.hh`
  - `tcp_connection.cc`
- tests
  - fsm_ack_rst_relaxed
  - fsm_ack_rst_win_relaxed
  - fsm_active_close
  - fsm_connect_relaxed
  - fsm_listen_relaxed
  - fsm_loopback
  - fsm_loopback_win
  - fsm_passive_close
  - fsm_reorder
  - fsm_retx
  - fsm_retx_relaxed
  - fsm_retx_win
  - fsm_winsize
  - ipv4_parser
  - tcp_expectation
  - tcp_expectation_forward
  - tcp_fsm_test_harness
  - test_utils_ipv4
- `tun.sh`
- `txrx.sh`

<br>

## [Lab 03] - 2017.10.18
### Changed
- etc
  - `tests.cmake`
- tests
  - `CMakeLists.txt`

### Added
- libsponge
  - tcp_helpers
    - tcp_config
  - `tcp_sender.hh`
  - `tcp_sender.cc`
- tests
  - send_ack
  - send_close
  - send_connect
  - send_equivalence_checker
  - send_extra
  - send_retx
  - send_transmit
  - send_window
  - sender_harness

<br>

## [Lab 02] - 2017.10.04
### Changed
- etc
  - `tests.cmake`
- tests
  - `CMakeLists.txt`

### Added
- libsponge
  - tcp_helpers
    - tcp_header
    - tcp_segment
    - tcp_state
  - `tcp_receiver.hh`
  - `tcp_receiver.cc`
  - `wrapping_integer.hh`
  - `wrapping_integer.cc`
- tests
  - receiver_harness
  - recv_close
  - recv_connect
  - recv_reorder
  - recv_special
  - recv_transmit
  - recv_window
  - string_conversions
  - test_utils
  - tcp_parser
  - wrapping_integers_cmp
  - wrapping_integers_roundtrip
  - wrapping_integers_unwrap
  - wrapping_integers_wrap

<br>

## [Lab 01] - 2017.09.27
### Changed
- etc
  - `tests.cmake`
- tests
  - `CMakeLists.txt`

### Added
- libsponge
  - `stream_reassembler.hh`
  - `stream_reassembler.cc`
- tests
  - fsm_stream_reassembler_cap
  - fsm_stream_reassembler_dup
  - fsm_stream_reassembler_harness
  - fsm_stream_reassembler_holes
  - fsm_stream_reassembler_many
  - fsm_stream_reassembler_overlapping
  - fsm_stream_reassembler_seq
  - fsm_stream_reassembler_single
  - fsm_stream_reassember_win

<br>

## [Lab 00] - 2017.09.20
### Added
- apps
  - `CMakeLists.txt`
  - `webget.cc`
- libsponge
  - `byte_stream.hh`
  - `byte_stream.cc`
- tests
  - CMakeLists.txt
  - byte_stream_capacity
  - byte_stream_construction
  - byte_stream_many_writes
  - byte_stream_one_write
  - byte_stream_test_harness
  - byte_stream_two_writes
  - test_err_if
  - test_should_be
  - webget_t

<br>

## [Initialization] - 2017.09.13
### Added
- `Dockerfile`
#### Sponge
- etc
- doctests
- libsponge 
  - util
    -  address
    -  buffer
    -  eventloop
    -  file_descriptor
    -  parser
    -  socket
    -  tun
    -  util
- .clang-format
- .gitignore
- CMakeLists.txt