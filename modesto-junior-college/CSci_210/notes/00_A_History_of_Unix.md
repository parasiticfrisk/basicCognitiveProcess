# A Brief History of Unix

- 1969: Unix invented at Bell Labs by Ken Thompson, Dennis Ritchie & others.
- 1971: First Edition used for text processing of patent documents.
- 1973: Fourth Edition was rewritten in C making it portable and started the OS revolution.
- 1975: Sixth Edition was made available outside of Bell Labs. BSD forks from here at Berkeley.
- 1979: Seventh Edition was improvement over all prior versions, debuted C language tools and Bourne shell.
- 1982: System III is the first public release of Unix outside of Bell Labs. SunOS and HP-UX fork from here.
- 1983: System V is the first supported release by AT&T with an installation base of 45,000.
- 1986: 4.3BSD released with TCP/IP and NFS. AIX announced by IBM. Install base 250,000.
- 1991: Linus Torvalds commences Linux Development. Solaris 1.0 debuts.
- 1994: Single Unix specification announced, separates trademark from specific code instances.
- 1994: First release of Red Hat Linux and Debian Linux, which become the dominant flavors of Linux. 
- 1995: Toy Story, first feature-length computer-animated film, produced on Solaris workstations.
- 1997: Titanic is the first major film to be largely produced on Linux servers.
- 1999: Linux Kernel 2.2 released to celebrate Unix's 30th birthday.
- 2001: Apple releases Mac OS X, based on BSD Unix.
- 2003: Linux 2.6 kernel released. Red Hat creates RHEL and Fedora.
- 2004: Ubuntu, a popular desktop Linux distribution based on Debian, first released.
- 2007: Mac OS X certified to Unix standard.
- 2010: Apple reports 50 million desktops and growing, all Certified Unix Systems.
- 2011: Linux kernel 3.2 released to mark Linux's 20th birthday.
- 2012: 500 million Android (Linux) and iOS (Darwin) devices have been sold world wide.
- 2013: All 10 of the top 10 supercomputers in the world run Linux today.

#### **A note on learning UNIX by Paul Murphy of ZDNet**

"Basically, to learn Unix you learn to understand and apply a small set of key ideas and achieve expertise by expanding both the set of ideas and your ability to apply them[.]"

## **Command Prompt**

When you login to a system you will be presented with what is referred to as a command prompt. This usually has some basic information about you as the user, as well as the machine you are logged into and the directory you are currently in.

#### Example: `[user@hostname ~]$`

### **Command line is awesome!!**

- Faster and easier to document, share, reproduce, automate.
- Much faster for complex or repetitive tasks. 
- Spaces and unusual characters in filenames make command line tools more difficult to use. (NB: this is not actually awesome)

### **ssh - Secure Shell**

Ssh (Secure Shell) is a protocol used to exchange data securely between systems, most commonly for interactive shell and file transfers.

On Mac OS X or other Linux or UNIX systems, simply use the ssh command to connect to remote hosts. On Windows, there are a variety of clients, one of the most popular and easy to use is PuTTY (freeware).

#### Example:

    [user@localhost ~]$ ssh PirateId@login.jmkll.org
    PirateId@login.jmkll.org's password:
    [user@compute ~]$

On the first connection to a host you will need to accept the host key.  For Mac and Linux systems, if your username is the same as your PirateId you can omit it.