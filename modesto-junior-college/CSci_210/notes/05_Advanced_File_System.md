# Unit 05: Advanced File System Management

### **Hardlink**

A link (ln) or hard link is basically a reference to an inode address and a block of data on the disk. Most files will only ever have one, but there are instances when multiple can be useful. Every hard link that points to the same file can be read and written to, and modifies the same underlying data inside the file. The exception to this are permissions; each hard link can have distinct, separate permissions.

Hard links do not take up additional space in the filesystem, since they all point to the same data. This is contrary to making a copy of a file, which will take up twice the amount of space on the filesystem.  A file remains as long as there are at least one hard link pointing to it. Once the last hard link is deleted, the file is officially deleted and the space it previously consumed is freed.

### **Symlink**

A symbolic link (ln -s) also referred to as a soft link, is similar to a shortcut in Windows. It points to the original location of a file, but if the destination file is moved or deleted, the link will be broken. A symlink can be deleted with no affect to the original file. Editing the data within the file from either the symlink or the file itself, will modify the original file.

### **find**

Find is a program that searches through one or more directories of a filesystem and reports files matching the specified criteria. Criteria could be file name, date, owner, permission, type, etc.

#### Example:

    [user@compute ~]$ find ~ -name large\*
    /home/user/largefile.10g

### **locate**

Locate is similar to find, except it searches a precompiled database index of all files on the system instead of actually looking at the filesystem itself. This makes locate much faster than find; in most cases, it is instantaneous.  Typically, the locate database is updated once per day by an automated task set by the system administrator. Because of this, the results from locate can be out of date if there have been changes made to the file(s) since the database was updated. Use find for the most up-to date information.

### **Pipes**

A pipe (|) is a method by which output from one command is used as the input for another command. This enables powerful processing of text, or streaming data from one program to another.

### **grep**

Utility for searching text for lines matching basic text or regular expressions.
grep can be most useful in its simplest form when piping a command to grep and searching for a string of text. 

#### Example:

    [user@compute ~]$ df -h | grep scratch
    /dev/sda7       44G  11G  32G 25% /scratch

Piping the output of `df` to `grep` with the expression 'scratch' will show any lines containing that string, in this case the /scratch mountpoint. This simple use can be applicable in many cases. Try some on your own.

#### *Useful flags:*

    -v               invert match (show lines which do **not** match the expression)
    -An, -Bn, -Cn    show the surrounding n line(s) around the text that matches
                     ...choices are Above, Below, or Context (above & below)
    -i               ignore case (case insensitive search)

#### **A note from Doug McIlroy, inventor of the Unix pipe**

"This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface."

### **Regex**

Regex, or Regular Expressions, are a concise and flexible means to "match" for strings of text, such as particular characters, words, or patterns of characters. It can really help when searching logs and databases for entries or like entries.  Because of their complexity, we will only touch on regular expressions by their use in other programs. See the links in External Resources section for more info.

### **sed**

Sed (Stream Editor), a utility that parses text and can apply transformations to that text as defined by regular expressions. It reads input from a pipe or from a file and applies a regular expression to each line and outputs them to stdout.

#### Example:

    [user@compute ~]$ cat my_quota.txt
    Filesystem      Size Used Avail Use% Mounted on
    san01a.dept.duke.edu :/vol/central_sata/data
    4.7T 2.7T 2.0T 58% /nfs/central
    [user@compute ~]$ sed 's/san01a/newserver/' my_quota.txt
    Filesystem      Size Used Avail Use% Mounted on
    newserver .dept.duke.edu:/vol/central_sata/data
    4.7T 2.7T 2.0T 58% /nfs/central

### **awk**

Awk is a tool used as a data extraction and reporting tool, often taking in values from stdout and separating lines into different fields via a specified separator and allowing you to report back a specific field.

#### Example: 

You can list all group members with getent, but it gives me other info as well, if you just want the members, you can use awk to parse out that info, using the colon as the separator, and listing field 4.

    [user@compute ~]$ getent group chilab
    chilab:\*:1041:gml7,jwu7,jdoss,xt2,mmk24,cl215,chi00002,ljo6,jel2,mh309,cl26,cl262,avc2
    [user@compute ~]$ getent group chilab | awk -F: '{print $4}'
    gml7,jwu7,jdoss,xt2,mmk24,cl215,chi00002,ljo6,jel2,mh309,cl26,cl262,avc2

### **Checksums**

A checksum (or hash sum) is a small snippet of text computed from an arbitrary block of data for the purpose of detecting accidental errors that may have been introduced during its transmission or storage. The integrity of the data can be checked at any later time by recomputing the checksum and comparing it with the stored one. If the checksums match, the data was almost certainly not altered.  Some popular hash algorithms include: MD5, cksum, SHA-1, SHA-256.

MD5 is commonly used as it gives a good balance of performance (little time taken to generate a hash on large data) and collision resistance (likelihood that two different files will calculate to the same hash value). 

#### Example:

    [user@localhost ~]$ md5sum foo.txt
    37c4b87edffc5d198ff5a185cee7ee09 foo.txt
    [user@localhost ~]$ mv -v foo.txt foo2.txt
    `foo.txt' -> `foo2.txt'
    [user@localhost ~]$ md5sum foo2.txt
    37c4b87edffc5d198ff5a185cee7ee09 foo2.txt

Notice, after moving the file, the hash sum is the same, because the contents are identical and the file integrity is intact. Now instead if we edit the contents just by adding one character, we get a drastically different checksum value:

    [user@localhost ~]$ md5sum foo.txt
    37c4b87edffc5d198ff5a185cee7ee09 foo.txt
    [user@localhost ~]$ vi foo.txt
    [user@localhost ~]$ cat foo.txt
    x The quick brown fox jumps over the lazy dog
    [user@localhost ~]$ md5sum foo.txt
    1dcf0a9446176bee28ee29464400da86 foo.txt

Just adding a single character to the beginning of the file causes the checksum to be drastically different, thus indicating a modification to the contents of file.