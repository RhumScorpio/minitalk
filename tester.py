import  subprocess
import  os
import  sys
import  time

line = "---------------------------------------------------------------------"
ENDL = "\n"
progName = "Minitalk 42 cursus tester"
startupMsg = line + ENDL + progName.center(len(line), ' ')  + ENDL + line
done = 0
usage = "py_talk: usage: [server_pid]"
Lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus aliquet sit amet justo eu auctor. Sed ut dolor eget est fermentum auctor vel vitae mauris. Sed eget odio lacus. Etiam ut velit luctus, vulputate turpis non, pharetra metus. Sed blandit dictum commodo. Fusce est ex, imperdiet ac efficitur id, faucibus ac elit. Sed laoreet tempus lorem, vitae placerat dui pellentesque eget. Nullam dapibus justo eget massa iaculis cursus. Vivamus suscipit at odio sit amet pulvinar. Integer eleifend vitae quam ut scelerisque. Pellentesque vestibulum, risus eget hendrerit sollicitudin, mauris sapien suscipit tortor, vitae dictum nulla purus nec urna. Morbi eleifend molestie tortor id tincidunt. Curabitur pellentesque tristique urna, ac ullamcorper est sollicitudin non. Maecenas a massa non orci gravida convallis eu non eros. Integer mattis aliquam nibh, ut imperdiet ipsum ultricies id.

Vivamus quis massa vel nunc auctor posuere a sit amet est. Nunc ut maximus felis. Proin quis neque vel nulla malesuada vulputate. Suspendisse dignissim mi urna, ut sodales purus rutrum a. Aliquam purus diam, eleifend non dolor sit amet, rhoncus gravida massa. Integer suscipit nisi a ex vulputate, sit amet bibendum nibh tempor. Nullam elementum augue sed sollicitudin dictum. Sed mattis ipsum in dui laoreet fringilla. Vivamus et enim eu ipsum accumsan eleifend dignissim ac urna.

Vivamus cursus velit justo, id ornare turpis tincidunt ac. Vivamus nibh justo, ultricies ut neque at, consequat pharetra lectus. Pellentesque efficitur nunc ac fermentum sagittis. Sed eget neque ligula. Maecenas consequat dui mauris, eu lacinia urna gravida ac. Pellentesque tincidunt, leo at elementum luctus, metus enim sagittis odio, luctus cursus metus felis vel risus. Curabitur in justo vitae odio blandit maximus. Mauris venenatis tincidunt dictum. Donec dui orci, egestas eu facilisis vel, eleifend nec nulla. Sed vel venenatis nisi.

Aliquam nunc elit, tincidunt ut est non, pharetra suscipit purus. Nullam vel nunc fermentum, rutrum metus dapibus, aliquam enim. In placerat nulla at rutrum lacinia. Suspendisse congue tempor tempor. Mauris quis ipsum vehicula, suscipit elit at, pretium enim. Pellentesque neque eros, iaculis ac libero nec, porttitor varius ante. Maecenas ullamcorper in sapien ac ornare. Sed convallis neque nibh, sed dictum arcu gravida id. Quisque in ligula vel neque sodales tincidunt. Mauris imperdiet odio eu ligula mattis gravida. Nulla facilisi. Maecenas non dolor orci. Vestibulum eu suscipit mauris.

Cras sodales auctor turpis, in eleifend augue maximus quis. Etiam nulla elit, placerat ut sollicitudin eget, vehicula nec nunc. Cras molestie sed magna non maximus. Suspendisse ultricies, diam nec accumsan hendrerit, arcu risus tincidunt massa, sit amet lobortis sem mi vel lorem. Suspendisse porta odio interdum rutrum dapibus. Nunc posuere porttitor neque, cursus fringilla diam eleifend lacinia. Duis ut enim rhoncus velit interdum finibus quis in purus."""
send = """The kill(2) system call sends a specified signal to a specified process, if permissions allow. Similarly, the kill(1) command allows a user to send signals to processes. The raise(3) library function sends the specified signal to the current process.

Exceptions such as division by zero or a segmentation violation will generate signals (here, SIGFPE "floating point exception" and SIGSEGV "segmentation violation" respectively, which both by default cause a core dump and a program exit).

The kernel can generate signals to notify processes of events. For example, SIGPIPE will be generated when a process writes to a pipe which has been closed by the reader; by default, this causes the process to terminate, which is convenient when constructing shell pipelines.

Typing certain key combinations at the controlling terminal of a running process causes the system to send it certain signals:[2]

Ctrl-C (in older Unixes, DEL) sends an INT signal ("interrupt", SIGINT); by default, this causes the process to terminate.
Ctrl-Z sends a TSTP signal ("terminal stop", SIGTSTP); by default, this causes the process to suspend execution.[3]
Ctrl-\ sends a QUIT signal (SIGQUIT); by default, this causes the process to terminate and dump core.
Ctrl-T (not supported on all UNIXes) sends an INFO signal (SIGINFO); by default, and if supported by the command, this causes the operating system to show information about the running command.[4]
These default key combinations with modern operating systems can be changed with the stty command.
"""
history = """Version 1 Unix had separate system calls to catch interrupts, quits, and machine traps. Version 4 combined all traps into one call, signal, and each numbered trap received a symbolic name in Version 7. kill appeared in Version 2, and in Version 5 could send arbitrary signals.[1] Plan 9 from Bell Labs replaced signals with notes, which permit sending short, arbitrary strings.[citation needed]"""
wiki = """Signals are standardized messages send to a running program to trigger specific behavior (such quitting or error handling). They are a limited form of inter-process communication (IPC), typically used in Unix, Unix-like, and other POSIX-compliant operating systems.

A signal is an asynchronous notification sent to a process or to a specific thread within the same process to notify it of an event. Common uses of signals are to interrupt, suspend, terminate or kill a process. Signals originated in 1970s Bell Labs Unix and were later specified in the POSIX standard.

When a signal is sent, the operating system interrupts the target process' normal flow of execution to deliver the signal. Execution can be interrupted during any non-atomic instruction. If the process has previously registered a signal handler, that routine is executed. Otherwise, the default signal handler is executed.

Embedded programs may find signals useful for inter-process communications, as signals are notable for their Algorithmic efficiency.

Signals are similar to interrupts, the difference being that interrupts are mediated by the CPU and handled by the kernel while signals are mediated by the kernel (possibly via system calls) and handled by individual processes. The kernel may pass an interrupt as a signal to the process that caused it (typical examples are SIGSEGV, SIGBUS, SIGILL and SIGFPE).""" + line + ENDL + "Sending signals".center(len(line)) + ENDL + line + ENDL + send
siglist = """The list below documents the signals specified in the Single Unix Specification. All signals are defined as macro constants in the <signal.h> header file.[which?] The name of the macro constant consists of a "SIG" prefix followed by a mnemonic name for the signal.

SIGABRT and SIGIOT
The SIGABRT and SIGIOT signal is sent to a process to tell it to abort, i.e. to terminate. The signal is usually initiated by the process itself when it calls abort() function of the C Standard Library, but it can be sent to the process from outside like any other signal.
SIGALRM, SIGVTALRM and SIGPROF
The SIGALRM, SIGVTALRM and SIGPROF signal is sent to a process when the time limit specified in a call to a preceding alarm setting function (such as setitimer) elapses. SIGALRM is sent when real or clock time elapses. SIGVTALRM is sent when CPU time used by the process elapses. SIGPROF is sent when CPU time used by the process and by the system on behalf of the process elapses.
SIGBUS
The SIGBUS signal is sent to a process when it causes a bus error. The conditions that lead to the signal being sent are, for example, incorrect memory access alignment or non-existent physical address.
SIGCHLD
The SIGCHLD signal is sent to a process when a child process terminates, is interrupted, or resumes after being interrupted. One common usage of the signal is to instruct the operating system to clean up the resources used by a child process after its termination without an explicit call to the wait system call.
SIGCONT
The SIGCONT signal instructs the operating system to continue (restart) a process previously paused by the SIGSTOP or SIGTSTP signal. One important use of this signal is in job control in the Unix shell.
SIGFPE
The SIGFPE signal is sent to a process when an exceptional (but not necessarily erroneous) condition has been detected in the floating point or integer arithmetic hardware. This may include division by zero, floating point underflow or overflow, integer overflow, an invalid operation or an inexact computation. Behaviour may differ depending on hardware.
SIGHUP
The SIGHUP signal is sent to a process when its controlling terminal is closed. It was originally designed to notify the process of a serial line drop (a hangup). In modern systems, this signal usually means that the controlling pseudo or virtual terminal has been closed.[9] Many daemons (who have no controlling terminal) interpret receipt of this signal as a request to reload their configuration files and flush/reopen their logfiles instead of exiting.[10] nohup is a command to make a command ignore the signal.
SIGILL
The SIGILL signal is sent to a process when it attempts to execute an illegal, malformed, unknown, or privileged instruction.
SIGINT
The SIGINT signal is sent to a process by its controlling terminal when a user wishes to interrupt the process. This is typically initiated by pressing Ctrl+C, but on some systems, the "delete" character or "break" key can be used.[11]
SIGKILL
The SIGKILL signal is sent to a process to cause it to terminate immediately (kill). In contrast to SIGTERM and SIGINT, this signal cannot be caught or ignored, and the receiving process cannot perform any clean-up upon receiving this signal. The following exceptions apply:
Zombie processes cannot be killed since they are already dead and waiting for their parent processes to reap them.
Processes that are in the blocked state will not die until they wake up again.
The init process is special: It does not get signals that it does not want to handle, and thus it can ignore SIGKILL.[12] An exception from this rule is while init is ptraced on Linux.[13][14]
An uninterruptibly sleeping process may not terminate (and free its resources) even when sent SIGKILL. This is one of the few cases in which a UNIX system may have to be rebooted to solve a temporary software problem.
SIGKILL is used as a last resort when terminating processes in most system shutdown procedures if it does not voluntarily exit in response to SIGTERM. To speed the computer shutdown procedure, Mac OS X 10.6, aka Snow Leopard, will send SIGKILL to applications that have marked themselves "clean" resulting in faster shutdown times with, presumably, no ill effects.[15] The command killall -9 has a similar, while dangerous effect, when executed e.g. in Linux; it doesn't let programs save unsaved data. It has other options, and with none, uses the safer SIGTERM signal.
SIGPIPE
The SIGPIPE signal is sent to a process when it attempts to write to a pipe without a process connected to the other end.
SIGPOLL
The SIGPOLL signal is sent when an event occurred on an explicitly watched file descriptor.[16] Using it effectively leads to making asynchronous I/O requests since the kernel will poll the descriptor in place of the caller. It provides an alternative to active polling.
SIGRTMIN to SIGRTMAX
The SIGRTMIN to SIGRTMAX signals are intended to be used for user-defined purposes. They are real-time signals.
SIGQUIT
The SIGQUIT signal is sent to a process by its controlling terminal when the user requests that the process quit and perform a core dump.
SIGSEGV
The SIGSEGV signal is sent to a process when it makes an invalid virtual memory reference, or segmentation fault, i.e. when it performs a segmentation violation.[17]
SIGSTOP
The SIGSTOP signal instructs the operating system to stop a process for later resumption.
SIGSYS
The SIGSYS signal is sent to a process when it passes a bad argument to a system call. In practice, this kind of signal is rarely encountered since applications rely on libraries (e.g. libc) to make the call for them. SIGSYS can be received by applications violating the Linux Seccomp security rules configured to restrict them. SIGSYS can also be used to emulate foreign system calls, e.g. emulate Windows system calls on Linux.[18]
SIGTERM
The SIGTERM signal is sent to a process to request its termination. Unlike the SIGKILL signal, it can be caught and interpreted or ignored by the process. This allows the process to perform nice termination releasing resources and saving state if appropriate. SIGINT is nearly identical to SIGTERM.
SIGTSTP
The SIGTSTP signal is sent to a process by its controlling terminal to request it to stop (terminal stop). It is commonly initiated by the user pressing Ctrl+Z. Unlike SIGSTOP, the process can register a signal handler for, or ignore, the signal.
SIGTTIN and SIGTTOU
The SIGTTIN and SIGTTOU signals are sent to a process when it attempts to read in or write out respectively from the tty while in the background. Typically, these signals are received only by processes under job control; daemons do not have controlling terminals and, therefore, should never receive these signals.
SIGTRAP
The SIGTRAP signal is sent to a process when an exception (or trap) occurs: a condition that a debugger has requested to be informed of – for example, when a particular function is executed, or when a particular variable changes value.
SIGURG
The SIGURG signal is sent to a process when a socket has urgent or out-of-band data available to read.
SIGUSR1 and SIGUSR2
The SIGUSR1 and SIGUSR2 signals are sent to a process to indicate user-defined conditions.
SIGXCPU
The SIGXCPU signal is sent to a process when it has used up the CPU for a duration that exceeds a certain predetermined user-settable value.[19] The arrival of a SIGXCPU signal provides the receiving process a chance to quickly save any intermediate results and to exit gracefully, before it is terminated by the operating system using the SIGKILL signal.
SIGXFSZ
The SIGXFSZ signal is sent to a process when it grows a file that exceeds the maximum allowed size.
SIGWINCH
The SIGWINCH signal is sent to a process when its controlling terminal changes its size (a window change).[20]"""
print(startupMsg)

def charInString(elem):
    for i in elem:
        i += 1
    return (i)
def ascii_test(server_pid):
    ascii_test = line + ENDL + "Printable ascii".center(len(line), ' ')  + ENDL + line
    i = 0
    subprocess.run(["./client", server_pid, ascii_test])
    while (i < 255):
        if (i >= 32 and i < 127):
            subprocess.run(["./client", server_pid, str(chr(i))])
            #execCmd("./client", server_pid + " " + chr(i))
        i += 1
def lorem_test(server_pid):
    test = line + ENDL + "Lorem ipsum".center(len(line), ' ')  + ENDL + line
    start_time = time.time()
    subprocess.run(["./client", server_pid, test])
    subprocess.run(["./client", server_pid, Lorem])
    print("Lorem ipsum: exec time: ")
    print(time.time() - start_time)
    print("for numbers of characters: " + str(len(Lorem) + len(test)) + ENDL)
    test = line + ENDL + "Signal wikipedia page".center(len(line), ' ')  + ENDL + line
    start_time = time.time()
    subprocess.run(["./client", server_pid, test])
    subprocess.run(["./client", server_pid, wiki])
    test = line + ENDL + "POSIX signals".center(len(line), ' ')  + ENDL + line
    subprocess.run(["./client", server_pid, test])
    subprocess.run(["./client", server_pid, siglist])
    print("Signal wikipedia page: exec time: ")
    print(time.time() - start_time)
    print("for numbers of characters: " + str(len(wiki) + len(test) + len(siglist)) + ENDL)
def main():
    if (len(sys.argv) != 2):
        print(usage)
        sys.exit(0)
    serverPid = sys.argv[1]
    ascii_test(serverPid)
    lorem_test(serverPid)
if __name__ == "main":
    main()
else:
    main()
