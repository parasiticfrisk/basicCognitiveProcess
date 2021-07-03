//
// Author: August Frisk
// Course: CSci 240 - Fall 2017
// Assign: Lab 00
// File: byte_stream.cc
//
// Description: Implementation of a flow-controlled in-memory byte stream.
//

#include "byte_stream.hh"

using namespace std;

ByteStream::ByteStream(const size_t capacity) { _capacity = capacity; }

size_t ByteStream::write(const string &data) {
    size_t len = data.length();
    len = len < _capacity - _buffer.size() ? len : _capacity - _buffer.size();
    _bytes_written += len;
    _buffer.append(BufferList(move(string().assign(data.begin(), data.begin() + len))));
    return len;
}

//! \param[in] len bytes will be copied from the output side of the buffer
string ByteStream::peek_output(const size_t len) const {
    size_t length = min(len, _buffer.size());
    string s = _buffer.concatenate();
    return string().assign(s.begin(), s.begin() + length);
}

//! \param[in] len bytes will be removed from the output side of the buffer
void ByteStream::pop_output(const size_t len) {
    size_t length = min(len, _buffer.size());
    _bytes_read += length;
    _buffer.remove_prefix(length);
}

//! Read (i.e., copy and then pop) the next "len" bytes of the stream
//! \param[in] len bytes will be popped and returned
//! \returns a string
std::string ByteStream::read(const size_t len) {
    size_t length = min(len, _buffer.size());
    string res = peek_output(length);
    pop_output(length);
    return res;
}

void ByteStream::end_input() { _input_ended = true; }

bool ByteStream::input_ended() const { return _input_ended; }

size_t ByteStream::buffer_size() const { return _buffer.size(); }

bool ByteStream::buffer_empty() const { return _buffer.size() == 0; }

bool ByteStream::eof() const { return buffer_empty() && input_ended(); }

size_t ByteStream::bytes_written() const { return _bytes_written; }

size_t ByteStream::bytes_read() const { return _bytes_read; }

size_t ByteStream::remaining_capacity() const { return _capacity - _buffer.size(); }
