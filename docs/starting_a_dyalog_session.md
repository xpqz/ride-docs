



# Starting a Dyalog Session

When running a Dyalog Session through the RIDE, that Session should only be accessed through the RIDE. One exception to this rule is when developing or running applications that are `⎕SM`/`⎕SR` based; access to the `⎕SM` window cannot be made through the RIDE.

When running a Dyalog Session through the RIDE, the Session can be:

- local to the machine on which the RIDE is running.
- remote from the machine on which the RIDE is running.
- The operating system on which the remote interpreter is running is irrelevant – the instructions given in this chapter apply to the operating system on which the RIDE is running (the two operating systems do not have to be the same).
- The remote machine does not need to have the RIDE installed but the Dyalog Session must be RIDE-enabled (see [Section ](ride_init.md#)).

Connections between the RIDE and Dyalog interpreters are initialised through the RIDE-Dyalog Session dialog box. The exception to this is Zero Footprint use, which always requires Dyalog to be started first with suitable configuration parameters, after which the RIDE will appear when you direct a web browser at the APL interpreter. See [Section ](the_zero_footprint_ride.md#) for more information on Zero Footprint mode.


This chapter describes how to use the RIDE to run Dyalog Sessions, both local and remote.


