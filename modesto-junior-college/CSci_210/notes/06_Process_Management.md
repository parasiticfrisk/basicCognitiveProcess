# Unit 06: Advanced Process Management

## **Checking Machine Resources**

Besides disk space, there are other resources on a server which you should be aware of when running applications, especially computationally intensive ones. Resources to consider include CPU, RAM (memory), and network bandwidth.

### **ps**

Ps (processes) is a program that lists running processes on the system.

#### *Useful Flags:*

    -e    show all processes, including those owned by others
    -u    sort by user
    -f    full format listing
    -x    show all processes
    -H    show a tree view of child/parent process hierarchy

`ps` can be used in conjunction with `grep` similar to the example provided above to locate a particular program or programs started by a user. 

### **free**

Free is a tool to see the amount of memory (RAM) and swap space available and in use on the system.

#### *Useful Flags:*

    -g    display numbers in gigabytes (most useful in today's machines)
    -m    display numbers in megabytes

Note that the way the Linux kernel allocates memory, free (and other utilities) may report that nearly all of your RAM is being used. This is not entirely true; Linux uses inactive memory to cache files very intelligently. However, if an application needs that memory, it will quickly release it from filesystem cache. For a more usable number, refer to the "-/+ buffers/cache" line to see how much RAM is available for applications, excluding the filesystem buffers.  (See [http://www.Linuxatemyram.com/](http://www.Linuxatemyram.com/) for a more detailed explanation.

### **top**

Top is an interactive program that provides a dynamic real-time view of a running system, including processes, CPU usage and the type of its use, memory, and swap consumption. It also allows you to interact with processes so that they can be killed or reniced (assuming the user has permission).

## **Managing Processes**

### **kill**

Just as it describes, kill is a command used for killing an active process abruptly. Often used by administrators for cleaning up rogue jobs, but regular users can also control their own jobs with this command as well. This command requires you to specify the PID of the process to be killed (this can be found with the ps command).

#### *Useful Flags:*

    -STOP    suspends the process exactly as it is
    -CONT    resume a previously STOP'd process
    -9       the most forceful method for killing a process

### **pkill**
    Similar to kill though it will allow you to search for processes based on specific terms such as user.

#### *Useful Flags:*

    -u -- user, pkill - u userid will kill all jobs by that user

### **killall**

Killall is aptly named - it kills all processes with the same name (not by PID). Most flags of the `kill` command work with killall as well.

## **Job Control**

UNIX systems have built-in support for running multiple processes at once from the same console through job control. Jobs can be launched in the background, then the user able to issue more commands while the background job runs. Backgrounded jobs will continue to output to your terminal.

Note that backgrounded jobs will NOT continue to run after disconnecting or logging out of the server. For this functionality, see `nohup` or  `screen` and `tmux`.  This method is fairly crude, and has substantial limitations. For more full-featured interactive process management, see screen.

#### *Useful Commands:*

    &           Runs  in the background
    CTRL+Z      Stops command and puts in background
    jobs        List processes under job control with associated job IDs
    fg          Bring to foreground and resume execution
    bg          Resume execution in background

#### Example:

    [user@compute ~]$ ./run.sh
    2012-10-01 12:15:32 INFO: Running iteration 1 of 5...
    2012-10-01 12:15:37 INFO: Running iteration 2 of 5...
    ^Z
    [1]+ Stopped         ./run.sh
    [user@compute ~]$ jobs
    [1]+ Stopped         ./run.sh
    [user@compute ~]$ fg 1
    ./run.sh
    2012-10-01 12:15:47 INFO: Running iteration 3 of 5...
    ^Z
    [1]+ Stopped         ./run.sh
    [user@compute ~]$ bg 1
    [1]+ ./run.sh &
    [user@compute ~]$ 2012-10-01 12:15:54 INFO: Running iteration 4 of 5...
    [user@compute ~]$ free -m
                total    used    free   shared  buffers   cached
    Mem:	32185   31032    1152        0      339    29315
    -/+ buffers/cache:   1377   30807
    Swap:	32765    779    31985
    [user@compute ~]$ 2012-10-01 12:15:59 INFO: Running iteration 5 of 5...
    2012-10-01 12:16:04 INFO: Done!
    [1]+ Done          ./run.sh
    [user@compute ~]$

In the above example, the program `run.sh` was executed normally, then stopped with `CTRL+Z`. The `jobs` command showed the job in a stopped state. `fg` command started the command executing again in the foreground, where it is once again stopped with `CTRL+Z`. `bg` is then used to resume execution in the background this time, which allows the user to run any other commands they like - in this case, `free -m` is used to check the memory usage. The `run.sh` script continues to run in the background, outputting text onto the console, until completing and exiting.

### **screen & tmux**

The best thing(s) since self-slicing bread!

Screen and tmux are "terminal multiplexers".  This allows you to connect and disconnect from long running processes and monitor the output. There are many good online "cheat sheets".