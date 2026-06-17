This project is a system administration related exercise to build an own server.

Skills: Network, Administration, Unix, Virtualization

Tools: VirtualBox (or UTM if can't use VirtualBox)cd


General guidelines
• The use of VirtualBox (or UTM if you can’t use VirtualBox) is mandatory.
• You only have to turn in a signature.txt file at the root of your repository. You must
paste the signature of your machine’s virtual disk in it. See the “Submission and peer-
evaluation” section for more information.
• No snapshots may exist at the beginning of each evaluation.

Rules:
1. must choose an operating system: Debian or Rocky
Q: what are those two system, what are other operating system, how to set up them?

Setting up Rocky is quite complex. Therefore, you do not have to set up
KDump. However, SELinux must be running at startup and its configuration
has to be adapted for the project’s needs. AppArmor for Debian must be
running at startup too.
Q: What are those terms? what's the process to set up an operating system? the differences between
aptitude and apt, or what SELinux or AppArmor is.

2. You must create at least 2 encrypted partitions using LVM.
Below is an example of a possible partitioning: ( a picture can't see)
Q: what is LVM? what does an example looks like and the meaning of each term?

3. A SSH service must be running on port 4242 in your virtual machine. For security reasons,
it must not be possible to connect using SSH as root.

Q: what is ssh service, how it works? why can't connect using ssh as root? if do so, what's the possible risk?

4. You have to configure your operating system with the UFW firewall (or firewalld for Rocky)
firewall and leave only port 4242 open in your virtual machine.
The example shows arbitrary disk sizes. You need to determine the appropriate size for each partition to ensure proper operation while avoiding unnecessary disk usage.
Your firewall must be active when you launch your virtual machine. For Rocky, you have to use firewalld instead of UFW.

5. The hostname of your virtual machine must be your login ending with 42 (e.g., wil42).
You will have to modify this hostname during your review.

6. you have to implement a strong password policy.
• You have to install and configure sudo following strict rules.
• In addition to the root user, a user with your login as the username has to be present.
• This user has to belong to the user42 and sudo groups.
During the defense, you will have to create a new user and assign it to a group.

To set up a strong password policy, you have to comply with the following requirements:
• Your password has to expire every 30 days.
• The minimum number of days between password changes must be set to 2.
• The user has to receive a warning message 7 days before their password expires.
• Your password must be at least 10 characters long. It must contain an uppercase letter, a lowercase letter, and a number. Also, it must not contain more than 3 consecutive identical characters.
• The password must not include the name of the user.
• The following rule does not apply to the root password: the password must contain at
least 7 characters that were not part of the previous password.
• Of course, your root password has to comply with this policy.
After setting up your configuration files, you will have to change all the passwords of the accounts present on the virtual machine, including the root account.

To set up a strong configuration for your sudo group, you have to comply with the following requirements:
• Authentication using sudo has to be limited to 3 attempts in the event of an incorrect password.
• A custom message of your choice has to be displayed if an error due to a wrong password occurs when using sudo.
• Each action performed with sudo has to be logged, including both inputs and outputs.

The log file has to be saved in the /var/log/sudo/ folder.
• The TTY mode has to be enabled for security reasons.
• For security reasons, the paths that can be used by sudo must also be restricted. Example:
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

7. Finally, you have to create a simple script called monitoring.sh. It must be written in bash.
At server startup, the script will display the information listed below on all terminals, and
every 10 minutes (you can take a look at wall but other options exist). The banner is optional.
No errors should be displayed.
Your script must always be able to display the following information:
• The architecture of your operating system and its kernel version.
• The number of physical processors.
• The number of virtual processors.
• The currently available RAM on your server and its utilization rate as a percentage.
• The currently available storage on your server and its utilization rate as a percentage.
• The current CPU utilization rate as a percentage.
• The date and time of the last reboot.
• Whether LVM is active or not.
• The number of active connections.
• The number of users using the server.
• The IPv4 address of your server and its MAC (Media Access Control) address.
• The number of commands executed with the sudo program.
During the defense, you will be asked to explain how this script works. You will also have to interrupt it without modifying it. Take a look at cron.


A README.md file must be provided at the root of your Git repository. Its purpose is to allow
anyone unfamiliar with the activity (peers, staff, recruiters, etc.) to quickly understand what
the activity is about, how to run it, and where to find more information on the topic.
The README.md must include at least:
• The very first line must be italicized and read: This activity has been created as part of
the 42 curriculum by <login1>[, <login2>[, <login3>[...]]].
• A "Description" section that clearly presents the activity, including its goal and a brief
overview.
• An "Instructions" section containing any relevant information about compilation, instal-
lation, and/or execution.
• A "Resources" section listing classic references related to the topic (documentation,
articles, tutorials, etc.), as well as a description of how AI was used — specifying for
which tasks and which parts of the activity.
➠ Additional sections may be required depending on the activity (e.g., usage examples,
feature list, technical choices, etc.).
Any required additions will be explicitly listed below.
• A Project description section must also explain your choice of operating system (Debian
or Rocky), including their respective advantages and disadvantages. It must describe the
main design choices made during the setup (partitioning, security policies, user manage-
ment, services installed) and provide a comparison between:
◦ Debian vs Rocky Linux
◦ AppArmor vs SELinux
◦ UFW vs firewalld
◦ VirtualBox vs UTM

You only need to submit the expected README.md file, and a signature.txt file at the root
of your Git repository. You must paste the signature of your machine’s virtual disk into this
file. To get this signature, you first have to open the default installation folder (it is the folder
where your VMs are saved):
• Windows: %HOMEDRIVE%%HOMEPATH%\VirtualBox VMs\
• Linux: ~/VirtualBox VMs/
• MacM1: ~/Library/Containers/com.utmapp.UTM/Data/Documents/
• MacOS: ~/VirtualBox VMs/
Then, retrieve the signature from the ".vdi" file (or ".qcow2 for UTM’users) of your virtual
machine in sha1 format. Below are four command examples for a rocky_serv.vdi file:
• Windows: certUtil -hashfile rocky_serv.vdi sha1
• Linux: sha1sum rocky_serv.vdi
• For Mac M1: shasum rocky.utm/Images/disk-0.qcow2
• MacOS: shasum rocky_serv.vdi
This is an example of the output you will get:
• 6e657c4619944be17df3c31faa030c25e43e40af
Please note that your virtual machine’s signature will be altered as soon as
you start the virtual machine again. To allow signature verification for all
your evaluations, you can either duplicate the virtual machine disk file, or use
a snapshots for each evaluation.
It is, of course, FORBIDDEN to include your virtual machine in your Git repos-
itory. During the review, the signature of the signature.txt file will be
compared with the one of your virtual machine. If the two of them are not
identical, your grade will be 0.
The use of snapshots is restricted. Each defense must start without any
snapshots. A snapshot dedicated to the defense will then be created and
deleted at the end of the defense. You are encouraged to make tests with
the snapshot features before submitting your project.
