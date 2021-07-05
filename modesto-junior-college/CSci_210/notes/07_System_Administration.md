# Unit 07 : Simple system administration

## **Admin access**

Making changes to the operating system components affects all users. As such, it requires administrator rights on the Linux system. On your class virtual machines you have admin access via the sudo command. On real production systems you will probably not have admin access and will need to request changes.

### **apt & yum - installing software**

Linux software is mostly provided by a distribution. Software is arranged into packages and groups of packages. This is kind-a like an "app store", but everything is free and kept up to date by the distribution.

#### Examples: 

On Red Hat Linux /CentOS distributions, use yum:

    yum install scipy

On Ubuntu / Debian distributions, use apt:

    apt-get install python-numpy

## **Building an application from source.**

The best practice is to use software provided by the Linux distribution. However, sometimes specialized research software isn't packaged in a common distribution like Ubuntu. Also, you may need a new or experimental version of an application or you may need to modify the source code. In such cases, users may need to compile these programs from their source code and install the binary application in their home directory to be used.  Your Linux system must have a C compiler and basic software build tools. 

To install these execute:

    sudo apt-get install build-essential

Typically, compiling from source code involves the following basic steps:

1. Download and extract the source code
2. Run the configure script: `./configure`
3. Compile the program: `make`
4. Install the program: `make install`

### **Configure**

The configure script will typically define variables such as where to find dependencies and where to install the resulting executable and library files. It will usually produce a text file called a Makefile, that you can use to build the application.

#### *Useful Flags:*

    --prefix    choose where to save the output files when you make

### **Make**

Make is the UNIX command to take the information from the make file and using the resident compiler (usually gcc) build the application from the source libraries provided in the package. 

#### *Useful Arguments:*

    test       check that the program compile correctly
    clean      clean up any leftovers from an earlier failed build
    install    install the binaries and libraries in the appropriate locations,
               based on the `configure --prefix` option