# Unit 02: Basic File System Functionality
 
### **pwd**

Print name of current Working Directory.

#### Example:

    [user@compute ~]$ pwd
    /home/user

### **cd**

Change Directory. Changes the current working directory.

#### Example:

    [user@compute ~]$ cd /nfs/labs
    [user@compute labs]$

## **Relative Paths and Absolute Paths**

A relative path is a path which is relative to your current working directory (does not begin with a leading slash). Relative paths sometimes start with a single dot or a double dot, indicating the current directory or the parent directory.

     ./    (Current directory)
    ../    (One directory up)

#### Example:

    [user@compute chilab1]$ pwd
    /nfs/labs/chilab
    [user@compute chilab]$ cd ../ohlerlab
    [user@compute ohlerlab]$ pwd
    /nfs/labs/ohlerlab

### **Application Paths**

When typing a command, the shell searches directories in the path (a list of directories) in order for commands matching the name you typed. The first one found gets executed.

All users have a default path that the system knows to look in when searching for executables. If you would like to find out what your current paths are set to you can always echo back the $PATH system variable.

#### Example:

    [user@compute ~]$ echo $PATH
    /usr/sbin:/bin:/usr/kerberos/bin:/usr/local/bin:/usr/bin

### **which**

Which is a command used to locate executables.

If there are multiple executables with the same name in different directories in your path, which can be used to identify which one will be executed when you type the command.

#### Example:

    [user@compute ~]$ which matlab
    /usr/local/bin/matlab

### **Executing**

In a UNIX environment, you execute a program by typing out the full path to it. In order to run matlab, you can type `/usr/local/bin/matlab`; or if your current working directory is the directory `/usr/local/bin`, you can use a relative path and type `./matlab`; or if it is in one of your application paths ($PATH) above, you simply have to type `matlab`.

### **ls**

Displays a listing of files and directories.

#### *Useful Flags:*

    -l    Long directory listing with details like size, ownership, and permissions
    -h    Print human-readable sizes (only affects long listings)
    -a    Show all items, even hidden ones (whose names begin with a period)
    -d    If the target is a directory, list the directory instead of its contents.

#### Examples:

    [user@compute labs]$ ls
    barda    dietrichlab  itlab        nevinslung  tianlab

    [user@compute ~]$ ls -l /nfs/labs/
    total 132
    drwxrws--- 17 root barda     4096 Jun 29 12:27 barda
    lrwxrwxrwx 1 root root       31 Jan 16 2012 benfeylab -> /nfs/dept/benfey_sas/benfeylab/

    [user@compute labs]$ ls -l -h -d barda/
    drwxrws--- 17 root barda 4.0K Jun 29 12:27 barda

## **File Permissions**
 
Permissions are displayed as 10 fields in the leftmost column on a long directory listing, and describe who can read, write, and execute the file or directory. They are divided into sections:

    | Info | User | Group | Other |
    | ---- | ---- | ----- | ----- |

These spaces will usually be populated with the characters "r" (read), "w" (write), and "x" (execute) and determine what a user is able to do with the file or folder. The info field denotes the "type" of file (insofar as Unix is concerned); it will contain a "-" for a "regular" file, a letter "d" if the entry is a directory, or other letters for "special" file types. 

#### Example: Running our `ls -l` command above we see the following for this folder.

    [user@compute ~]$ ls -l
    total 8
    drwxr-xr-x 2 steve visitors 4096 Apr 25 12:20 expt
    drwxr-xr-x 3 steve visitors 4096 Apr 17 21:04 R

In this example, there are two directories listed. They are directories as indicated by the "d" in the info field. The user (steve) has full permissions (read/write/execute), and the group (visitors) can read and execute (but not write), and everyone else can also read and execute (but not write).

For a file, execute permission means that it can be executed as a program or script. For a directory, execute permission (along with read permission) means that the contents of the directory can be read and listed.

### **mkdir**

Creates a new empty directory.

### **touch**

Performs a write operation to a file without writing any actual data. Creates a file if it does not exist, or updates the modified timestamp on a file that already exists.

Useful for creating a blank file or updating a timestamp.

#### Example:

    [user@compute ~]$ ls foo
    ls: foo: No such file or directory
    [user@compute ~]$ touch foo
    [user@compute ~]$ ls -l foo
    -rw-r--r-- 1 user staff 0 Jul 31 12:22 foo

### **cp**

Copy a file or directory.

#### *Useful Flags:*

    -v                     Prints a line for every file copied
    -R, -r, --recursive    Recursively copy directories and all of their content.
                           Use care with this one.

#### Example:

    [user@compute ~]$ cp -v foo bar
    'foo' -> 'bar'

    [user@compute ~]$ ls -l foo bar
    -rw-r--r-- 1 user staff 0 Jul 31 12:23 bar
    -rw-r--r-- 1 user staff 0 Jul 31 12:23 foo

### **mv**

Moves or renames a file (which is actually the same operation in UNIX).

#### *Useful Flags:*

    -v                   Verbose. Prints a line for every file moved
    -i, --interactive    Prompt before overwriting

#### Example:

     [user@compute ~]$ mv -v foo foo_moved
     `foo' -> `foo_moved'
     [user@compute ~]$ ls -l foo foo_moved
     ls: foo: No such file or directory
     -rw-r--r-- 1 user staff 0 Jul 31 12:23 foo_moved

### **rm**

Removes (deletes) a file

#### *Useful Flags:*

    -r, -R, --recursive    Recursively remove directories and their contents
                           USE EXTREME CARE
    -i, --interactive      Prompt before overwriting
    -f, --force            Without notice plow through, very dangerous
    -v, --verbose          Prints a line for every file removed/deleted.

### **rmdir**

Removes an empty directory

Sometimes a directory will seem empty but will actually include hidden files. If rmdir fails, you may need take a closer look at the apparently-empty directory with `ls -al`.

### **w**
 
Show who is logged on (and what command they are running), system uptime, and load average. Optionally provide a username to view only their sessions.

#### Example:

    [user@compute ~]$ w user
    13:34:49 up 76 days, 25 min, 26 users, load average: 0.04, 0.01, 0.00
    USER   TTY   FROM       LOGIN@  IDLE  JCPU  PCPU WHAT
    user   pts/8           12:15  0.00s 0.03s 0.00s w user

### **id**

Prints information for yourself or another user. It will give you the user's unique ID number, and all the groups that the user is a member of along with their associated group ID numbers. This can help you identify permissions for file and directory access.

#### Example:

    [user@compute ~]$ id
    uid=5555(user) gid=1000(professors)
    [user@compute ~]$ id joe
    uid=1234(joe) gid=1000(professors) groups=1000(professors),1056(dept),\
        1029(willardlab),1088(genomic-handbook)

### **whoami**

A similar tool is whoami, which simply displays your own username. Example:

    [user@compute ~]$ whoami
    user

### **getent**

*Get* *ent*ries from a system database, such as /etc/passwd (list of users), /etc/group (list of groups), and other system files. Most commonly, this is used to find group membership. If you want to see which users are members of a specific group, then you can use getent to get entries in the group database.

#### Example:

    [user@compute ~]$ getent group chilab
    chilab:\*:1041:gml7,cs80,jwu7,jdoss,xt2,mmk24,les36,jb279,mjv10,mh180,\
    cl215,sl238,chi00002,ljo6,avc2,jel2,mh309,cl26,cl262

### **chmod**

Change mode, is a command used to modify permissions on a file. If you would like to share your files with another user in your group, you can modify the permissions to grant read, write, or execute the file.

#### *Useful Flags:*
    
    u (User)
    g (Group)
    o (Other)
    + (Add Permission)
    - (Remove Permission)
    r (read)
    w (write)
    x (execute)

#### Example:

    [user@compute ~]$ ls -l largefile.10g
    -rwx------. 1 user research 10737418240 Jul 2 08:46 largefile.10g

The user above has the file largefile.10g that he would like to share with other people in the group "research" so that they can read and write to the file. This is where chmod comes in:

    [user@compute ~]$ chmod g+rw largefile.10g
    [user@compute ~]$ ls -l largefile.10g
    -rwxrw----. 1 user research 10737418240 Jul 2 08:46 largefile.10g

The g+rw means that for the *g*roup, add ( + ) *r*ead and *w*rite permission. This results in the file having read, write, and execute permissions for the user, and read and write for the group.

### **chown**

Change Owner, is a command used to modify the owner of a file. This usually can only be performed on a system where you have administrative rights and can switch files from one user to another.

#### Example:

	[user@compute ~]$ chown user2 largefile.10g
	[user@compute ~]$ ls -l largefile.10g
	-rw-r--r-- 1 user2 staff 10737418240 Sep 6 11:38 largefile.10g

### **chgrp**

Change Group, is a command used to modify the group that can read a file. You can only switch group ownerships on a file that you are the owner of.

#### Example:

    [user@compute ~]$ chgrp group2 largefile.10g
    [user@compute ~]$ ls -l largefile.10g
    -rw-r--r-- 1 user group2 10737418240 Sep 6 11:38 largefile.10g

### **Octal Permissions**

Another way to modify permissions that you will often see is to use octal numbers to do so. Each value r, w, x is equivalent to a number which, when all permissions are set, add up to 7 (full permission).

    4 = read
    2 = write
    1 = execute

#### Example:

If we wanted to grant read and write permissions to the research group like we did with our example above, we could also do the following:

    [user@compute ~]$ chmod 760 largefile.10g
    [user@compute ~]$ ls -l largefile.10g
    -rwxrw---- . 1 user research 10737418240 Jul 2 08:46 largefile.10g

The 760 tells us that the user field should have an octal count of 7, (read+write+execute), the group field should have a count of 6, (read+write) and the other field should have a count of 0.