# Unit 01: Shell Navigation

### **echo**

Prints back what the user types to the screen or presents a variable in plaintext.

## **Bash**

An Open Source replacement for the Bourne Shell (sh). It is the default shell on most Linux distributions currently and the one most likely to be encountered by users.

csh and tcsh are less common, and bash users tend to find their differences annoying. Google "Top Ten Reasons not to use the C shell" or "Csh Programming Considered Harmful" (a classic rant by Perl developer Tom Christiansen)

If you control your own system, and spend a lot of time working in (or scripting) the shell, there are other less-common shells that you might want to consider. In particular, zsh has a devoted following, and offers useful features that aren't available in bash.

## **Tab Completion**

Working with the command line can be daunting when used to a GUI (graphical user interface). By using tab completion, you can minimize the amount of text you have to type by pressing [TAB] to complete what you have already partially typed. On modern systems with advanced tab completion you can auto-complete remote filesystems, command syntax, and more.

### **history**

The history command is very useful to see what commands you have run in the past, and keeps by default the last 1000 lines entered at the prompt.

This can be a security hazard though, as sometimes people accidentally type their passwords on the command line, and if someone happens to shoulder-peek whilst you are browsing your history it could be compromised.

#### *Useful Flags:*

    -c    clears history
    -d    followed by a line number, clears the history from that line up only

### **man**

Shows the manuals for commands.

Man can be your best friend when you are unfamiliar with commands in UNIX. You can run man followed by any command and see a comprehensive manual of the command and all options you can run it with.

Sometimes manuals can be lengthy and the amount of information you need is not easily discernible, as such, short form help can be found often by trailing a command with `-?` or `--help`.

If you know what you want to do, but don't know the command, `man -k` (or `apropos`) will list all the man pages that include the string you enter. You can then use `man` to learn more details about the command(s) that you found.

#### **Hotkeys and Shortcuts:**

    CTRL+R            Dynamically search your command history
    CTRL+E            Move cursor to the end of the line
    CTRL+A            Move cursor to the beginning of the line
    CTRL+W            Delete previous word
    CTRL+C            Kill the current command
    CTRL+P            Recall the previous command from history
    ALT+. (period)    Insert the last parameter from the previous command
    CTRL+D            Exit/logoff
    Up/Down Arrows    Scroll through command history

### **~/.bashrc and ~/.bash_profile**

These files are scripts which are executed whenever you log in or open a new terminal. They are used to configure your environment, set the PATH variable, or run commands.
They are used somewhat differently on various systems, but for most uses the ~/.bashrc file should be used for adding functionality.

## **$PATH**

$PATH is a variable specified usually in the ~/.bashrc, that tells your session how to interact with the filesystem, usually where non-standard items are located, and in what order to process them. 

This is useful when a program is already installed on the system, but you would like to compile or run a newer or different version without modifying the program which is already installed. You can install that program in your home directory, then modify your PATH to include the path to the program you installed.

In this example, python 2.4.3 is installed in /usr/bin, and python 2.7.3 is installed in /usr/local/bin. By modifying the order that these directories appear in the PATH variable, a different version of the program will be called when simply executing its name:

    [user@compute01 ~]$ echo $PATH
    /usr/bin:/usr/local/bin:/home/user/bin
    [user@compute01 ~]$ which python
    /usr/bin/python
    [user@compute01 ~]$ python
    Python \*\*2.4.3 (#1, Jun 18 2012, 08:55:23)\*\*
    [GCC 4.1.2 20080704 (Red Hat 4.1.2-52)] on Linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

    [user@compute01 ~]$ echo $PATH
    /usr/local/bin:/usr/bin
    [user@compute01 ~]$ which python
    /usr/local/bin/python
    [user@compute01 ~]$ python
    Python \*\*2.7.3 (default, Aug 17 2012, 17:43:15)\*\*
    [GCC 4.1.2 20080704 (Red Hat 4.1.2-52)] on Linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>