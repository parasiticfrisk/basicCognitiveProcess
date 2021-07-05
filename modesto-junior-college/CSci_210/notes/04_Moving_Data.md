# Unit 04: Exploring Methods of Moving Data

### **scp**

Scp (Secure Copy) transfers one or more files to or from a remote host via the SSH protocol. Therefore, you can transfer data into and out of nearly any server with SSH configured (see how SSH is incredibly useful?).

#### Example:

    [user@compute ~]$ scp largefile.10g user@compute2.dept.duke.edu:/home/user/
    largefile.10g    100%  10GB 21.4MB/s  07:59

### **sftp**

SFTP (Secure FTP) is designed for secure file transfer (also over SSH, but requires more configuration on the server), and is run in an interactive mode with commands.

### **wget**

Wget (Web Get) is a handy program that downloads a file from a web site or FTP server. For example, if you find a download link to a .tar file containing a program you'd like to install on a server, simply copy the URL from your browser and paste it to your terminal after the wget command, and it will download that file to the remote server in the current directory.

### **rsync**

Rsync (Remote Sync) is a very powerful tool for transferring, replicating, and verifying a set of files from one directory to another, often over a network (using, you guessed it, SSH). rsync is also able to resume an interrupted transfer, which is very handy when a multi-gigabyte transfer fails at 97%.

#### *Useful flags:*

    -r    recursive: copy the contents of folders.
    -P    show progress of transfers, and allow partial transfers to be resumed.
    -a    archive mode: copy full contents of folders, preserving file ownership,
          permissions, and timestamps. This is useful when making a backup of 
          a directory or a whole computer.

#### Example:

    user@localhost ~ $ ls -l foo/
    bar baz testfile
    user@localhost ~ $ rsync -Pa foo compute01.dept.duke.edu:
    sending incremental file list
    foo/
    foo/bar		3765 100%  0.00kB/s  0:00:00 (xfer#1, to-check=2/4)
    foo/baz		2825 100% 183.92kB/s  0:00:00 (xfer#2, to-check=1/4)
    foo/testfile	1778 100% 115.76kB/s  0:00:00 (xfer#3, to-check=0/4)
    sent 8594 bytes received 73 bytes 17334.00 bytes/sec
    total size is 8368 speedup is 0.97

## **Version control**

Projects involving multiple authors often use a version control system to keep track of changes. The most common version control system at the moment is git.

### **git**

Git is a distributed version control and source code management system.

#### *Useful Commands:*

    git clone    creates a local copy of an online git repository
    git add      adds a new or modified file to be tracked in the staging area
    git commit   sends tracked files in the staging area to the parent repository 
    git status   shows untracked files, and files you've changed since the last commit
    git diff     shows the differences between your working directory and the parent
                 repository, or between two commits

#### Example:

    [user@compute ~]$ $ git clone https://github.com/scipy/scipy
    Cloning into 'scipy'...
    remote: Counting objects: 91976, done.
    remote: Compressing objects: 100% (31/31), done.
    remote: Total 91976 (delta 14), reused 2 (delta 0)
    Receiving objects: 100% (91976/91976), 49.29 MiB | 5.83 MiB/s, done.
    Resolving deltas: 100% (70684/70684), done.
    Checking connectivity... done.