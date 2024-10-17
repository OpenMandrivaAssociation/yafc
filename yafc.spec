%define	name	yafc
%define	version	1.1.1
%define release %mkrel 8

Summary:	Yafc - yet another ftp client
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/File transfer
URL:		https://yafc.sourceforge.net/
Source0:	http://download.sourceforge.net/yafc/%{name}-%{version}.tar.bz2
Patch:		yafc-1.1-gcc.patch
Patch1:		yafc-1.1.1-format.patch
BuildRequires:	readline-devel ncurses-devel heimdal-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Yafc is yet another ftp client, similar to ftp(1).
It is an interactive interface to the FTP protocol.

FEATURES

* cached directory listings
* uses readline (tab completion, emacs/vi editing keys, history file, etc.)
* extensive tab completion
* multiple connections open
* aliases
* colored ls (ie, ls --color, uses $LS_COLORS like GNU ls)
* autologin and bookmarks
* Kerberos authentication support
* recursive get/put/rm/ls
* nohup mode get and put
* tagging (queueing) of files for later transferring
* automagically enters nohup-mode when SIGHUP received (in get and put)
* redirection to local command or file ('>', '>>' and '|')
* uses autoconf and automake
* proxy support
* more...

%prep
%setup -q
%patch -p1 -b .gcc
%patch1 -p1 -b .format

%build
autoreconf -fi
%configure2_5x \
	--without-krb4
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files -f %{name}.lang
%defattr(-,root,root)
%doc contrib BUGS NEWS README THANKS TODO inputrc.sample yafcrc.sample
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man1/*
