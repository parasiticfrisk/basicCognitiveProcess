# Unit 03: Interactions With Data and Disk Storage

### **Mount Point**

A mount point is a directory or location in the local filesystem that you can use to mount either a remote directory or local device to access the files available there.

### **NFS**

NFS (Network File System)  is a protocol which allows remote file storage to be available (mounted) on another machine. Many Linux servers use NFS for home directories and many of their storage options.

### **Disk Usage & Quotas**

Knowing how much total space is available, how much is used, and how much is free is critical to working with data. For network storage, you probably have a quota assigned as well, which limits the amount of space an individual user can use on the storage volume. 

### **df**

DF (Disk File System Info) is used to see the entire size of a local volume or disk, and what is available. However, the 'available' numbers are simply the space free on the volume, and do not reflect limits imposed by user quotas.

So a user could see `df` report that there are many GB free, while at the same time they don't have space to save a 2 MB file.

#### *Useful Flags:*

    -h           human-readable (converts byte values to MB, GB, etc.)
    -T           lists the type of filesystem

### **du**

DU (Disk Usage) is used to count out the size of a particular directory, if you know the quota or volume size this will tell you what particular files or folders are using up specifically.

#### *Useful Flags:*

      -h     human readable - converts sizes to GB
      -s     summary - only shows top folder size.

## **Reading files**

There are a variety of ways to view and edit files within the terminal on Linux systems.

### **cat**

Short for "con*cat*enate", cat was originally intended to combine two files into one long file to browse; however, many people use it for a simple output of the contents of a file. It's useful in a graphical terminal because once a file or files are "catted" out, you can browse up and down them with your mouse.

### **less & more**

These programs are intended for the reading of longer files. More will display the contents of a file, and at what place you are in the file via percentage, near the bottom, and allow you to move only downward through the file one page at a time with the space bar. `Less` on the other hand offers much more than `more`: it allows for searching with `/`, navigation up *and* down with the arrow keys, and other handy features.

### **head & tail**

Head and tail are quick file readers, displaying respectively the top (head) or bottom (tail) sections of a file. By default it shows 10 lines, but the `-n` switch can set the number of lines to be shown.

#### Examples:

    [user@compute ~]$ tail /usr/share/dict/words
    Zythia
    zythum
    Zyzomys
    Zyzzogeton
    zyzzyva
    zyzzyvas
    ZZ
    Zz
    zZt
    ZZZ
    [user@compute ~]$ head -n15 /usr/share/dict/words
    1080
    10-point
    10th
    11-point
    12-point
    16-point
    18-point
    1st
    2
    20-point
    2,4,5-t
    2,4-d
    2D
    2nd
    30-30
    [user@compute ~]$ tail -n2 /usr/share/dict/words
    zZt
    ZZZ

## **Text Editors**

Most configuration files, scripts, and system files are plain text and will need to be edited. There are a variety of text editors available on UNIX, which one you use is largely up to individual preference. To open a file, simply type run your editor of choice followed by the file (or files) you'd like to edit.

### **nano / pico**

Nano and pico are nearly identical text editors developed for the Pine email client, and are a great editing tool for those new to UNIX. Since they were supposed to be a simple tool for email users, they have a low learning curve, and include a command reference at the bottom of the window for new users.

#### *Useful Keys:*

    CTRL+O    save
    CTRL+W    search
    CTRL+V    page down
    CTRL+Y    page up
    CTRL+X    exit

### **vi / vim**

The default editor on most UNIX/Linux systems, and the editor of choice of many system administrators and programmers, including some of the instructors of this course.

It is very powerful and has many shortcuts and built in functions to make file editing more efficient. Vim is so complex that many classes and books have been designed for the sole purpose of teaching its advanced functions.

While it does have a high initial learning curve, a little time spent up front to get past the initial learning curve can be worthwhile, as its basic functions can be useful even to the more casual user.

### **emacs**

Emacs is an advanced text editor, but that's not why its partisans love it.

It contains a fully-executable programming shell, and you can make it do almost anything.

The tradeoff for that power is that its learning curve makes vim look like pico.

### **Opening and Saving**

In order to open most files in a UNIX system, you just type the name of the editor you wish to use, and then follow with the filename.  To save, most of the editors have a write out function as defined in the Useful Keys section above.

## **Comparing Files**

### **cmp**

This is a program that will tell you whether two files are different, and tell you the location of the first difference.

### **diff**

This is a program that will point out lines that are different if you have two files, or copies of the same file and want to see what the differences are.

#### *Useful Flags:*

    -y    Displays contents side by size and points out differences.
    -u    Displays "unified" differences (differences surrounded by context, and
          denoted by a "+" or "-" at the start of the line).
    -q    Only displays that they are differently quickly.
    -b    Ignore extra lines or whitespace.

## **Command Output Redirection**

Redirection can be used to take the output of a command and write it into to a file instead of standard output (the terminal). There are two types of file redirection, one for overwrite and one for append.

`>`: A single arrow is used to create a file, or overwrite the contents of an existing file if necessary. Good for sanity checks. Many people will have a program that writes out a new file with a specific output and check back against it.

`>>`: A double arrow is used to append to an existing file. Very useful for logs or continuing records, where you just want to add lines to the end

In this example, we use the `df` command to show the disk usage for the user's home directory, and save the output into a file called my_quota.txt:

    [user@compute ~]$ df -h ~ > my_quota.txt
    [user@compute ~]$ cat my_quota.txt
    Filesystem      Size Used Avail Use% Mounted on
    san01a.dept.duke.edu:/vol/central_sata/data
    4.7T 2.7T 2.0T 58% /nfs/central

### **File Extensions?**

Unlike Windows, where every file has an extension identifying its type, most files in a UNIX filesystem do not, and are just defined by their permissions, all files can be opened with one of the text editors above, but many cannot be read or edited this way, a compiled binary file will appear as gibberish to most people.

## **File Compression**

### **Tar**

Tar is main UNIX archive utility that will allow you to store many files and directories into a single file, while optionally compressing them in the process. Compression methods include gz (GZip), bz2 (BZip2), or xz.

Using compression can drastically shrink the file size, which is useful when archiving or transferring data across the Internet. Many applications (and source code) are distributed inside these archives.

#### *Useful Flags:* 

    -c    (create) create a new archive
    -x    (extract) extract or expand an archive file
    -j    (bz2 format) if compressed
    -J    (xz format) if compressed
    -z    (gzip format) if compressed
    -v    (verbose) will list files in and out of archive
    -f    (file name) the file you want to open, or save to
    -C    (directory name) change to directory DIR

#### Example:

A user has a directory full of files which can be cumbersome to send over email as individual files. Using tar and bz2 compression, the directory can be compressed into a single file that can then be easily emailed:

    [user@compute ~]$ du -hs CS210/
    24M CS210/
    [user@compute ~]$ tar -cjvf CS210.tar.bz2 CS210/
    CS210/
    CS210/intro/
    CS210/intro/file\_layout.html
    CS210/intro/index.html
    CS210/intro/dilbert-UNIX.png
    CS210/intro/style.css
    CS210/intro/agenda.html
    CS210/intro/parts.html
    CS210/intro/parts.png
    ...
    ..
    .
    [user@compute ~]$ du -hs CS210.tar.bz2
    5M CS210.tar.bz2

### **Zip** 

Zip is also available are the commands zip and unzip which are used for manipulating zip files, the common compression/archiving format on Windows and other platforms.

#### *Useful Flags:* 

    -r    recursive: grab all files in the folder you want to zip
    -9    maximum compression: compress as small as possible, at the cost of more time

#### Example:

Same as above but with zip. (Note, it shows you compression numbers per file. Neat.)

    [user@compute ~]$ du -hs CS210/
    24M CS210/
    [user@compute ~]$ zip -r9 CS210.zip CS210
    adding: CS210/ (stored 0%)
    adding: CS210/intro/ (stored 0%)
    adding: CS210/intro/file\_layout.html (deflated 36%)
    adding: CS210/intro/index.html (deflated 48%)
    adding: CS210/intro/dilbert-UNIX.png (stored 0%)
    adding: CS210/intro/style.css (deflated 50%)
    adding: CS210/intro/agenda.html (deflated 56%)
    adding: CS210/intro/parts.html (deflated 36%)
    adding: CS210/intro/parts.png (deflated 1%)
    adding: CS210/intro/multitask2.html (deflated 40%)
    adding: CS210/intro/file\_layout\_2.html (deflated 36%)
    ...
    ..
    .
    [user@compute ~]$ du -hs CS210.zip
    5M CS210.zip