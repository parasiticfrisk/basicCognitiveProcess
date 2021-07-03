//
// Author: August Frisk
// Course: CSci 240 - Fall 2017
// Assign: Lab 00
// File: webget.cc
//
// Description: This program utlilizes the operating system's pre-existing
//              support for the Transmission Control Protocol to create a TCP
//              stream socket, connect to a Web server, and fetch a page.
//

#include "socket.hh"
#include "tcp_sponge_socket.hh"
#include "util.hh"

#include <cstdlib>
#include <iostream>

using namespace std;

void get_URL(const string &host, const string &path) {

    const Address webserver(host, "http");
    FullStackSocket tcp_socket;
    tcp_socket.connect(webserver);
    tcp_socket.write("GET " + path + " HTTP/1.1\r\n");
    tcp_socket.write("Host: " + host + "\r\n");
    tcp_socket.write("Connection: close\r\n");
    tcp_socket.write("\r\n");
    auto recvd = tcp_socket.read();
    // HTTP/1.1 200 OK
    // Content-type: text/plain
    string res = "";
    for (auto c : recvd) {
        if (c != '\n' && c != '\r')
            res.push_back(c);
    }
    while (recvd.length() != 0) {
        recvd = tcp_socket.read();
        if (recvd == "" || recvd == "\n" || recvd == "\r\n" || recvd == "\r")
            continue;
        for (auto c : recvd) {
            if (c != '\n' && c != '\r')
                res.push_back(c);
        }
    }
    cout << res.substr(56) << endl;
    tcp_socket.close();

    tcp_socket.wait_until_closed();
}

int main(int argc, char *argv[]) {
    try {
        if (argc <= 0) {
            abort();  // For sticklers: don't try to access argv[0] if argc <= 0.
        }

        // The program takes two command-line arguments: the hostname and "path" part of the URL.
        // Print the usage message unless there are these two arguments (plus the program name
        // itself, so arg count = 3 in total).
        if (argc != 3) {
            cerr << "Usage: " << argv[0] << " HOST PATH\n";
            cerr << "\tExample: " << argv[0] << " stanford.edu /class/cs144\n";
            return EXIT_FAILURE;
        }

        // Get the command-line arguments.
        const string host = argv[1];
        const string path = argv[2];

        // Call the student-written function.
        get_URL(host, path);
    } catch (const exception &e) {
        cerr << e.what() << "\n";
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
