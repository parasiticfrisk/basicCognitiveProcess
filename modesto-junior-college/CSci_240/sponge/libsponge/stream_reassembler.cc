//
// Author: August Frisk
// Course: CSci 240 - Fall 2017
// Assign: Lab 01
// File: stream_reassembler.cc
//
// Description: A stream reassembler.
//

#include "stream_reassembler.hh"

using namespace std;

StreamReassembler::StreamReassembler(const size_t capacity) : _output(capacity), _capacity(capacity) {
    _buffer.resize(capacity);
}

//! \details This function accepts a substring (aka a segment) of bytes,
//! possibly out-of-order, from the logical stream, and assembles any newly
//! contiguous substrings and writes them into the output stream in order.
void StreamReassembler::push_substring(const string &data, const size_t index, const bool eof) {
    // over capacity
    if (index >= _head_index + _capacity) {
        return;
    }

    // handle extra substring prefix
    block_node elm;
    // emtpy substring
    if (index + data.length() <= _head_index) {
        goto JUDGE_EOF;
    } else if (index < _head_index) {
        size_t offset = _head_index - index;
        elm.data.assign(data.begin() + offset, data.end());
        elm.begin = index + offset;
        elm.length = elm.data.length();
    } else {
        elm.begin = index;
        elm.length = data.length();
        elm.data = data;
    }
    _unassembled_byte += elm.length;

    // merge substring
    do {
        // merge next
        long merged_bytes = 0;
        auto iter = _blocks.lower_bound(elm);
        while (iter != _blocks.end() && (merged_bytes = merge_block(elm, *iter)) >= 0) {
            _unassembled_byte -= merged_bytes;
            _blocks.erase(iter);
            iter = _blocks.lower_bound(elm);
        }
        // merge prev
        if (iter == _blocks.begin()) {
            break;
        }
        iter--;
        while ((merged_bytes = merge_block(elm, *iter)) >= 0) {
            _unassembled_byte -= merged_bytes;
            _blocks.erase(iter);
            iter = _blocks.lower_bound(elm);
            if (iter == _blocks.begin()) {
                break;
            }
            iter--;
        }
    } while (false);
    _blocks.insert(elm);

    // write to ByteStream
    if (!_blocks.empty() && _blocks.begin()->begin == _head_index) {
        const block_node head_block = *_blocks.begin();
        // modify _head_index and _unassembled_byte according to successful write to _output
        size_t write_bytes = _output.write(head_block.data);
        _head_index += write_bytes;
        _unassembled_byte -= write_bytes;
        _blocks.erase(_blocks.begin());
    }

JUDGE_EOF:
    if (eof) {
        _eof_flag = true;
    }
    if (_eof_flag && empty()) {
        _output.end_input();
    }
}

size_t StreamReassembler::unassembled_bytes() const { return this->_unassembled_byte; }

bool StreamReassembler::empty() const { return this->_unassembled_byte == 0; }

long StreamReassembler::merge_block(block_node &elm1, const block_node &elm2) {
    block_node x, y;
    if (elm1.begin > elm2.begin) {
        x = elm2;
        y = elm1;
    } else {
        x = elm1;
        y = elm2;
    }
    if (x.begin + x.length < y.begin) {
        return -1;  // no intersection, couldn't merge
    } else if (x.begin + x.length >= y.begin + y.length) {
        elm1 = x;
        return y.length;
    } else {
        elm1.begin = x.begin;
        elm1.data = x.data + y.data.substr(x.begin + x.length - y.begin);
        elm1.length = elm1.data.length();
        return x.begin + x.length - y.begin;
    }
}