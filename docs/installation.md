# Installation

This chapter describes how to install the RIDE.

## Pre-requisites

RIDE  can only connect to a Dyalog interpreter that is version 15.0 or later.

The RIDE is supported on the following operating systems:

- Linux x86_64 – the following distributions: 
    - Debian 8 onwards
    - Fedora 25 onwards
    - Ubuntu 14.04 onwards

    distributions built on top of these should also work

    (Linux distribution must also have libnss version 3.26 onwards)
- macOS – Yosemite onwards
- Microsoft Windows – Windows 7 onwards

For the zero-footprint RIDE:

- a compatible browser must be installed.
- the operating system must be supported by the underlying technology [Electron](https://github.com/electron/electron/blob/v13.4.0/docs/tutorial/support.md).

If Dyalog is not installed on the machine that the RIDE is being installed on, then the APL385 font and keyboard mappings installed with the RIDE mean that they are available when running a Dyalog Session through the RIDE. However, to be able to enter APL glyphs outside a Dyalog Session (for example, in text files or emails) you will need to download and install the appropriate files (files and instructions are available from [here](https://www.dyalog.com/apl-font-keyboard.htm), as is the Dyalog Unicode IME for Microsoft Windows).

## Installing RIDE
### Installing on Linux

The installation process for the RIDE is the same irrespective of whether it is installed as a stand-alone product or on a machine that already has Dyalog installed.

To install the RIDE

1. Download the RIDE's .deb or .rpm file (whichever is appropriate for your Linux distribution) from my.dyalog.com. If your Linux distribution does not support either .deb or .rpm files, then please contact support@dyalog.com.
2. From the command line, use standard installation commands to install the package.

### Installing on macOS

The RIDE is the default UI for Dyalog on macOS and is installed at the same time as Dyalog (see the Dyalog for macOS Installation and Configuration Guide); no further installation is required.

To install the RIDE as a separate, stand-alone, product

1. Download the RIDE's .pkg file from my.dyalog.com.
2. Double-click on the RIDE's .pkg file.
3. Follow the instructions in the RIDE Installer window to successful completion of the installation process.

Starting the RIDE adds its icon to the dock. To keep the RIDE icon in the dock permanently, right-click on the icon and select Options > Keep in Dock from the drop-down list that appears.

### Installing on Microsoft Windows

The installation process for the RIDE is the same irrespective of whether it is installed as a stand-alone product or on a machine that already has Dyalog installed.

To install the RIDE

1. Download the RIDE's .zip file from my.dyalog.com.
2. Unzip the downloaded .zip file, placing the setup_ride.exe and setup_ride.msi files in the same location as each other.
3. Double-click on the setup_ride.exe file.
4. Follow the instructions in the RIDE Installation window to successful completion of the installation process.

## Configuration (.ini) File

A .ini configuration file can be used to define settings for the `RIDE_INIT` configuration parameter. By default, the interpreter will look for a ride.ini file in:

-  the directory in which the default session and log files are stored, for example, C:\Users\JohnDoe\AppData\Local\Programs\Dyalog\ (on Microsoft Windows)
-  $HOME/.dyalog/ (on IBM AIX, macOS and Linux)

This file is not automatically created by Dyalog but can be created manually. Examples of the fields that you might want to include within the .ini configuration file are included in [Appendix 1](sample_configuration_file.md).

A different name and location for the .ini configuration file can be specified by including a second `mode`, `CONFIG`, in the `RIDE_INIT` parameter (see [Section 1.0.1](ride_init.md)) and setting it so that `CONFIG=<filename>`, where `<filename>` is the fully-qualified path to, and name of, a .ini configuration file containing name-value pairs related to mode, certificate details, and so on.

The .ini configuration file must be located on the machine on which the interpreter is running (this is not necessarily the same machine as the one on which the RIDE is running).














