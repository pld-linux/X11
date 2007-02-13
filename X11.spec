#
# TODO
# - XDM Auth broken (can anyone confirm now with new implementation?)
# - determine which modules can be used by video Xserver only and which
#   can be shared; review -modules not to require video Xserver, so they
#   can be used by other Xservers alone (such as Xprt)
# - -Xprint seem to be Xprt configuration files - if they aren't used by
#   some (possibly remote) X client, merge them into -Xprt
# - where to take dtpdmd from?
#
# Conditional build:
%bcond_without	glide		# don't build glide driver
%bcond_without	r300		# r300_dri.so
%bcond_with	dualhead	# apply dualhead patch
%bcond_with	via_openchrome	# apply via drivers from openchrome instead xorg

Summary:	XOrg X11 Window System servers and basic programs
Summary(de.UTF-8):	XOrg X11 Window-System-Server und grundlegende Programme
Summary(es.UTF-8):	Programas básicos y servidores para el sistema de ventanas XOrg X11
Summary(fr.UTF-8):	Serveurs du système XOrg X11 et programmes de base
Summary(ja.UTF-8):	XOrg X11 window system のサーバと基本的なプログラム
Summary(ko.UTF-8):	X에 필요한 기본적인 글꼴과 프로그램과 문서들
Summary(pl.UTF-8):	XOrg X11 Window System wraz z podstawowymi programami
Summary(pt_BR.UTF-8):	Programas básicos e servidores para o sistema de janelas XOrg X11
Summary(ru.UTF-8):	Базовые шрифты, программы и документация для рабочей станции под X
Summary(tr.UTF-8):	XOrg X11 Pencereleme Sistemi sunucuları ve temel programlar
Summary(uk.UTF-8):	Базові шрифти, програми та документація для робочої станції під X
Summary(zh_CN.UTF-8):	XOrg X11 窗口系统服务器和基本程序
Name:		X11
Version:	6.9.0
Release:	19
Epoch:		1
License:	MIT/X Consortium/BSD (see README)
Group:		X11
Source0:	ftp://ftp.x.org/pub/X11R%{version}/src/%{name}R%{version}-src1.tar.gz
# Source0-md5:	9cd255a090e81e2c62637122794e6150
Source1:	ftp://ftp.x.org/pub/X11R%{version}/src/%{name}R%{version}-src2.tar.gz
# Source1-md5:	f49a0993d89038a46556720688450479
Source2:	ftp://ftp.x.org/pub/X11R%{version}/src/%{name}R%{version}-src3.tar.gz
# Source2-md5:	4d5450bde835270632e004b25e45ef33
Source7:	ftp://ftp.pld-linux.org/software/xinit/xdm-xinitrc-0.2.tar.bz2
# Source7-md5:	0a15b1c374256b5cad7961807baa3896
Source8:	xdm.pamd
Source9:	xserver.pamd
Source10:	xdm.init
Source11:	xfs.init
Source12:	xfs.config
Source13:	XTerm.ad-pl
Source14:	xdm.sysconfig
Source15:	xfs.sysconfig
Source24:	twm.desktop
Source25:	xeyes.desktop
Source26:	xedit.desktop
Source27:	xterm.desktop
Source28:	xclipboard.desktop
Source29:	xclock.desktop
Source30:	oclock.desktop
Source31:	xconsole.desktop
Source34:	xlogo64.png
Source35:	xeyes.png
Source36:	xedit.png
Source37:	xterm.png
Source38:	xclipboard.png
Source39:	xclock.png
Source40:	oclock.png
Source41:	xconsole.png
Source42:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/XFree86-non-english-Xman-pages.tar.bz2
# Source42-md5:	a184106bb83cb27c6963944d9243ac3f
Source44:	%{name}-Xserver-headers
Source45:	%{name}-Xserver-headers-links
Source46:	twm-xsession.desktop
Source47:	xcalc.desktop
Source48:	xload.desktop
Source49:	xmag.desktop
Source50:	xcalc.png
Source51:	xload.png
Source52:	xmag.png
Source53:	http://oss.sgi.com/projects/ogl-sample/ABI/glext.h
Source54:	XvMCConfig
# NoSource53-md5:	0c40bd4545aa630e139043c2b12f0807
#via_openchrome
Source55:	xorg-via_openchrome_vt3336_branch_snap20070212.patch.tar.bz2
# Source55-md5:       f864012ad05bf2cc7f21b94df55cbdb3
Patch0:		http://xorg.freedesktop.org/releases/X11R6.9.0/patches/x11r6.9.0-geteuid.diff
Patch1:		%{name}-PLD.patch
Patch2:		%{name}-enableglide.patch
Patch3:		%{name}-DisableDebug.patch
Patch4:		%{name}-Xwrapper.patch
Patch5:		%{name}-xfs.patch
Patch6:		%{name}-xterm-utempter.patch
Patch7:		%{name}-app_defaults_dir.patch
Patch8:		%{name}-broken-includes.patch
Patch9:		%{name}-fhs.patch
Patch10:	%{name}-xdmsecurity.patch
Patch11:	%{name}-xman.patch
Patch12:	%{name}-xdm-fixes.patch
Patch13:	%{name}-pic.patch
Patch14:	%{name}-r128-busmstr2.patch
Patch15:	%{name}-neomagic_swcursor.patch
Patch16:	%{name}-mga-busmstr.patch
Patch17:	%{name}-agpgart-load.patch
Patch18:	%{name}-XTerm.ad.patch
Patch19:	%{name}-llh.patch
Patch20:	%{name}-xman-manpaths.patch
Patch21:	%{name}-clearrts.patch
Patch22:	XFree86-Xfont-Type1-large-DoS.patch
Patch23:	%{name}-GLcore-strip-a-workaround.patch
Patch24:	%{name}-pkgconfig.patch
Patch25:	XFree86-spencode-nowarning.patch
Patch26:	%{name}-xterm-256colors.patch
Patch27:	%{name}-makefile-fastbuild.patch
Patch28:	%{name}-dri-ffb-compile.patch
Patch29:	%{name}-radeon-entervt.patch
Patch30:	%{name}-acpi_event_loop_fix.patch
# updated from http://dl.sourceforge.net/i810fb/i810fb-xfree86-420.tar.bz2 : i810fb-xfree420.diff
Patch31:	%{name}-i810fb.patch
# https://bugs.freedesktop.org/show_bug.cgi?id=4320
Patch32:	%{name}-compositefastpath.patch
Patch33:	ftp://ftp.x.org/pub/X11R6.9.0/patches/x11r6.9.0-mitri.diff
Patch34:	%{name}-intel.patch
Patch35:	http://xorg.freedesktop.org/releases/X11R6.9.0/patches/x11r6.9.0-cidfonts.diff
Patch36:	%{name}-i810_945GM.patch
Patch50:	%{name}-glibc-locale_sync.patch
Patch60:	%{name}-oldkeyb.patch
Patch61:	%{name}-sparc64-asmfix.patch
Patch62:	%{name}-sparc64-v9fix.patch
Patch63:	%{name}-pci-build.patch
# from http://xorg.freedesktop.org/releases/X11R6.9.0/patches/x11r6.9.0-setuid.diff, but existing chunks removed.
Patch64:	x11r6.9.0-setuid.diff
# XFree86-tdfx-fix-vtswitch-font-corruption.patch - issue still not fixed,
# but patch doesn't help either; however, it occurs in text mode only, not
# with tdfxfb, which is worth using anyway
Patch65:	x11r6.9.0-dbe-render.diff

# radeon
Patch69:	%{name}-radeon-dynamic-clocks.patch
Patch71:	%{name}-radeon-set-fb-location.patch
Patch72:	http://glen.alkohol.ee/xkb/xorg.patch
Patch73:	%{name}-r300.patch
Patch74:	%{name}-unichrome.patch

#head-patch
#ftp://ftp.linux.cz/pub/linux/people/jan_kasprzak/xorg-dualhead/
Patch100:	ftp://ftp.linux.cz/pub/linux/people/jan_kasprzak/xorg-dualhead/xorg-x11-6.8.1-dualhead.patch

URL:		http://www.x.org/
BuildRequires:	/usr/bin/perl
# Required by xc/programs/Xserver/hw/xfree86/drivers/glide/glide_driver.c
%ifarch %{ix86} %{x8664} ia64
%{?with_glide:BuildRequires:	Glide2x_SDK}
%endif
BuildRequires:	bison
BuildRequires:	cpp
BuildRequires:	ed
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	utempter-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-xauth = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.79.0
Requires:	filesystem >= 2.0-1
Provides:	XFree86 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86
Obsoletes:	xpm-progs
Obsoletes:	xterm
# for /usr/X11R6/bin/mkfontdir
Obsoletes:	XFree86-font-utils
%ifarch sparc sparc64 sparcv9
Obsoletes:	X11R6.1
%endif
ExclusiveArch:	%{ix86} %{x8664} alpha armv4l ia64 m68k ppc sparc sparc64 sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_themesdir	/usr/share/themes
%define		_wmpropsdir	/usr/share/wm-properties
%define		_xsessdir	/usr/share/xsessions
%define		_libx11dir	%{_prefix}/lib/X11
%define		_appdefsdir	%{_libx11dir}/app-defaults

# avoid Mesa dependency in X11-OpenGL-libs
# Glide3 (libglide3.so.3) can be provided by Glide_V3-DRI or Glide_V5-DRI
%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libOSMesa.so.3.3 libglide3.so.3

# ELF objects with Rendition microcode - disliked by ELF utils
%define		_noautostrip	.*\\.uc
%define		_noautochrpath	.*\\.uc

%description
The X Window System provides the base technology for developing
graphical user interfaces. Simply stated, X draws the elements of the
GUI on the user's screen and builds methods for sending user
interactions back to the application. X also supports remote
application deployment--running an application on another computer
while viewing the input/output on your machine. X is a powerful
environment which supports many different applications, such as games,
programming tools, graphics programs, text editors, etc. XOrg X11 is
the version of X which runs on Linux, as well as other platforms.

This package contains the basic fonts, programs and documentation for
an X workstation. However, this package doesn't provide the program
which you will need to drive your video hardware. To control your
video card, you'll need the particular X server package which
corresponds to your computer's video card.

%description -l de.UTF-8
X-Window ist eine voll funktionsfähige grafische Benutzeroberfläche
mit mehreren Fenstern, mehreren Clients und verschiedenen Arten von
Fenstern. Es kommt auf den meisten Unix-Plattformen zum Einsatz. Die
Clients lassen sich auch mit Hilfe anderer Fenstersysteme anzeigen.
Das X-Protokoll gestattet die Ausführung der Applikationen direkt auf
lokalen Rechnern oder über ein Netz und bietet große Flexibilität bei
Client-Server-Implementierungen.

%description -l es.UTF-8
X Window es una interface gráfica completa con múltiples ventanas,
múltiples clientes y diferentes estilos de ventanas. Se usa en la
mayoría de las plataformas Unix, y los clientes también pueden
ejecutar en otros sistemas de ventanas populares. El protocolo X
permite que las aplicaciones puedan ejecutarse tanto en la máquina
local como a través de la red, y proveer flexibilidad en
implementaciones cliente/servidor. Este paquete contiene las fuentes
básicas, programas y documentación para una estación de trabajo X. No
ofrece un servidor X que acceda tu hardware de vídeo -- estos son
puestos a disposición en otro paquete.

%description -l pl.UTF-8
X Window System jest graficznym interfejsem użytkownika; cechuje się
możliwością pracy w wielu oknach, z wieloma klientami i do tego w
różnych wystrojach okien. :) Jest używany na większości platform
sytemów Unix, a klienci mogą być uruchamiani także pod innymi
popularnymi systemami okienkowymi. Protokół X pozwala na uruchamianie
aplikacji zarówno z lokalnej maszyny jak i poprzez sieć - dając przez
to elastyczną implementację architektury klient/serwer.

Pakiet ten nie zawiera X serwera który jest pośrednikiem z Twoją kartą
graficzną (jest on w innym pakiecie).

%description -l pt_BR.UTF-8
X Window é uma interface gráfica completa com múltiplas janelas,
múltiplos clientes e diferentes estilos de janelas. É usado na maioria
das plataformas Unix, e clientes também podem rodar em outros sistemas
de janelas populares. O protocolo X permite que aplicações possam
rodar tanto na máquina local como através da rede, provendo
flexibilidade em implementações cliente/servidor.

Este pacote contém as fontes básicas, programas e documentação para
uma estação de trabalho X. Ele não fornece um servidor X que acessa
seu hardware de vídeo -- estes são disponibilizados em outro pacote.

%description -l ru.UTF-8
X Window System предоставляет базу для разработки графических
интерфейсов пользователя. Попросту говоря, X рисует элементы GUI на
экране пользователя и стоит методы для передачи действий пользователя
прикладным программам. X также поддерживает распределение приложений -
запуск программ на удаленном компьютере с вводом/выводом на
пользовательскую машину. X - это мощная среда, поддерживающая
множество приложений, таких как игры, инструменты для программиста,
графические программы, текстовые редакторы и т.п. XOrg X11 - это
версия X, работающая на Linux и других системах.

Этот пакет содержит базовые шрифты, программы и документацию для
рабочей станции X.

Дополнительно необходимо установить пакеты Xconfigurator, фонтсервер
xfs и библиотеки X11-libs. Возможно придется установить также один или
более пакетов шрифтов XOrg X11.

Ну и, наконец, если вы собираетесь разрабатывать приложения,
работающие как X-клиенты, вам также надо будет установить X11-devel.

%description -l tr.UTF-8
X Window sistemi, çoklu pencere, çoklu istemci ve çeşitli pencere
stilleriyle geniş özelliklere sahip bir Grafik Kullanıcı Arabirimidir.
Çoğu UNIX sisteminde çalıştığı gibi istemcileri de birçok pencereleme
sistemiyle çalışabilir. X protokolu kullanan uygulamaların yerel
makina veya bilgisayar ağı üzerinden çalıştırılabilmesi esnek bir
istemci/sunucu ortamı sağlar. Bu paket bir X istasyonu için gerekli
olan temel yazıtiplerini, programları ve belgeleri sunar. Ekran
kartınızı sürmek için gerekli olan X sunucusu bu pakete dahil
değildir.

%description -l uk.UTF-8
X Window System надає базу для розробки графічних інтерфейсів
користувача. Простіше кажучи, X малює елементи GUI на екрані
користувача та будує методи для передачі дій користувача прикладним
програмам. X також підтримує розподіл прикладних програм - запуск
програм на віддаленому комп'ютері з вводом/виводом на машину
користувача. X - це потужне середовище, яке підтримує велику кількість
різних програм, таких як ігри, інструменти для програміста, графічні
програми, текстові редактори і т.і. XOrg X11 - це версія X, яка працює
на Linux та інших системах.

Цей пакет містить базові шрифти, програми та документацію для робочої
станції X.

Додатково необхідно встановити пакети Xconfigurator, фонтсервер xfs та
бібліотеки X11-libs. Можливо також прийдеться встановити один або
декілька пакетів шрифтів XOrg X11.

Ну і, нарешті, якщо ви збираєтесь розробляти прикладні програми, що
працюють як X-клієнти, вам також треба буде встановити X11-devel.

%package common
Summary:	XOrg X11 files required both on server and client side
Summary(pl.UTF-8):	Pliki XOrg X11 wymagane zarówno po stronie serwera jak i klienta
Group:		X11
Provides:	XFree86-common = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-common

%description common
XOrg X11 files required both on server and client side.

%description common -l pl.UTF-8
Pliki XOrg X11 wymagane zarówno po stronie serwera jak i klienta.

%package Xprint
Summary:	Xprint tool
Summary(pl.UTF-8):	Narzędzie Xprint
Group:		X11
# for /etc/X11/xserver
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description Xprint
Xprint tool.

%description Xprint -l pl.UTF-8
Narzędzie Xprint.

%package DPS
Summary:	Display PostScript
Summary(pl.UTF-8):	Display PostScript
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	DPS
Provides:	XFree86-DPS = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-DPS
Obsoletes:	dgs

%description DPS
X-Window Display PostScript is device-independent imaging model for
displaying information on a screen.

%description DPS -l pl.UTF-8
X-Window Display PostScript to niezależny od urządzenia model
wyświetlania informacji na ekranie.

%package DPS-devel
Summary:	Header files for Display PostScript
Summary(pl.UTF-8):	Pliki nagłówkowe dla Display PostScript
Group:		X11/Development/Libraries
Requires:	%{name}-DPS = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	XFree86-DPS-devel = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-DPS-devel
Obsoletes:	dgs-devel

%description DPS-devel
Header files for develop X-Window Display Postscript.

%description DPS-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki X-Window Display PostScript.

%package DPS-static
Summary:	Display PostScript static libraries
Summary(pl.UTF-8):	Biblioteki statyczne Display PostScript
Group:		X11/Development/Libraries
Requires:	%{name}-DPS-devel = %{epoch}:%{version}-%{release}
Provides:	XFree86-DPS-static = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-DPS-static
Obsoletes:	dgs-static

%description DPS-static
X-Window Display PostScript static libraries.

%description DPS-static -l pl.UTF-8
Statyczne biblioteki X-Window Display PostScript.

%package OpenGL-core
Summary:	OpenGL support extension modules for Xserver
Summary(pl.UTF-8):	Moduły rozszerzeń X serwera obsługujące OpenGL
Group:		X11/Servers
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Provides:	XFree86-OpenGL-core = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-OpenGL-core

%description OpenGL-core
OpenGL support extension modules for Xserver.

%description OpenGL-core -l pl.UTF-8
Moduły rozszerzeń X serwera obsługujące OpenGL.

%package OpenGL-libGL
Summary:	OpenGL support for X11R6 - GL library
Summary(pl.UTF-8):	Wsparcie OpenGL dla systemu X11R6 - biblioteka GL
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	XFree86-OpenGL-libGL = %{epoch}:%{version}-%{release}
Obsoletes:	X11-driver-firegl
Obsoletes:	X11-driver-nvidia
Obsoletes:	XFree86-Mesa-libGL
Obsoletes:	XFree86-OpenGL-libGL
Obsoletes:	XFree86-driver-firegl
Obsoletes:	XFree86-driver-nvidia

%description OpenGL-libGL
OpenGL support for X11R6 system - GL library.

%description OpenGL-libGL -l pl.UTF-8
Wsparcie OpenGL dla systemu X11R6 - biblioteka GL.

%package OpenGL-libs
Summary:	OpenGL libraries for X11R6
Summary(pl.UTF-8):	Biblioteki OpenGL dla systemu X11R6
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	OpenGL = 1.5
Provides:	OpenGL-GLU = 1.3
Provides:	OpenGL-GLX = 1.4
Provides:	XFree86-OpenGL-libs = %{epoch}:%{version}-%{release}
Obsoletes:	Mesa
Obsoletes:	XFree86-OpenGL-libs

%description OpenGL-libs
OpenGL libraries for X11R6 system.

%description OpenGL-libs -l pl.UTF-8
Biblioteki OpenGL dla systemu X11R6.

%package OpenGL-devel-base
Summary:	OpenGL for X11R6 development (GL and GLX only)
Summary(pl.UTF-8):	Pliki nagłówkowe OpenGL dla systemu X11R6 (tylko GL i GLX)
Group:		X11/Development/Libraries
Requires:	%{name}-OpenGL-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	OpenGL-devel-base
Provides:	XFree86-OpenGL-devel-base = %{epoch}:%{version}-%{release}
Obsoletes:	X11-driver-nvidia-devel
Obsoletes:	XFree86-OpenGL-devel-base
Obsoletes:	XFree86-driver-nvidia-devel

%description OpenGL-devel-base
Base headers (GL and GLX only) for OpenGL for X11R6.

%description OpenGL-devel-base -l pl.UTF-8
Podstawowe pliki nagłówkowe (tylko GL i GLX) OpenGL dla systemu X11R6.

%package OpenGL-devel
Summary:	OpenGL for X11R6 development
Summary(pl.UTF-8):	Pliki nagłówkowe OpenGL dla systemu X11R6
Group:		X11/Development/Libraries
Requires:	%{name}-OpenGL-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	OpenGL-devel-base
Provides:	OpenGL-GLU-devel = 1.3
Provides:	OpenGL-GLX-devel = 1.4
Provides:	OpenGL-devel = 1.5
Provides:	XFree86-OpenGL-devel = %{epoch}:%{version}-%{release}
Obsoletes:	Mesa-devel
Obsoletes:	XFree86-OpenGL-devel
Obsoletes:	XFree86-OpenGL-doc
Obsoletes:	glxMesa-devel

%description OpenGL-devel
Headers and man pages for OpenGL for X11R6.

%description OpenGL-devel -l pl.UTF-8
Pliki nagłówkowe i manuale do OpenGL dla systemu X11R6.

%package OpenGL-static
Summary:	X11R6 static libraries with OpenGL
Summary(pl.UTF-8):	Biblioteki statyczne do X11R6 ze wsparciem dla OpenGL
Group:		X11/Development/Libraries
Requires:	%{name}-OpenGL-devel = %{epoch}:%{version}-%{release}
Provides:	OpenGL-GLU-static = 1.3
Provides:	OpenGL-static = 1.5
Provides:	XFree86-OpenGL-static = %{epoch}:%{version}-%{release}
Obsoletes:	Mesa-static
Obsoletes:	XFree86-OpenGL-static

%description OpenGL-static
X11R6 static libraries with OpenGL.

%description OpenGL-static -l pl.UTF-8
Biblioteki statyczne zawierające wsparcie dla OpenGL do X11R6.

%package Xnest
Summary:	XOrg X11 Xnest server
Summary(pl.UTF-8):	Serwer XOrg X11 Xnest
Summary(ru.UTF-8):	"Вложенный" сервер XOrg X11
Summary(uk.UTF-8):	"Вкладений" сервер XOrg X11
Group:		X11/Servers
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	/usr/X11R6/lib/X11/rgb.txt
Requires:	X11-fonts-base
Provides:	XFree86-Xnest = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Xnest

%description Xnest
Xnest is an X Window System server which runs in an X window. Xnest is
a 'nested' window server, actually a client of the real X server,
which manages windows and graphics requests for Xnest, while Xnest
manages the windows and graphics requests for its own clients.

You will need to install Xnest if you require an X server which will
run as a client of your real X server (perhaps for testing purposes).

%description Xnest -l pl.UTF-8
Xnest jest X serwerem uruchamianym w okienku innego X serwera. Xnest
zachowuje się jak X klient w stosunku do prawdziwego X serwera, a jak
X serwer dla własnych klientów.

%description Xnest -l ru.UTF-8
Xnest - это сервер X Window System, который работает в окне X. На
самом деле это клиент реального X-сервера, который управляет окнами и
графическими запросами для Xnest в то время, как Xnest управляет
окнами и графическими запросами для своих собственных клиентов.

Вам надо установить Xnest если вам нужен X-сервер, который работает
как клиент вашего реального X-сервера (скорее всего, в тестовых
целях).

%description Xnest -l uk.UTF-8
Xnest - це сервер X Window System, який працює у вікні X. Фактично це
клієнт реального X-сервера, який керує вікнами та графічними запитами
для Xnest в той час, як Xnest керує вікнами та графічними запитами для
своїх власних клієнтів.

Вам треба встановити Xnest якщо вам потрібен X-сервер, який працює як
клієнт вашого реального X-сервера (скорше всього, у тестових цілях).

%package Xprt
Summary:	X print server
Summary(pl.UTF-8):	X serwer z rozszerzeniem Xprint
Group:		X11/Servers
Requires:	%{name}-Xprint = %{epoch}:%{version}-%{release}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	/usr/X11R6/lib/X11/rgb.txt
Requires:	X11-fonts-base
Requires:	xprint-initrc
Provides:	XFree86-Xprt = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Xprt

%description Xprt
Xprt provides an X server with the print extension and special DDX
implementation.

%description Xprt -l pl.UTF-8
Xprt jest X serwerem z rozszerzeniem Xprint.

%package Xserver
Summary:	XOrg X11 X display server
Summary(de.UTF-8):	XOrg X11 Server
Summary(fr.UTF-8):	Serveur XOrg X11
Summary(pl.UTF-8):	Serwer XOrg X11
Summary(tr.UTF-8):	XOrg X11 sunucusu
Group:		X11/Servers
Requires(pre):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	/usr/X11R6/lib/X11/rgb.txt
Requires:	X11-fonts-base
Requires:	pam >= 0.79.0
Provides:	XFree86-Xserver = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Mono
Obsoletes:	XFree86-SVGA
Obsoletes:	XFree86-VGA16
# obsoleted by many drivers: suncg3,suncg6,suncg14,sunffb,sunleo,suntcx
Obsoletes:	XFree86-Sun
Obsoletes:	XFree86-Sun24
# still not supported in 4.2.0:
#Obsoletes:	XFree86-8514
#Obsoletes:	XFree86-AGX
#Obsoletes:	XFree86-Mach8
#Obsoletes:	XFree86-P9000
# (and many drivers from XF86_SVGA server... and some from others)
Obsoletes:	XFree86-XF86Setup
Obsoletes:	XFree86-Xserver
Obsoletes:	Xconfigurator

%description Xserver
Generally used X server which uses display hardware. It requires
proper driver for your display hardware - package itself contains only
drivers for VGA and VESA-compliant cards (without acceleration). Other
drivers can be found in X11-driver-* packages.

%description Xserver -l pl.UTF-8
Jest to podstawowy X serwer wyświetlający obraz na karcie graficznej.
Do działania wymaga odpowiedniego sterownika - sam pakiet zawiera
tylko odpowiedni dla kart VGA oraz SVGA zgodnych z VESA (bez
akceleracji). Inne sterowniki można znaleźć w pakietach X11-driver-*.

%package Xvfb
Summary:	XOrg X11 Xvfb server
Summary(pl.UTF-8):	Serwer XOrg X11 Xvfb
Summary(ru.UTF-8):	Сервер XOrg X11 для виртуального фреймбуфера
Summary(uk.UTF-8):	Сервер XOrg X11 для віртуального фреймбуфера
Group:		X11/Servers
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	/usr/X11R6/lib/X11/rgb.txt
Requires:	X11-fonts-base
Provides:	XFree86-Xvfb = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Xvfb

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X Window System server that is
capable of running on machines with no display hardware and no
physical input devices. Xvfb emulates a dumb framebuffer using virtual
memory. Xvfb doesn't open any devices, but behaves otherwise as an X
display. Xvfb is normally used for testing servers. Using Xvfb, the
mfb or cfb code for any depth can be exercised without using real
hardware that supports the desired depths. Xvfb has also been used to
test X clients against unusual depths and screen configurations, to do
batch processing with Xvfb as a background rendering engine, to do
load testing, to help with porting an X server to a new platform, and
to provide an unobtrusive way of running applications which really
don't need an X server but insist on having one.

If you need to test your X server or your X clients, you may want to
install Xvfb for that purpose.

%description Xvfb -l pl.UTF-8
Xvfb (X Virtual Frame Buffer) jest X serwerem, który można uruchamiać
na maszynach bez urządzeń wyświetlających ani fizycznych urządzeń
wejściowych. Xvfb emuluje prosty framebuffer w pamięci. Zwykle jest
używany do testowania X serwerów, może też być używany do testowania X
klientów w rzadko używanych konfiguracjach ekranu. Można też użyć Xvfb
do uruchomienia aplikacji, które w rzeczywistości nie wymagają X
serwera, ale odmawiają uruchomienia bez niego.

%description Xvfb -l ru.UTF-8
Xvfb (X Virtual Frame Buffer) - это X-сервер, который способен
работать на машинах без дисплейной аппаратуры и физических устройств
ввода. Xvfb эмулирует простейший фреймбуфер используя виртуальную
память. Xvfb не открывает никаких устройств, ведя себя как нормальный
X-сервер во всем остальном. Обычно он используется для проверки
серверов. Используя Xvfb, можно тестировать код mfb или cfb для любой
глубины цвета без использования реальной аппаратуры, поддерживающей
такую глубину. Xvfb также можно использовать для проверки X-клиентов с
необычными глубинами цвета и конфигурациями экрана, производить
пакетную обработку с Xvfb в качестве фонового рендерера, проводить
нагрузочные тесты, для помощи в портировании X-сервера на новую
платформу и для хитроумного запуска приложений, которым реально не
нужен X-сервер, но которые настаивают на том, чтоб он был доступен.

Если вам надо тестировать ваши X-сервера или X-клиенты, вы можете
установить для этой цели Xvfb.

%description Xvfb -l uk.UTF-8
Xvfb (X Virtual Frame Buffer) - це X-сервер, здатний працювати на
машинах без дисплейної апаратури та візичних пристроїв вводу. Xvfb
емулює найпростіший фреймбуфер використовуючи віртуальну пам'ять. Xvfb
не відкриває ніяких пристроїв, ведучи себе як нормальний X-сервер у
решті відношень. Зазвичай його використовують для перевірки серверів.
Використовуючи Xvfb, можна тестувати код mfb або cfb для будь-якої
глибини кольору та конфігурації екрану без використання реальної
апаратури, яка підтримує такі режими. Також Xvfb можна використати для
перевірки X-клієнтів з незвичними глибинами кольору та конфігураціями
екрану, проводити пакетну обробку з Xvfb у якості фонового рендерера,
проводити нагрузочні тести, для допомоги у портуванні X-сервера на
нову платформу та запуску програм, яким реально не потрібен X-сервер,
але які наполягають на тому, щоб він був доступний.

Якщо вам потрібно тестувати ваші X-сервери або X-клієнти, ви можете
встановити для цієї цілі Xvfb.

%package devel
Summary:	X11R6 headers and programming man pages
Summary(de.UTF-8):	X11R6 Headers und man pages für Programmierer
Summary(fr.UTF-8):	Pages man de programmation
Summary(pl.UTF-8):	Pliki nagłówkowe X11R6
Summary(ru.UTF-8):	Библиотеки разработчика, хедера и документация по программированию X11R6
Summary(tr.UTF-8):	X11R6 ile geliştirme için gerekli dosyalar
Summary(uk.UTF-8):	Бібліотеки програміста, хедери та документація по програмуванню X11R6
Group:		X11/Development/Libraries
Requires:	%{name}-imake = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	fontconfig-devel >= 1:2.2.0
Provides:	XFree86-devel = %{epoch}:%{version}-%{release}
Provides:	libXvMCW-devel
Provides:	render = 0.8
Provides:	xcursor-devel = 1.1.2
Provides:	xft-devel = 2.1.6
Provides:	xpm-devel
Provides:	xrender-devel = 0.8.4
# don't use package names from xlibs implementation as metapackages
#Provides:	libXcomposite-devel
#Provides:	libXdamage-devel
#Provides:	libXfixes-devel
#Provides:	libXrender-devel
%ifarch sparc sparc64 sparcv9
Obsoletes:	X11R6.1-devel
%endif
Obsoletes:	XFree86-devel
Obsoletes:	XFree86-render
Obsoletes:	XFree86-xcursor-devel
Obsoletes:	XFree86-xft-devel
Obsoletes:	XFree86-xft2-devel
Obsoletes:	XFree86-xrender-devel
Obsoletes:	Xft-devel
Obsoletes:	libXvMCW-devel
Obsoletes:	render
Obsoletes:	xcursor-devel
Obsoletes:	xft-devel
Obsoletes:	xpm-devel
Obsoletes:	xrender-devel

%description devel
Libraries, header files, and documentation for developing programs
that run as X clients. It includes the base Xlib library as well as
the Xt and Xaw widget sets.

%description devel -l de.UTF-8
Libraries, Header-Dateien und Dokumentation zum Entwickeln von
Programmen, die als X-Clients laufen. Enthält die Xlib-Library und die
Widget-Sätze Xt und Xaw.

%description devel -l fr.UTF-8
Bibliothéques, fichiers d'en-tête, et documentation pour développer
des programmes s'exécutant en clients X. Cela comprend la Bibliothéque
Xlib de base aussi bien que les ensembles de widgets Xt et Xaw.

%description devel -l pl.UTF-8
Pliki nagłówkowe, dokumentcja dla programistów rozwijających aplikacje
klienckie pod X Window. Zawiera podstawową bibliotekę Xlib a także Xt
i Xaw.

%description devel -l ru.UTF-8
X11-devel включает библиотеки, хедера и документацию, необходимые для
разработки программ, работающих как X-клиенты. X11-devel включает
базовую библиотеку Xlib и наборы примитивов Xt и Xaw.

Установите X11-devel если вы собираетесь разрабатывать программы,
которые будут работать как X-клиенты.

%description devel -l tr.UTF-8
X istemcisi olarak çalışacak programlar geliştirmek için gereken
statik kitaplıklar, başlık dosyaları ve belgeler. Xlib kitaplığının
yanısıra Xt ve Xaw arayüz kitaplıklarını da içerir.

%description devel -l uk.UTF-8
X11-devel містить бібліотеки, хедери та документацію, необхідні для
розробки програм, які працюють як X-клієнти. X11-devel містить базову
бібліотеку Xlib та набори примітивів Xt та Xaw.

Встановіть X11-devel якщо ви збираєтесь розробляти програми, які
будуть працювати як X-клієнти.

%package Xserver-devel
Summary:	Header files for XOrg X11 Xserver drivers/extensions development
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia sterowników/rozszerzeń X serwera XOrg X11
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	XFree86-Xserver-devel = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Xserver-devel

%description Xserver-devel
Header files for XOrg X11 Xserver drivers and extensions development.

%description Xserver-devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia sterowników i rozszerzeń X serwera XOrg
X11.

%package driver-apm
Summary:	Alliance Promotion video driver
Summary(pl.UTF-8):	Sterownik do kart Alliance Promotion
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Alliance
Obsoletes:	XFree86-driver-apm

%description driver-apm
Alliance Promotion driver.

%description driver-apm -l pl.UTF-8
Sterownik do kart Alliance Promotion.

%package driver-ark
Summary:	Ark Logic video driver
Summary(pl.UTF-8):	Sterownik do kart Ark Logic
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-ark

%description driver-ark
Ark Logic driver.

%description driver-ark -l pl.UTF-8
Sterownik do kart Ark Logic.

%package driver-ati
Summary:	ATI video driver
Summary(pl.UTF-8):	Sterownik do kart ATI
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-driver-i2c = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-ATI
Obsoletes:	XFree86-Mach32
Obsoletes:	XFree86-Mach64
Obsoletes:	XFree86-driver-ati

%description driver-ati
ATI video driver.

%description driver-ati -l pl.UTF-8
Sterownik do kart ATI.

%package driver-r128
Summary:	ATI Rage 128 video driver
Summary(pl.UTF-8):	Sterownik do kart ATI Rage 128
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Rage128
Obsoletes:	XFree86-driver-r128

%description driver-r128
ATI Rage 128 video driver.

%description driver-r128 -l pl.UTF-8
Sterownik do kart ATI Rage 128.

%package driver-r128-dri
Summary:	DRI modules for ATI Rage 128 video driver
Summary(pl.UTF-8):	Moduły DRI dla sterownika do kart ATI Rage 128
Group:		X11/Servers
Requires:	%{name}-driver-r128 = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif

%description driver-r128-dri
DRI modules for ATI Rage 128 video driver.

%description driver-r128-dri -l pl.UTF-8
Moduły DRI dla sterownika do kart ATI Rage 128.

%package driver-radeon
Summary:	ATI Radeon video driver
Summary(pl.UTF-8):	Sterownik do kart ATI Radeon
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-driver-ati = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-radeon

%description driver-radeon
ATI Radeon video driver.

%description driver-radeon -l pl.UTF-8
Sterownik do kart ATI Radeon.

%package driver-radeon-dri
Summary:	DRI modules for ATI Radeon video driver
Summary(pl.UTF-8):	Moduły DRI dla sterownika do kart ATI Radeon
Group:		X11/Servers
Requires:	%{name}-driver-radeon = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif

%description driver-radeon-dri
DRI modules for ATI Radeon video driver.

%description driver-radeon-dri -l pl.UTF-8
Moduły DRI dla sterownika do kart ATI Radeon.

%package driver-chips
Summary:	Chips and Technologies video driver
Summary(pl.UTF-8):	Sterownik do kart na układach Chips and Technologies
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-ChipsTechnologies
Obsoletes:	XFree86-driver-chips

%description driver-chips
Chips and Technologies video driver.

%description driver-chips -l pl.UTF-8
Sterownik do kart na układach Chips and Technologies.

%package driver-cirrus
Summary:	Cirrus Logic video driver
Summary(pl.UTF-8):	Sterownik do kart Cirrus Logic
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Cirrus
Obsoletes:	XFree86-driver-cirrus

%description driver-cirrus
Cirrus Logic video driver.

%description driver-cirrus -l pl.UTF-8
Sterownik do kart Cirrus Logic.

%package driver-cyrix
Summary:	Cyrix video driver
Summary(pl.UTF-8):	Sterownik do grafiki na układzie Cyrix MediaGX
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Cyrix
Obsoletes:	XFree86-driver-cyrix

%description driver-cyrix
Cyrix video driver.

%description driver-cyrix -l pl.UTF-8
Sterownik do grafiki na układzie Cyrix MediaGX.

%package driver-fbdev
Summary:	Video driver for framebuffer device
Summary(pl.UTF-8):	Sterownik korzystający z framebuffera
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-FBDev
Obsoletes:	XFree86-driver-fbdev

%description driver-fbdev
Non-accelerated video driver for framebuffer device.

%description driver-fbdev -l pl.UTF-8
Nieakcelerowany sterownik korzystający z framebuffera.

%package driver-glide
Summary:	3Dfx Voodoo1 and Voodoo2 video driver
Summary(pl.UTF-8):	Sterownik do kart 3Dfx Voodoo1 i Voodoo2
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
# dlopens libglide2x.so
Requires:	Glide_VG
Obsoletes:	XFree86-driver-glide

%description driver-glide
Voodoo1 and Voodoo2 video driver.

%description driver-glide -l pl.UTF-8
Sterownik do kart Voodoo1 i Voodoo2 firmy 3Dfx.

%package driver-glint
Summary:	GLINT/Permedia video driver
Summary(pl.UTF-8):	Sterownik do kart GLINT i Permedia
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-3DLabs
Obsoletes:	XFree86-driver-glint

%description driver-glint
GLINT/Permedia video driver.

%description driver-glint -l pl.UTF-8
Sterownik do kart GLINT i Permedia.

%package driver-glint-dri
Summary:	DRI modules for GLINT/Permedia video driver
Summary(pl.UTF-8):	Moduły DRI dla sterownika do kart GLINT i Permedia
Group:		X11/Servers
Requires:	%{name}-driver-glint = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif

%description driver-glint-dri
DRI modules for GLINT/Permedia video driver.

%description driver-glint-dri -l pl.UTF-8
Moduły DRI dla sterownika do kart GLINT i Permedia.

%package driver-i128
Summary:	Number 9 I128 video driver
Summary(pl.UTF-8):	Sterownik do kart Number 9 I128
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-I128
Obsoletes:	XFree86-driver-i128

%description driver-i128
Number 9 I128 video driver.

%description driver-i128 -l pl.UTF-8
Sterownik do kart Number 9 I128.

%package driver-i2c
Summary:	I2C drivers
Summary(pl.UTF-8):	Sterowniki I2C
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-i2c
I2C drivers.

%description driver-i2c -l pl.UTF-8
Sterowniki I2C.

%package driver-i740
Summary:	Intel i740 video driver
Summary(pl.UTF-8):	Sterownik do kart na układzie Intel i740
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-i740
Obsoletes:	XFree86-i740

%description driver-i740
Intel i740 video driver.

%description driver-i740 -l pl.UTF-8
Sterownik do kart na układzie Intel i740.

%package driver-i810
Summary:	Intel i810/i815/i830 video driver
Summary(pl.UTF-8):	Sterownik do grafiki na układach Intel i810/i815/i830
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-i810
Obsoletes:	XFree86-i810

%description driver-i810
Intel i810/i815/i830 video driver.

%description driver-i810 -l pl.UTF-8
Sterownik do grafiki na układach Intel i810/i815/i830.

%package driver-i810-dri
Summary:	DRI modules dor Intel i810/i815/i830 video driver
Summary(pl.UTF-8):	Moduły DRI dla sterownika do grafiki na układach Intel i810/i815/i830
Group:		X11/Servers
Requires:	%{name}-driver-i810 = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif

%description driver-i810-dri
DRI modules dor Intel i810/i815/i830 video driver.

%description driver-i810-dri -l pl.UTF-8
Moduły DRI dla sterownika do grafiki na układach Intel i810/i815/i830.

%package driver-imstt
Summary:	Integrated Micro Solutions Twin Turbo 128 driver
Summary(pl.UTF-8):	Sterownik do kart Integrated Micro Solutions Twin Turbo 128
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-imstt

%description driver-imstt
Integrated Micro Solutions Twin Turbo 128 driver.

%description driver-imstt -l pl.UTF-8
Sterownik do kart Integrated Micro Solutions Twin Turbo 128.

%package driver-mga
Summary:	Matrox video driver
Summary(pl.UTF-8):	Sterownik do kart Matrox
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-mga
Obsoletes:	XFree86-mga

%description driver-mga
Matrox video driver.

%description driver-mga -l pl.UTF-8
Sterownik do kart Matrox.

%package driver-mga-dri
Summary:	DRI modules for Matrox video driver
Summary(pl.UTF-8):	Moduly DRI dla sterownika do kart Matrox
Group:		X11/Servers
Requires:	%{name}-driver-mga = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif

%description driver-mga-dri
DRI modules for Matrox video driver.

%description driver-mga-dri -l pl.UTF-8
Moduly DRI dla sterownika do kart Matrox.

%package driver-neomagic
Summary:	NeoMagic video driver
Summary(pl.UTF-8):	Sterownik do kart NeoMagic
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-NeoMagic
Obsoletes:	XFree86-driver-neomagic

%description driver-neomagic
NeoMagic video driver.

%description driver-neomagic -l pl.UTF-8
Sterownik do kart NeoMagic.

%package driver-newport
Summary:	Newport (XL) adapters video driver
Summary(pl.UTF-8):	Sterownik do kart Newport (XL)
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-newport

%description driver-newport
Newport (XL) adapters video driver (found primarily in SGI Indy and
Indigo2 machines).

%description driver-newport -l pl.UTF-8
Sterownik do kart Newport (XL) (występujących głównie w komputerach
SGI Indy i Indigo).

%package driver-nsc
Summary:	National Semiconductors GEODE family video driver
Summary(pl.UTF-8):	Sterownik dla kart na układach z rodziny GEODE firmy National Semiconductors
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-nsc

%description driver-nsc
National Semiconductors GEODE family video driver. Supports GXLV (5530
companion chip), SC1200, SC1400 and GX2 (5535 companion chip).

%description driver-nsc -l pl.UTF-8
Sterownik dla kart na układach z rodziny GEODE firmy National
Semiconductors. Obsługuje GXLV (układ towarzyszący 5530), SC1200,
SC1400 oraz GX2 (układ towarzyszący 5535).

%package driver-nv
Summary:	nVidia video driver
Summary(pl.UTF-8):	Sterownik do kart na układach firmy nVidia
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-NVidia
Obsoletes:	XFree86-driver-nv

%description driver-nv
nVidia video driver. Supports Riva128, RivaTNT, GeForce.

%description driver-nv -l pl.UTF-8
Sterownik do kart na układach firmy nVidia: Riva128, RivaTNT, GeForce.

%package driver-rendition
Summary:	Rendition video driver
Summary(pl.UTF-8):	Sterownik do kart Rendition
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Rendition
Obsoletes:	XFree86-driver-rendition

%description driver-rendition
Rendition/Micron video driver.

%description driver-rendition -l pl.UTF-8
Sterownik do kart Verite firmowanych przez Rendition/Micron.

%package driver-s3virge
Summary:	S3 ViRGE/Trio3D video driver
Summary(pl.UTF-8):	Sterownik do kart na układach S3 ViRGE i Trio3D
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-S3V
Obsoletes:	XFree86-driver-s3virge

%description driver-s3virge
S3 ViRGE/Trio3D video driver.

%description driver-s3virge -l pl.UTF-8
Sterownik do kart na układach S3 ViRGE i Trio3D.

%package driver-s3
Summary:	S3 Trio video driver
Summary(pl.UTF-8):	Sterownik do kart na układach S3 Trio
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-S3
Obsoletes:	XFree86-driver-s3

%description driver-s3
S3 Trio video driver.

%description driver-s3 -l pl.UTF-8
Sterownik do kart na układach S3 Trio.

%package driver-savage
Summary:	S3 Savage video driver
Summary(pl.UTF-8):	Sterownik do kart na układach S3 Savage
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-savage

%description driver-savage
S3 Savage video driver.

%description driver-savage -l pl.UTF-8
Sterownik do kart na układach S3 Savage.

%package driver-siliconmotion
Summary:	Silicon Motion video driver
Summary(pl.UTF-8):	Sterownik do kart na układach Silicon Motion
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-siliconmotion

%description driver-siliconmotion
Silicon Motion video driver.

%description driver-siliconmotion -l pl.UTF-8
Sterownik do kart na układach Lynx firmy Silicon Motion.

%package driver-sis
Summary:	SiS video driver
Summary(pl.UTF-8):	Sterownik do kart na układach SiS
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-SiS
Obsoletes:	XFree86-driver-sis

%description driver-sis
SiS video driver.

%description driver-sis -l pl.UTF-8
Sterownik do kart na układach SiS.

%package driver-sis-dri
Summary:	DRI modules for SiS video driver
Summary(pl.UTF-8):	Moduły DRI dla sterownika do kart na układach SiS
Group:		X11/Servers
Requires:	%{name}-driver-sis = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
%endif

%description driver-sis-dri
DRI modules for SiS video driver.

%description driver-sis-dri -l pl.UTF-8
Moduły DRI dla sterownika do kart na układach SiS.

%package driver-sisusb
Summary:	Video driver for SiS video chips connected via a Net2280-based USB dongle
Summary(pl.UTF-8):	Sterownik obrazu dla układów SiS podłączonych poprzez przejściówkę USB Net2280
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description driver-sisusb
Video driver for SiS video chips connected via a Net2280-based USB
dongle. It supports SiS315E/PRO video chipset.

Note: it requires a Linux kernel driver (included in Linux 2.6.12 and
later).

%description driver-sisusb -l pl.UTF-8
Sterownik obrazu dla układów SiS podłączonych poprzez przejściówkę USB
opartą na układzie Net2280. Obsługuje układ graficzny SiS315E/PRO.

Uwaga: wymaga sterownika jądra Linuksa (załączonego w wersji Linuksa
2.6.12 i późniejszych).

%package driver-sunbw2
Summary:	sunbw2 - Sun BW2 video driver
Summary(pl.UTF-8):	Sterownik do monochromatycznego framebuffera BW2 na Sunie
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-SunMono
Obsoletes:	XFree86-driver-sunbw2

%description driver-sunbw2
sunbw2 - Sun BW2 video driver.

%description driver-sunbw2 -l pl.UTF-8
Sterownik do monochromatycznego framebuffera BW2 na Sunie.

%package driver-suncg14
Summary:	suncg14 - Sun CG14 video driver
Summary(pl.UTF-8):	Sterownik do kolorowego framebuffera CG14 na Sunie
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-suncg14

%description driver-suncg14
suncg14 - Sun CG14 video driver.

%description driver-suncg14 -l pl.UTF-8
Sterownik do kolorowego framebuffera CG14 na Sunie.

%package driver-suncg3
Summary:	suncg3 - Sun CG3 video cards driver
Summary(pl.UTF-8):	Sterownik do kolorowego framebuffera CG3 na Sunie
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-suncg3

%description driver-suncg3
suncg3 - Sun CG3 video cards driver.

%description driver-suncg3 -l pl.UTF-8
Sterownik do kolorowego framebuffera CG3 na Sunie.

%package driver-suncg6
Summary:	suncg6 - Sun GX and Turbo GX video driver
Summary(pl.UTF-8):	Sterownik do grafiki GX i Turbo GX na Sunie
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-suncg6

%description driver-suncg6
suncg6 - Sun GX and Turbo GX video driver.

%description driver-suncg6 -l pl.UTF-8
Sterownik do grafiki GX i Turbo GX na Sunie.

%package driver-sunffb
Summary:	sunffb - Sun Creator, Creator 3D and Elite 3D video cards driver
Summary(pl.UTF-8):	Sterownik do kart Sun Creator, Creator 3D, Elite 3D
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-sunffb

%description driver-sunffb
sunffb - Sun Creator, Creator 3D and Elite 3D video cards driver.

%description driver-sunffb -l pl.UTF-8
Sterownik do kart Sun Creator, Creator 3D, Elite 3D.

%package driver-sunleo
Summary:	sunleo - Sun Leo (ZX) video cards driver
Summary(pl.UTF-8):	Sterownik do kart Sun Leo (ZX)
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-sunleo

%description driver-sunleo
sunleo - Sun Leo (ZX) video cards driver.

%description driver-sunleo -l pl.UTF-8
Sterownik do kart Sun Leo (ZX).

%package driver-suntcx
Summary:	suntcx - Sun TCX video cards driver
Summary(pl.UTF-8):	Sterownik do kart Sun TCX
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-suntcx

%description driver-suntcx
suntcx - Sun TCX video cards driver.

%description driver-suntcx -l pl.UTF-8
Sterownik do kart Sun TCX.

%package driver-tdfx
Summary:	3Dfx video driver
Summary(pl.UTF-8):	Sterownik do kart 3Dfx
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-3dfx
Obsoletes:	XFree86-driver-tdfx

%description driver-tdfx
3Dfx video driver. Supports Voodoo Banshee, Voodoo3, Voodoo4, Voodoo5.
For Banshee or Voodoo3, DRI driver requires Glide_V3-DRI package, for
Voodoo4 or Voodoo5 it requires Glide_V5-DRI package.

%description driver-tdfx -l pl.UTF-8
Sterownik do kart 3Dfx: Voodoo Banshee, Voodoo3, Voodoo4, Voodoo5.
Sterownik DRI wymaga pakietu Glide_V3-DRI do kart Banshee lub Voodoo3,
a Glide_V5-DRI do kart Voodoo4 lub Voodoo5.

%package driver-tdfx-dri
Summary:	DRI modules for 3Dfx video driver
Summary(pl.UTF-8):	Moduły DRI dla sterownika do kart 3Dfx
Group:		X11/Servers
Requires:	%{name}-driver-tdfx = %{epoch}:%{version}-%{release}
%ifarch %{ix86} ia64 alpha arm ppc
# for dri
Requires:	%{name}-OpenGL-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-OpenGL-libGL = %{epoch}:%{version}-%{release}
# -libs already required by -OpenGL-libGL
# dlopens libglide3x.so
Requires:	Glide3-DRI
%endif

%description driver-tdfx-dri
DRI modules for 3Dfx video driver.

%description driver-tdfx-dri -l pl.UTF-8
Moduły DRI dla sterownika do kart 3Dfx.

%package driver-tga
Summary:	TGA video driver
Summary(pl.UTF-8):	Sterownik do kart TGA
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-TGA
Obsoletes:	XFree86-driver-tga

%description driver-tga
TGA video driver.

%description driver-tga -l pl.UTF-8
Sterownik do kart TGA.

%package driver-trident
Summary:	Trident video driver
Summary(pl.UTF-8):	Sterownik do kart Trident
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Trident
Obsoletes:	XFree86-driver-trident

%description driver-trident
Trident video driver.

%description driver-trident -l pl.UTF-8
Sterownik do kart Trident.

%package driver-tseng
Summary:	Tseng Labs video driver
Summary(pl.UTF-8):	Sterownik do kart Tseng Labs
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-Tseng
Obsoletes:	XFree86-W32
Obsoletes:	XFree86-driver-tseng

%description driver-tseng
Tseng Labs video driver.

%description driver-tseng -l pl.UTF-8
Sterownik do kart firmy Tseng Labs.

%package driver-via
Summary:	VIA CLE266 driver
Summary(pl.UTF-8):	Sterownik do kart VIA CLE266
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-via

%description driver-via
VIA CLE266 driver.

%description driver-via -l pl.UTF-8
Sterownik do kart VIA CLE266.

%package driver-vmware
Summary:	VMWare SVGA emulated video driver
Summary(pl.UTF-8):	Sterownik do emulacji karty SVGA dostępnej pod VMware
Group:		X11/Servers
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-driver-vmware

%description driver-vmware
VMware emulated SVGA video driver. Necessary if you run Linux on
VMware virtual machine.

%description driver-vmware -l pl.UTF-8
Sterownik do emulacji karty SVGA dostępnej pod VMware. Przydatny,
jeśli uruchamiasz Linuksa na wirtualnej maszynie VMware.

%package libs
Summary:	X11R6 shared libraries
Summary(de.UTF-8):	X11R6 shared Libraries
Summary(es.UTF-8):	Bibliotecas compartidas X11R6
Summary(fr.UTF-8):	Bibliothèques partagées X11R6
Summary(pl.UTF-8):	Biblioteki dzielone dla X11R6
Summary(pt_BR.UTF-8):	Bibliotecas compartilhadas X11R6
Summary(ru.UTF-8):	Разделяемые библиотеки для X Window System (X11R6.4)
Summary(uk.UTF-8):	Бібліотеки спільного використання для X Window System (X11R6.4)
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	glibc >= 6:2.3.5-7.6
Provides:	XFree86-libs = %{epoch}:%{version}-%{release}
#Provides:	libXcomposite
#Provides:	libXdamage
#Provides:	libXfixes
#Provides:	libXrender
Provides:	libXvMCW
Provides:	xcursor = 1.1.2
Provides:	xft = 2.1.6
Provides:	xpm
Provides:	xrender = 0.8.4
%ifarch sparc sparc64 sparcv9
Obsoletes:	X11R6.1-libs
%endif
Obsoletes:	XFree86-libs
Obsoletes:	XFree86-xcursor
Obsoletes:	XFree86-xft
Obsoletes:	XFree86-xft2
Obsoletes:	XFree86-xrender
Obsoletes:	Xft
Obsoletes:	libXvMCW
Obsoletes:	xcursor
Obsoletes:	xft
Obsoletes:	xorg-x11-libs-data
Obsoletes:	xpm
Obsoletes:	xrender

%description libs
X11-libs contains the shared libraries that most X programs need to
run properly. These shared libraries are in a separate package in
order to reduce the disk space needed to run X applications on a
machine without an X server (i.e, over a network).

If you are installing the X Window System on your machine, you will
need to install X11-libs. You will also need to install the X11
package, X11-Xserver, one of the X11-driver-*, X11-fonts,
X11-fonts-ISO8859-1, optionally some of the other fonts (choose 75dpi
or 100dpi depending upon your monitor's resolution), the X11-setup and
the X11-tools. And, finally, if you are going to be developing
applications that run as X clients, you will also need to install
X11-devel.

%description libs -l de.UTF-8
Dieses Paket enthält die zur gemeinsamen Nutzung vorgesehenen
Libraries, die die meisten X-Programme für den einwandfreien Betrieb
benötigen. Sie wurden in einem separaten Paket untergebracht, um den
Festplattenspeicherplatz auf Computern zu reduzieren, die ohne einen
X- Server (über ein Netz) arbeiten.

%description libs -l es.UTF-8
Este paquete contiene bibliotecas compartidas que la mayoría de los
programas X necesitan para ejecutarse correctamente. Están en un
paquete a parte, para reducir el espacio en disco necesario para
ejecutar aplicaciones X en una máquina sin un servidor X (a través de
la red).

%description libs -l fr.UTF-8
Ce paquetage contient les bibliothèques partagées nécessaires à de
nombreux programmes X. Elles se trouvent dans un paquetage séparé afin
de réduire l'espace disque nécessaire à l'exécution des applications X
sur une machine sans serveur X (en réseau).

%description libs -l pl.UTF-8
Pakiet zawierający podstawowe biblioteki potrzebne większości
programów korzystających z systemu X Window. Wydzielony w celu
oszczędności miejsca potrzebnego do uruchamiania aplikacji X Window na
komputerach bez X serwera (np. przez sieć).

%description libs -l pt_BR.UTF-8
Este pacote contém bibliotecas compartilhadas que a maioria dos
programas X precisam para rodar corretamente. Eles estão em um pacote
separado para reduzir o espaço em disco necessário para rodar
aplicações X em uma máquina sem um servidor X (através da rede).

%description libs -l tr.UTF-8
Bu paket X programlarının düzgün çalışabilmeleri için gereken
kitaplıkları içerir. Bunlar, X programlarını (sunucu olsun olmasın)
çalıştırmak için gerekli disk alanını azaltmak için ayrı bir paket
olarak sunulmuştur.

%description libs -l ru.UTF-8
X11-libs содержит разделяемые библиотеки, которые необходимы для
работы большинству программ для X. Эти библиотеки вынесены в отдельный
пакет чтобы сэкономить дисковое пространство, необходимое для запуска
приложений X на машинах без X-сервера (например, по сети).

Если вы устанавливаете X Window System на вашей машине, вам необходимо
установить X11-libs. Также необходимо установить следующие пакеты:
XOrg X11, один или несколько пакетов шрифтов XOrg X11, Xconfigurator,
X11-xfs.

Если вы собираетесь разрабатывать программы, работающие как X-клиенты,
вам также надо установить X11-devel.

%description libs -l uk.UTF-8
X11-libs містить бібліотеки спільного використання, котрі необхідні
для роботи більшості прикладних програм для X. Ці бібліотеки винесені
в окремий пакет для економії дискового простору, необхідного для
запуску прикладних програм X на машинах без X-серверу (наприклад, по
мережі).

Якщо ви встановлюєте X Window System на вашій машині, вам необхідно
встановити X11-libs. Також необхідно встановити такі пакети: XOrg X11,
один або декілька пакетів шрифтів XOrg X11, Xconfigurator, X11-xfs.

Якщо ви збираєтесь розробляти програми, які працюють як X-клієнти, вам
також необхідно встановити X11-devel.

%package modules
Summary:	Modules with X servers extensions
Summary(pl.UTF-8):	Wspólne dla wszystkich X serwerów moduły rozszerzeń
Group:		X11/Servers
Provides:	XFree86-modules = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-module-PEX
Obsoletes:	XFree86-module-XIE
Obsoletes:	XFree86-modules

%description modules
Modules with X servers extensions.

%description modules -l pl.UTF-8
Wspólne dla wszystkich X serwerów moduły rozszerzeń.

%package setup
Summary:	Graphical configuration tool for XOrg X11
Summary(pl.UTF-8):	Graficzny konfigurator dla XOrg X11
Summary(ru.UTF-8):	Утилита для конфигурации XOrg X11
Summary(uk.UTF-8):	Утиліта для конфігурування XOrg X11
Group:		X11
Requires:	%{name}-Xserver = %{epoch}:%{version}-%{release}
Provides:	XFree86-setup = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-setup
Obsoletes:	XFree86-xf86cfg

%description setup
Setup containst a configuration tool for the XOrg X11 family of
servers. It allows you to configure video settings, keyboard layouts,
mouse type, and other miscellaneous options. It is slow however, and
requires the generic VGA 16 color server be available.

%description setup -l pl.UTF-8
Pakiet setup zawiera narzędzia do konfiguracji XOrg X11. Pozwala na
skonfigurowanie ustawień obrazu, klawiatury, typu myszki i innych
różnych rzeczy. Jednakże jest wolny i wymaga dostępności serwera do
standardowej 16-kolorowej VGA.

%description setup -l ru.UTF-8
Утилита для конфигурации XOrg X11.

%description setup -l uk.UTF-8
Утиліта для конфігурування XOrg X11.

%package static
Summary:	X11R6 static libraries
Summary(pl.UTF-8):	Biblioteki statyczne X11R6
Summary(ru.UTF-8):	Статические библиотеки X11R6
Summary(uk.UTF-8):	Статичні бібліотеки X11R6
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	XFree86-static = %{epoch}:%{version}-%{release}
Provides:	xcursor-static = 1.1.2
Provides:	xft-static = 2.1.6
Provides:	xpm-static
Provides:	xrender-static = 0.8.4
%ifarch sparc sparc64 sparcv9
Obsoletes:	X11R6.1-devel
%endif
Obsoletes:	XFree86-static
Obsoletes:	XFree86-xcursor-static
Obsoletes:	XFree86-xft-static
Obsoletes:	XFree86-xrender-static
Obsoletes:	Xft-devel
Obsoletes:	xcursor-static
Obsoletes:	xft-static
Obsoletes:	xpm-static
Obsoletes:	xrender-static

%description static
X11R6 static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne X11R6.

%description static -l ru.UTF-8
X11-static включает статические библиотеки, необходимые для разработки
программ, работающих как X-клиенты. собранные программы, которые будут
работать как X-клиенты.

%description static -l uk.UTF-8
X11-static містить статичні бібліотеки, необхідні для розробки
програм, які працюють як X-клієнти.

%package tools
Summary:	Various tools for XOrg X11
Summary(pl.UTF-8):	Różne narzędzia dla XOrg X11
Summary(ru.UTF-8):	Разнообразные утилиты для XOrg X11
Summary(uk.UTF-8):	Різноманітні утиліти для XOrg X11
Group:		X11
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	man-config
Provides:	XFree86-tools = %{epoch}:%{version}-%{release}
Obsoletes:	X11R6-contrib
Obsoletes:	XFree86-tools

%description tools
Various tools for X, including listres, xbiff, xedit, xeyes, xcalc,
xload and xman, among others.

If you're using X, you should install X11-tools. You will also need to
install the XOrg X11 package, the XOrg X11 package which corresponds
to your video card, some of the XOrg X11 fonts packages, the X11-setup
package and the X11-libs package.

Finally, if you are going to develop applications that run as X
clients, you will also need to install X11-devel.

This package contains all applications that used to be in
X11R6-contrib in older releases.

%description tools -l pl.UTF-8
Różne narzędzia dla X, w tym listres, xbiff, xedit, xeyes, xcalc,
xload, xman i inne.

Jeśli używasz Xów powinieneś zainstalować X11-tools. Będziesz również
musiał zainstalować pakiet XOrg X11, pakiet odpowiadający Twojej
karcie graficznej, jeden z pakietów z fontami, pakiet Xconfigurator
oraz X11-libs.

Wreszcie, jeśli zamierzasz tworzyć aplikacje, które działają jako
klienci X, będziesz musiał zainstalować również X11-devel.

Ten pakiet zawiera aplikacje, które były w X11R6-contrib w starszych
wersjach X.

%description tools -l ru.UTF-8
Разнообразные утилиты для X, включая listres, xbiff, xedit, xeyes,
xcalc, xload, xman и другие.

Если вы устанавливаете X Window System, вам надо установить X11-tools.
Также вам также необходимо установить такие пакеты: XOrg X11,
Xconfigurator, X11-xfs и X11-libs. Возможно, вам надо установить и
другие пакеты шрифтов XOrg X11.

Если вы собираетесь разрабатывать программы, работающие как X-клиенты,
вам также надо установить X11-devel.

Этот пакет содержит все программы, которые раньше включались в
X11R6-contrib.

%description tools -l uk.UTF-8
Різноманітні утиліти для X, включаючи listres, xbiff, xedit, xeyes,
xcalc, xload, xman та інші.

Якщо ви встановлюєте X Window System, вам необхідно встановити
X11-tools. Також треба встановити такі пакети: XOrg X11,
Xconfigurator, X11-xfs та X11-libs. Можливо, вам треба встановити й
інші пакети шрифтів XOrg X11.

Якщо ви збираєтесь розробляти програми, які працюють як X-клієнти, вам
також необхідно встановити X11-devel.

Цей пакет містить усі програми, які раніше входили до X11R6-contrib.

%package -n XcursorTheme-handhelds
Summary:	Cursors Theme "handhelds"
Summary(pl.UTF-8):	Motyw kursorów "handhelds"
Group:		Themes
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	XFree86-libs
Obsoletes:	XFree86-Xcursor-packs-handhelds

%description -n XcursorTheme-handhelds
Cursors theme "handhelds" for X11.

%description -n XcursorTheme-handhelds -l pl.UTF-8
Motyw kursorów "handhelds" dla X11.

%package -n XcursorTheme-redglass
Summary:	Cursors theme "redglass"
Summary(pl.UTF-8):	Motyw kursorów "redglass"
Group:		Themes
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	XFree86-libs
Obsoletes:	XFree86-Xcursor-packs-redglass

%description -n XcursorTheme-redglass
Cursors theme "redglass" for X11.

%description -n XcursorTheme-redglass -l pl.UTF-8
Motyw kursorów "redglass" dla X11.

%package -n XcursorTheme-whiteglass
Summary:	Cursors theme "whiteglass"
Summary(pl.UTF-8):	Motyw kursorów "whiteglass"
Group:		Themes
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	XFree86-libs
Obsoletes:	XFree86-Xcursor-packs-whiteglass

%description -n XcursorTheme-whiteglass
Cursors theme "whiteglass" for X11.

%description -n XcursorTheme-whiteglass -l pl.UTF-8
Motyw kursorów "whiteglass" dla X11.

%package imake
Summary:	C preprocessor interface to the make utility
Summary(pl.UTF-8):	Miedzymordzie do make oparte o preprocesor C
Group:		Development/Building
Provides:	imake = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-imake
Obsoletes:	imake

%description imake
Imake is used to generate Makefiles from a template, a set of cpp
macro functions, and a per-directory input file called an Imakefile.
This allows machine dependencies (such as compiler options, alternate
command names, and special make rules) to be kept separate from the
descriptions of the various items to be built.

%description imake -l pl.UTF-8
Imake jest używany do generowania plików Makefile na bazie szablonu,
zbioru makr preprocesora C oraz (dla każdego podkatalogu) pliku
wejściowego Imakefile. Pozwala to na oddzielenie informacji zależnych
od środowiska kompilacji (takich jak opcje kompilatora, alternatywne
nazwy komend i reguły specjalne) od opisu różnych elementów które mają
być kompilowane.

%package sessreg
Summary:	sessreg - manage utmp/wtmp entries for non-init clients
Summary(pl.UTF-8):	Program do zarządzania wpisami w utmp/wtmp
Group:		X11
Provides:	sessreg = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-sessreg
Obsoletes:	sessreg

%description sessreg
sessreg is a simple program for managing utmp/wtmp entries for xdm
sessions.

System V has a better interface to /var/run/utmp than BSD; it
dynamically allocates entries in the file, instead of writing them at
fixed positions indexed by position in /etc/ttys.

%description sessreg -l pl.UTF-8
sessreg jest prostym programem do zarządzania wpisami w utmp/wtmp dla
sesji xdm.

System V ma lepszy niż BSD interfejs do /var/run/utmp; dynamicznie
alokuje wpisy w pliku, zamiast zapisywania ich na ustalonych pozycjach
indeksowanych położeniem w /etc/ttys.

%package twm
Summary:	Tab Window Manager for the X Window System
Summary(pl.UTF-8):	Twm - podstawowy zarządca okien dla X Window System
Summary(ru.UTF-8):	Простой оконный менеджер
Summary(uk.UTF-8):	Простий віконний менеджер
Group:		X11/Window Managers
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	filesystem >= 2.0-1
Provides:	twm = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-twm
Obsoletes:	twm

%description twm
Twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointerdriven keyboard
focus, and user-specified key and pointer button bindings.

%description twm -l pl.UTF-8
Twm jest zarządcą okien dla X Window System. Daje belki tytułowe,
ramki okien, parę form zarządzania ikonami, definiowalne makra,
ustawianie focusu kliknięciem lub położeniem wskaźnika myszy,
definiowalne przypisania klawiszy i przycisków myszy.

%description twm -l ru.UTF-8
Простой компактний оконный менеджер.

%description twm -l uk.UTF-8
Простий компактний віконний менеджер.

%package xauth
Summary:	xauth - X authority file utility
Summary(pl.UTF-8):	xauth - narzędzie do plików X authority
Group:		X11
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	xauth = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-xauth
Obsoletes:	xauth

%description xauth
The xauth program is used to edit and display the authorization
information used in connecting to the X server. This program is
usually used to extract authorization records from one machine and
merge them in on another (as is the case when using remote logins or
granting access to other users).

%description xauth -l pl.UTF-8
Program xauth służy do edycji i wyświetlania informacji
autoryzacyjnych używanych przy łączeniu z X serwerem. Ten program
przeważnie jest używany do wyciągania rekordów autoryzacji z jednej
maszyny i dołączania ich na innej (w celu umożliwienia zdalnego
logowania lub udostępnienia innym użytkownikom).

%package xdm
Summary:	xdm - X Display Manager with support for XDMCP, host chooser
Summary(pl.UTF-8):	XDM - zarządca ekranów z obsługą XDMCP i wybieraniem hostów
Summary(ru.UTF-8):	Менеджер дисплея X
Summary(uk.UTF-8):	Менеджер дисплею X
Group:		X11
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-sessreg = %{epoch}:%{version}-%{release}
Requires:	/usr/X11R6/bin/sessreg
Requires:	pam >= 0.79.0
Requires:	rc-scripts
Provides:	XDM
Provides:	xdm = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-xdm
Obsoletes:	entrance
Obsoletes:	gdm
Obsoletes:	kdm
Obsoletes:	slim
Obsoletes:	wdm
Obsoletes:	xdm

%description xdm
Xdm manages a collection of X displays, which may be on the local host
or remote servers. The design of xdm was guided by the needs of X
terminals as well as the X Consortium standard XDMCP, the X Display
Manager Control Protocol.

%description xdm -l pl.UTF-8
Xdm zarządza zestawem ekranów X, które mogą być lokalne lub na
zdalnych serwerach. Został zaprojektowany zgodnie z potrzebami X
terminali oraz standardem X Consortium XDMCP.

%description xdm -l ru.UTF-8
Менеджер дисплея X.

%description xdm -l uk.UTF-8
Менеджер дисплею X.

%package xfs
Summary:	Font server for XOrg X11
Summary(pl.UTF-8):	Serwer fontów dla XOrg X11
Summary(ru.UTF-8):	Фонтсервер для X Window System
Summary(uk.UTF-8):	Фонтсервер для X Window System
Group:		X11
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	X11-fonts-base
Requires:	rc-scripts
Provides:	group(xfs)
Provides:	user(xfs)
Provides:	xfs = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-xfs
Obsoletes:	xfs
Obsoletes:	xfsft
Obsoletes:	xorg-x11-xfs

%description xfs
This is a font server for XOrg X11. You can serve fonts to other X
servers remotely with this package, and the remote system will be able
to use all fonts installed on the font server, even if they are not
installed on the remote computer.

%description xfs -l pl.UTF-8
Pakiet zawiera serwer fontów dla XOrg X11. Może udostępniać fonty dla
X serwerów lokalnych lub zdalnych.

%description xfs -l ru.UTF-8
X11-xfs содержит сервер шрифтов для XOrg X11. Xfs также может
предоставлять шрифты удаленным X-серверам. Удаленная система будет
способна использовать все шрифты, установленные на сервере шрифтов,
даже если они не установлены на удаленном компьютере.

Вы должны установить X11-xfs если вы устанавливаете X Window System.
Также вам придется установить следующие пакеты: XOrg X11, пакет(ы)
шрифтов XOrg X11, необходимые для вашей системы, Xconfigurator и
X11-libs.

%description xfs -l uk.UTF-8
X11-xfs містить сервер шрифтів для XOrg X11. Xfs також може надавати
шрифти віддаленим X-серверам. Віддалена система зможе використовувати
усі шрифти, які встановлені на сервері шрифтів, навіть якщо вони не
встановлені на віддаленому комп'ютері.

Ви повинні встановити X11-xfs якщо ви встановлюєте X Window System.
Також вам прийдеться встановити наступні пакети: XOrg X11, пакет(и)
шрифтів XOrg X11, необхідні для вашої системи, Xconfigurator та
X11-libs.

%prep
%setup -qc -a1 -a2 -a7
cd xc
%patch0 -p0
%patch64 -p1
%patch65 -p1
%patch33 -p0
%patch35 -p0
cd ..
%patch34 -p1
%patch1 -p1
%{?with_glide:%patch2 -p0}
%patch3 -p0
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p0
%patch14 -p0
%patch15 -p0
%patch16 -p0
%patch17 -p0
%patch18 -p0
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p0
%patch25 -p1
%patch26 -p0
%patch27 -p0
%patch28 -p1

rm -f xc/config/cf/host.def

%patch29 -p1
%patch30 -p0
%patch31 -p0
%patch32 -p0
%patch36 -p0
%patch50 -p1
%patch60 -p0
# FIXME
# %patch61 -p1
%patch62 -p1
%patch63 -p1

# FIXME, is this still needed?
# %patch69 -p0
# FIXME, is this still needed?
# %patch71 -p0
%{__patch} -d xc/programs/xkbcomp/symbols/pc < %{PATCH72}

%{?with_r300:%patch73 -p1}
%{?with_r300:%patch74 -p1}
# patch74 required patch73
%{?with_dualhead:%patch100 -p1}
%{?with_via_openchrome: bzip2 -dc %{SOURCE55} |tar -x --to-stdout | %{__patch} -p1 -s}


sed -i -e 's#krb5/##g' xc/lib/Xau/*.* xc/programs/xdm/greeter/*.* \
	xc/programs/xdm/*.* xc/programs/Xserver/os/*.*

%build
PWD=`pwd`
%{__make} -S -C xc World \
	FAST=1 \
	DEFAULT_OS_CPU_FROB=%{_target_cpu} \
	CC="%{__cc}" \
	BOOTSTRAPCFLAGS="%{rpmcflags}" \
	CCOPTIONS="%{rpmcflags}" \
	CXXOPTIONS="%{rpmcflags}" \
	CXXDEBUGFLAGS="" \
	CDEBUGFLAGS="" \
	FONTSDIR= \
	ICONDIR="%{_iconsdir}" \
	LINUXDIR="/dev/null" \
	TOP="$PWD/xc"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d,security/console.apps,sysconfig} \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11/fs \
	$RPM_BUILD_ROOT%{_appdefsdir}/{cs,da,de,es,fr,hu,it,ja,ko,nl,pl,pt,ru,sk,zh_CN.gb2312,zh_TW.big5} \
	$RPM_BUILD_ROOT%{_datadir}/misc \
	$RPM_BUILD_ROOT%{_sbindir} \
	$RPM_BUILD_ROOT/usr/{bin,include,lib} \
	$RPM_BUILD_ROOT/var/{log,lib/xkb} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_iconsdir},%{_pixmapsdir}/mini} \
	$RPM_BUILD_ROOT{%{_wmpropsdir},%{_themesdir}/{ThinIce,Metal,Industrial}} \
	$RPM_BUILD_ROOT%{_xsessdir} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}

PWD=`pwd`
%{__make} -C xc	install	install.man \
	DESTDIR="$RPM_BUILD_ROOT" \
	DOCDIR="%{_docdir}/%{name}-%{version}" \
	INSTBINFLAGS="-m 755" \
	INSTPGMFLAGS="-m 755" \
	RAWCPP="/lib/cpp" \
	BOOTSTRAPCFLAGS="%{rpmcflags}" \
	CCOPTIONS="%{rpmcflags}" \
	CXXOPTIONS="%{rpmcflags}" \
	CXXDEBUGFLAGS="" \
	CDEBUGFLAGS="" \
	FONTSDIR= \
	ICONDIR="%{_iconsdir}" \
	LINUXDIR="/dev/null" \
	TOP="$PWD/xc"

# fix pkgconfig path
if [ "%{_pkgconfigdir}" != "/usr/lib/pkgconfig" ] ; then
	mv $RPM_BUILD_ROOT/usr/lib/pkgconfig/* $RPM_BUILD_ROOT%{_pkgconfigdir}
fi

# setting default X
rm -f $RPM_BUILD_ROOT%{_bindir}/X
ln -sf Xorg $RPM_BUILD_ROOT%{_bindir}/X

# setting ghost X in /etc/X11 -- xf86config will fix this ...
ln -sf %{_bindir}/Xorg $RPM_BUILD_ROOT%{_sysconfdir}/X11/X

# add X11 links in /usr/bin, /usr/lib /usr/include
ln -sf %{_includedir}/X11 $RPM_BUILD_ROOT/usr/include/X11
ln -sf %{_libx11dir} $RPM_BUILD_ROOT/usr/lib/X11
ln -sf %{_bindir} $RPM_BUILD_ROOT/usr/bin/X11

# fix libGL*.so links
rm -f $RPM_BUILD_ROOT%{_libdir}/libGL*.so
ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
ln -sf libGLU.so.1 $RPM_BUILD_ROOT%{_libdir}/libGLU.so

# according to OpenGL ABI for Linux v1.0
# (http://oss.sgi.com/projects/ogl-sample/ABI/index.html)
# libGL.so.1, libGL.so, libGLU.so.1, libGL.so must be accessible in /usr
# libGL is already linked by XOrg X11 build, but libGLU not
ln -sf %{_libdir}/libGLU.so.1 $RPM_BUILD_ROOT/usr/%{_lib}/libGLU.so.1
ln -sf %{_libdir}/libGLU.so $RPM_BUILD_ROOT/usr/%{_lib}/libGLU.so

# move instead of symlinking
rm -f $RPM_BUILD_ROOT/usr/include/GL
mv -f $RPM_BUILD_ROOT%{_includedir}/GL $RPM_BUILD_ROOT/usr/include

# get the most current OpenGL extensions
cp -f %{SOURCE53} $RPM_BUILD_ROOT/usr/include/GL/glext.h

# don't include shared version due to Motif issues
rm -f $RPM_BUILD_ROOT%{_libdir}/libGLw.so*

# collect Xserver headers and make symlinks
for f in `cat %{SOURCE44}`; do
	install -D xc/${f} $RPM_BUILD_ROOT%{_includedir}/X11/Xserver/${f}
done
cd $RPM_BUILD_ROOT%{_includedir}/X11/Xserver
sh %{SOURCE45}
cd -

# set up PLD xdm config
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/{*Console,Xaccess,Xsession,Xsetup*}
install xdm-xinitrc-*/pixmaps/* $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/pixmaps
install xdm-xinitrc-*/{*Console,Xaccess,Xsession,Xsetup*} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm

install %{SOURCE8} $RPM_BUILD_ROOT/etc/pam.d/xdm
install %{SOURCE9} $RPM_BUILD_ROOT/etc/pam.d/xserver
install %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/xdm
install %{SOURCE11} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfs
install %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/X11/fs/config
install %{SOURCE13} $RPM_BUILD_ROOT%{_appdefsdir}/pl/XTerm

install %{SOURCE14} $RPM_BUILD_ROOT/etc/sysconfig/xdm
install %{SOURCE15} $RPM_BUILD_ROOT/etc/sysconfig/xfs

install %{SOURCE24} $RPM_BUILD_ROOT%{_wmpropsdir}/twm.desktop
install %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} %{SOURCE29} \
	%{SOURCE30} %{SOURCE31} %{SOURCE47} %{SOURCE48} %{SOURCE49} \
	$RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE34} %{SOURCE35} %{SOURCE36} %{SOURCE37} %{SOURCE38} \
	%{SOURCE39} %{SOURCE40} %{SOURCE41} %{SOURCE50} %{SOURCE51} \
	%{SOURCE52} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

bzip2 -dc %{SOURCE42} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# twm desktop file for gdm/kdm support
install %{SOURCE46} $RPM_BUILD_ROOT%{_xsessdir}/twm.desktop

:> $RPM_BUILD_ROOT/etc/security/console.apps/xserver
:> $RPM_BUILD_ROOT/etc/security/blacklist.xserver
:> $RPM_BUILD_ROOT/etc/security/blacklist.xdm

ln -sf %{_fontsdir} $RPM_BUILD_ROOT%{_libx11dir}/fonts

# do not duplicate xkbcomp program
rm -f $RPM_BUILD_ROOT%{_libx11dir}/xkb/xkbcomp
ln -sf %{_bindir}/xkbcomp $RPM_BUILD_ROOT%{_sysconfdir}/X11/xkb/xkbcomp

ln -sf %{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_libx11dir}/doc

rm -f $RPM_BUILD_ROOT%{_libx11dir}/config/host.def

:> $RPM_BUILD_ROOT%{_libx11dir}/config/host.def
:> $RPM_BUILD_ROOT%{_sysconfdir}/X11/xorg.conf

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html

# resolve conflict with man-pages
mv -f $RPM_BUILD_ROOT%{_mandir}/man4/{mouse.4,mouse-x.4}

# help rpm to detect deps
chmod 755 $RPM_BUILD_ROOT%{_libdir}/modules/dri/*.so

gzip -9nf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/*

# don't gzip README.* files, they are needed by XF86Setup
gunzip $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/README.*

install -d $RPM_BUILD_ROOT/etc/ld.so.conf.d
echo '%{_libdir}' > $RPM_BUILD_ROOT/etc/ld.so.conf.d/X11-%{_lib}.conf

chmod -R u+w $RPM_BUILD_ROOT

cp -a %{SOURCE54} $RPM_BUILD_ROOT%{_sysconfdir}/X11/XvMCConfig

%clean
rm -rf $RPM_BUILD_ROOT

#--- %post{un}, %preun, %trigger ----------

%post	DPS -p /sbin/ldconfig
%postun DPS -p /sbin/ldconfig

%post	OpenGL-libGL -p /sbin/ldconfig
%postun OpenGL-libGL -p /sbin/ldconfig

%post	OpenGL-libs -p /sbin/ldconfig
%postun OpenGL-libs -p /sbin/ldconfig

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%pre modules
if [ -d /etc/X11/xkb/geometry/hp ]; then
	rm -rf /etc/X11/xkb/geometry/hp
fi

%triggerpostun modules -- X11-modules < 4.0.2
if [ -d /usr/X11R6/lib/X11/xkb ]; then
	rm -rf /usr/X11R6/lib/X11/xkb
	ln -sf /etc/X11/xkb /usr/X11R6/lib/X11/xkb
fi

%triggerpostun libs -- X11-libs < 1:6.8.2-11.13
sed -i -e "/^%(echo %{_libdir} | sed -e 's,/,\\/,g')$/d" /etc/ld.so.conf

%post xdm
/sbin/chkconfig --add xdm
if [ -f /var/lock/subsys/xdm ]; then
	echo "Run \"/sbin/service xdm restart\" to restart xdm." >&2
	echo "WARNING: it will terminate all sessions opened from xdm!" >&2
else
	echo "Run \"/sbin/service xdm start\" to start xdm." >&2
fi

%preun xdm
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del xdm
	%service xdm stop
fi

%pre xfs
%groupadd -P %{name}-xfs -g 56 -r -f xfs
%useradd -P %{name}-xfs -u 56 -r -d /etc/X11/fs -s /bin/false -c "X Font Server" -g xfs xfs

%post xfs
/sbin/chkconfig --add xfs
%service xfs restart "font server"

%preun xfs
if [ "$1" = "0" ]; then
	%service xfs stop
	/sbin/chkconfig --del xfs
fi

%postun xfs
if [ "$1" = "0" ]; then
	%userremove xfs
	%groupremove xfs
fi

%triggerpostun xfs -- xfs
#if [ -s /etc/X11/fs/config.rpmsave ]; then
#	cp -f /etc/X11/fs/config.rpmsave /etc/X11/fs/config
#fi
%groupadd -P %{name}-xfs -g 56 -r -f xfs
%useradd -P %{name}-xfs -u 56 -r -d /etc/X11/fs -s /bin/false -c "X Font Server" -g xfs xfs
/sbin/chkconfig --add xfs
/sbin/service xfs start >&2

%triggerpostun Xserver -- XFree86-Xserver
if [ -s /etc/X11/XF86Config.rpmsave ]; then
	cp -f /etc/X11/XF86Config.rpmsave /etc/X11/xorg.conf
	sed -i -e "s/xfree86/xorg/g" /etc/X11/xorg.conf
fi

#--- %files --------------------------

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%doc %{_libx11dir}/doc

%{_appdefsdir}/UXTerm
%{_appdefsdir}/XCalc
%{_appdefsdir}/XCalc-color
%{_appdefsdir}/XClipboard
%{_appdefsdir}/XClock
%{_appdefsdir}/XClock-color
%{_appdefsdir}/XLoad
%{_appdefsdir}/XLogo
%{_appdefsdir}/XLogo-color
%{_appdefsdir}/XSm
%{_appdefsdir}/XTerm
%lang(pl) %{_appdefsdir}/pl/XTerm
%{_appdefsdir}/XTerm-color

%attr(755,root,root) %{_libx11dir}/lbxproxy
%attr(755,root,root) %{_libx11dir}/proxymngr
%attr(755,root,root) %{_libx11dir}/rstart
%attr(755,root,root) %{_libx11dir}/fonts
%attr(755,root,root) %{_libx11dir}/xinit
%attr(755,root,root) %{_libx11dir}/xsm

%dir /etc/X11/lbxproxy
/etc/X11/lbxproxy/*
%dir /etc/X11/proxymngr
/etc/X11/proxymngr/*
%dir /etc/X11/rstart
/etc/X11/rstart/config
%attr(755,root,root) /etc/X11/rstart/rstartd.real
%dir /etc/X11/rstart/commands
/etc/X11/rstart/commands/x
/etc/X11/rstart/commands/x11
%attr(755,root,root) /etc/X11/rstart/commands/*List*
%dir /etc/X11/rstart/commands/x11r6
%attr(755,root,root) /etc/X11/rstart/commands/x11r6/*
%dir /etc/X11/rstart/contexts
/etc/X11/rstart/contexts/*
%dir /etc/X11/xsm
/etc/X11/xsm/*

%dir %{_libx11dir}/x11perfcomp
%attr(755,root,root) %{_libx11dir}/x11perfcomp/*

%attr(755,root,root) %{_bindir}/Xmark
%attr(755,root,root) %{_bindir}/appres
%attr(755,root,root) %{_bindir}/atobm
%attr(755,root,root) %{_bindir}/bitmap
%attr(755,root,root) %{_bindir}/bmtoa
%attr(755,root,root) %{_bindir}/cxpm
%attr(755,root,root) %{_bindir}/dga
%attr(755,root,root) %{_bindir}/editres
%attr(755,root,root) %{_bindir}/gtf
%attr(755,root,root) %{_bindir}/iceauth
%attr(755,root,root) %{_bindir}/lbxproxy
%attr(755,root,root) %{_bindir}/lndir
%attr(755,root,root) %{_bindir}/luit
%attr(755,root,root) %{_bindir}/makeg
%attr(755,root,root) %{_bindir}/makestrs
%attr(755,root,root) %{_bindir}/mergelib
%attr(755,root,root) %{_bindir}/mkdirhier
%attr(755,root,root) %{_bindir}/mkhtmlindex
%attr(755,root,root) %{_bindir}/proxymngr
%attr(755,root,root) %{_bindir}/resize
%attr(755,root,root) %{_bindir}/revpath
%attr(755,root,root) %{_bindir}/rstart
%attr(755,root,root) %{_bindir}/rstartd
%attr(755,root,root) %{_bindir}/setxkbmap
%attr(755,root,root) %{_bindir}/showrgb
%attr(755,root,root) %{_bindir}/smproxy
%attr(755,root,root) %{_bindir}/startx
%attr(755,root,root) %{_bindir}/sxpm
%attr(755,root,root) %{_bindir}/uxterm
%attr(755,root,root) %{_bindir}/xcmsdb
%attr(755,root,root) %{_bindir}/xconsole
%attr(755,root,root) %{_bindir}/xcursorgen
%attr(755,root,root) %{_bindir}/xcutsel
%attr(755,root,root) %{_bindir}/xdpyinfo
%attr(755,root,root) %{_bindir}/xfindproxy
%attr(755,root,root) %{_bindir}/xfwp
%attr(755,root,root) %{_bindir}/xgamma
%attr(755,root,root) %{_bindir}/xhost
%attr(755,root,root) %{_bindir}/xinit
%attr(755,root,root) %{_bindir}/xkbbell
%attr(755,root,root) %{_bindir}/xkbevd
%attr(755,root,root) %{_bindir}/xkbprint
%attr(755,root,root) %{_bindir}/xkbvleds
%attr(755,root,root) %{_bindir}/xkbwatch
%attr(755,root,root) %{_bindir}/xlsatoms
%attr(755,root,root) %{_bindir}/xlsclients
%attr(755,root,root) %{_bindir}/xlsfonts
%attr(755,root,root) %{_bindir}/xmodmap
%attr(755,root,root) %{_bindir}/xon
%attr(755,root,root) %{_bindir}/xprop
%attr(755,root,root) %{_bindir}/xrandr
%attr(755,root,root) %{_bindir}/xrdb
%attr(755,root,root) %{_bindir}/xrefresh
%attr(755,root,root) %{_bindir}/xrx
%attr(755,root,root) %{_bindir}/xset
%attr(755,root,root) %{_bindir}/xsetmode
%attr(755,root,root) %{_bindir}/xsetpointer
%attr(755,root,root) %{_bindir}/xsetroot
%attr(755,root,root) %{_bindir}/xsm
%attr(755,root,root) %{_bindir}/xstdcmap
%attr(755,root,root) %{_bindir}/xterm
%attr(755,root,root) %{_bindir}/xvidtune
%attr(755,root,root) %{_bindir}/xvinfo
%attr(755,root,root) %{_bindir}/xwd
%attr(755,root,root) %{_bindir}/xwud

%{_includedir}/X11/bitmaps
%{_includedir}/X11/pixmaps

%{_desktopdir}/xconsole.desktop
%{_desktopdir}/xterm.desktop
%{_pixmapsdir}/xconsole.png
%{_pixmapsdir}/xlogo64.png
%{_pixmapsdir}/xterm.png

%{_appdefsdir}/Xvidtune

%{_mandir}/man1/Xmark.1*
%{_mandir}/man1/appres.1*
%{_mandir}/man1/atobm.1*
%{_mandir}/man1/bitmap.1*
%{_mandir}/man1/bmtoa.1*
%{_mandir}/man1/cxpm.1*
%{_mandir}/man1/dga.1*
%{_mandir}/man1/editres.1*
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/iceauth.1*
%{_mandir}/man1/lbxproxy.1*
%{_mandir}/man1/libxrx.1*
%{_mandir}/man1/lndir.1*
%{_mandir}/man1/luit.1x*
%{_mandir}/man1/makestrs.1*
%{_mandir}/man1/makeg.1*
%{_mandir}/man1/mergelib.1*
%{_mandir}/man1/mkdirhier.1*
%{_mandir}/man1/mkhtmlindex.1*
%{_mandir}/man1/proxymngr.1*
%{_mandir}/man1/resize.1*
%{_mandir}/man1/revpath.1*
%{_mandir}/man1/rstart.1*
%{_mandir}/man1/rstartd.1*
%{_mandir}/man1/setxkbmap.1*
%{_mandir}/man1/showrgb.1*
%{_mandir}/man1/smproxy.1*
%{_mandir}/man1/startx.1*
%{_mandir}/man1/sxpm.1*
%{_mandir}/man1/xcmsdb.1*
%{_mandir}/man1/xconsole.1*
%{_mandir}/man1/xcursorgen.1*
%{_mandir}/man1/xcutsel.1*
%{_mandir}/man1/xdpyinfo.1*
%{_mandir}/man1/xfindproxy.1*
%{_mandir}/man1/xfwp.1*
%{_mandir}/man1/xgamma.1*
%{_mandir}/man1/xhost.1*
%{_mandir}/man1/xinit.1*
%{_mandir}/man1/xkbevd.1*
%{_mandir}/man1/xkbprint.1*
%{_mandir}/man1/xlsatoms.1*
%{_mandir}/man1/xlsclients.1*
%{_mandir}/man1/xlsfonts.1*
%{_mandir}/man1/xmodmap.1*
%{_mandir}/man1/xprop.1*
%{_mandir}/man1/xrandr.1*
%{_mandir}/man1/xrdb.1*
%{_mandir}/man1/xrefresh.1*
%{_mandir}/man1/xrx.1*
%{_mandir}/man1/xset.1*
%{_mandir}/man1/xsetmode.1*
%{_mandir}/man1/xsetpointer.1*
%{_mandir}/man1/xsetroot.1*
%{_mandir}/man1/xsm.1*
%{_mandir}/man1/xstdcmap.1*
%{_mandir}/man1/xterm.1*
%{_mandir}/man1/xvidtune.1*
%{_mandir}/man1/xvinfo.1*
%{_mandir}/man1/xwd.1*
%{_mandir}/man1/xwud.1*
%{_mandir}/man1/xon.1*
%{_mandir}/man7/*

# not related to any packaged files
#%{_mandir}/man1/XDarwin.1*
#%{_mandir}/man1/dmxtodmx.1*
#%{_mandir}/man1/dumpkeymap.1*
#%{_mandir}/man1/ucs2any.1*
#%{_mandir}/man1/vdltodmx.1*
#%{_mandir}/man1/xdmxconfig.1*

%lang(it) %{_mandir}/it/man1/startx.1*
%lang(it) %{_mandir}/it/man1/xconsole.1*
%lang(it) %{_mandir}/it/man1/xinit.1*
%lang(it) %{_mandir}/it/man1/xsetpointer.1*

%lang(ko) %{_mandir}/ko/man1/xterm.1*

%lang(pl) %{_mandir}/pl/man1/lbxproxy.1*
%lang(pl) %{_mandir}/pl/man1/startx.1*
%lang(pl) %{_mandir}/pl/man1/xinit.1*
%lang(pl) %{_mandir}/pl/man1/xwd.1*

# to be separated
#%attr(755,root,root) %{_bindir}/fonttosfnt
%attr(755,root,root) %{_bindir}/mkfontdir
%attr(755,root,root) %{_bindir}/mkfontscale
#%{_mandir}/man1/fonttosfnt.1*
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/mkfontscale.1*

%files common
%defattr(644,root,root,755)
/usr/bin/X11
/usr/lib/X11
%dir %{_bindir}
%dir %{_libdir}
%if "%{_lib}" != "lib"
%dir %{_prefix}/lib
%endif
%dir %{_libx11dir}
%{_libx11dir}/rgb.txt

%files Xprint
%defattr(644,root,root,755)
%dir %{_sysconfdir}/X11/xserver/C
%dir %{_sysconfdir}/X11/xserver/C/print
%{_sysconfdir}/X11/xserver/C/print/*
%lang(en) %dir %{_sysconfdir}/X11/xserver/en_US
%lang(en) %dir %{_sysconfdir}/X11/xserver/en_US/print
%lang(en) %{_sysconfdir}/X11/xserver/en_US/print/*

%files DPS
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makepsres
%attr(755,root,root) %{_bindir}/pswrap
%attr(755,root,root) %{_bindir}/dpsinfo
%attr(755,root,root) %{_bindir}/dpsexec
%attr(755,root,root) %{_libdir}/libdps.so.*.*
%attr(755,root,root) %{_libdir}/libdpstk.so.*.*
%attr(755,root,root) %{_libdir}/libpsres.so.*.*
%{_mandir}/man1/makepsres.1*
%{_mandir}/man1/pswrap.1*
%{_mandir}/man1/dpsexec.1*
%{_mandir}/man1/dpsinfo.1*

%files DPS-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdps.so
%attr(755,root,root) %{_libdir}/libdpstk.so
%attr(755,root,root) %{_libdir}/libpsres.so
%{_includedir}/DPS

%files DPS-static
%defattr(644,root,root,755)
%{_libdir}/libdps.a
%{_libdir}/libdpstk.a
%{_libdir}/libpsres.a

%files OpenGL-core
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/extensions/libglx.so
%attr(755,root,root) %{_libdir}/modules/extensions/libGLcore.so

%files OpenGL-libGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %{_libdir}/libGL.so
# Linux OpenGL ABI compatibility symlinks
%attr(755,root,root) /usr/%{_lib}/libGL.so.1
%attr(755,root,root) /usr/%{_lib}/libGL.so

%files OpenGL-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glxinfo
%attr(755,root,root) %{_bindir}/glxgears
%attr(755,root,root) %{_libdir}/libGLU.so.*.*
# to be fixed: it contains unresolved symbols and would need -lXm
#%attr(755,root,root) %{_libdir}/libGLw.so.*.*
%attr(755,root,root) %{_libdir}/libOSMesa.so.*.*
# Linux OpenGL ABI compatibility symlink
%attr(755,root,root) /usr/%{_lib}/libGLU.so.1
%{_mandir}/man1/glxinfo.1*
%{_mandir}/man1/glxgears.1*

%files OpenGL-devel-base
%defattr(644,root,root,755)
/usr/include/GL/gl.h
/usr/include/GL/glx.h
/usr/include/GL/glext.h
/usr/include/GL/glxtokens.h

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLU.so
%attr(755,root,root) %{_libdir}/libOSMesa.so
# Linux OpenGL ABI compatibility symlink
%attr(755,root,root) /usr/%{_lib}/libGLU.so
%{_libdir}/libGLw.a
%dir /usr/include/GL
/usr/include/GL/GLwDrawA.h
/usr/include/GL/GLwDrawAP.h
/usr/include/GL/GLwMDrawA.h
/usr/include/GL/GLwMDrawAP.h
/usr/include/GL/glu.h
/usr/include/GL/glxext.h
/usr/include/GL/glxint.h
/usr/include/GL/glxmd.h
/usr/include/GL/glxproto.h
/usr/include/GL/osmesa.h
%{_mandir}/man3/gl[A-Z]*
%{_mandir}/man3/glu*
%{_mandir}/man3/GLw*

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libGL.a
%{_libdir}/libGLU.a
%{_libdir}/libOSMesa.a

%files Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*

%files Xprt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xprt
%{_mandir}/man1/Xprt.1*

%files Xserver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xorg
%attr(755,root,root) %{_bindir}/*dmx*
%attr(4755,root,root) %{_bindir}/Xwrapper
%attr(755,root,root) %{_bindir}/getconfig*
%attr(755,root,root) %{_sysconfdir}/X11/X
%attr(755,root,root) %{_bindir}/X
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/Xserver.1*
%{_mandir}/man1/*dmx*.1*
%{_mandir}/man1/getconfig.1*
%{_mandir}/man5/xorg.conf.5*
%{_mandir}/man5/getconfig.5*


%{_libx11dir}/Cards
%{_libx11dir}/Options
%{_libx11dir}/getconfig

%config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xorg.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/XvMCConfig
%attr(640,root,root) %config %verify(not md5 mtime size) /etc/pam.d/xserver
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver

%files Xvfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvfb
%{_mandir}/man1/Xvfb.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bdftopcf
%ifnarch ppc sparc sparc64 sparcv9
%attr(755,root,root) %{_bindir}/ioport
%endif
%attr(755,root,root) %{_bindir}/mmapr
%attr(755,root,root) %{_bindir}/mmapw
%attr(755,root,root) %{_bindir}/xcursor-config
%attr(755,root,root) %{_bindir}/xft-config
%attr(755,root,root) %{_libdir}/libFS.so
%attr(755,root,root) %{_libdir}/lib*XvMC*.so
%attr(755,root,root) %{_libdir}/libICE.so
%attr(755,root,root) %{_libdir}/libSM.so
%attr(755,root,root) %{_libdir}/libX11.so
%attr(755,root,root) %{_libdir}/libXRes.so
%attr(755,root,root) %{_libdir}/libXTrap.so
%attr(755,root,root) %{_libdir}/libXau.so
%attr(755,root,root) %{_libdir}/libXaw.so
%attr(755,root,root) %{_libdir}/libXcomposite.so
%attr(755,root,root) %{_libdir}/libXcursor.so
%attr(755,root,root) %{_libdir}/libXdamage.so
%attr(755,root,root) %{_libdir}/libXdmcp.so
%attr(755,root,root) %{_libdir}/libXevie.so
%attr(755,root,root) %{_libdir}/libXext.so
%attr(755,root,root) %{_libdir}/libXfixes.so
%attr(755,root,root) %{_libdir}/libXfont.so
%attr(755,root,root) %{_libdir}/libXft.so
%attr(755,root,root) %{_libdir}/libXi.so
%attr(755,root,root) %{_libdir}/libXinerama.so
%attr(755,root,root) %{_libdir}/libXmu.so
%attr(755,root,root) %{_libdir}/libXmuu.so
%attr(755,root,root) %{_libdir}/libXp.so
%attr(755,root,root) %{_libdir}/libXpm.so
%attr(755,root,root) %{_libdir}/libXrandr.so
%attr(755,root,root) %{_libdir}/libXrender.so
%attr(755,root,root) %{_libdir}/libXss.so
%attr(755,root,root) %{_libdir}/libXt.so
%attr(755,root,root) %{_libdir}/libXtst.so
%attr(755,root,root) %{_libdir}/libXv.so
%attr(755,root,root) %{_libdir}/libXxf86dga.so
%attr(755,root,root) %{_libdir}/libXxf86misc.so
%attr(755,root,root) %{_libdir}/libXxf86rush.so
%attr(755,root,root) %{_libdir}/libXxf86vm.so
%attr(755,root,root) %{_libdir}/libfontenc.so
%attr(755,root,root) %{_libdir}/libxkbfile.so
%attr(755,root,root) %{_libdir}/libxkbui.so
%attr(755,root,root) %{_libdir}/libxrx*.so
%{_libdir}/libXprintAppUtil.a
%{_libdir}/libXprintUtil.a
%{_libdir}/libdmx.a
%{_libdir}/libfntstubs.a
%{_libdir}/liboldX.a
%{_libdir}/libxf86config.a
%{_includedir}/X11/*.h
%{_includedir}/X11/ICE
%{_includedir}/X11/PM
%{_includedir}/X11/SM
%{_includedir}/X11/Xaw
%{_includedir}/X11/Xcursor
%{_includedir}/X11/Xft
%{_includedir}/X11/Xmu
%{_includedir}/X11/XprintAppUtil
%{_includedir}/X11/XprintUtil
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/*.h
%{_includedir}/X11/fonts
%{_includedir}/xf86*.h
%{_libx11dir}/config
%{_mandir}/man1/bdftopcf.1*
%{_mandir}/man1/xft-config.1*
%{_mandir}/man3/[A-FH-Zl]*
%{_pkgconfigdir}/xcomposite.pc
%{_pkgconfigdir}/xcursor.pc
%{_pkgconfigdir}/xdamage.pc
%{_pkgconfigdir}/xevie.pc
%{_pkgconfigdir}/xfixes.pc
%{_pkgconfigdir}/xft.pc
%{_pkgconfigdir}/xrender.pc

%files Xserver-devel
%defattr(644,root,root,755)
%{_includedir}/X11/Xserver

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664}
%files driver-apm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/apm_drv.so
%{_mandir}/man4/apm.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664}
%files driver-ark
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/ark_drv.so
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} mips ppc arm
%files driver-chips
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/chips_drv.so
%{_mandir}/man4/chips.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} alpha
%files driver-cirrus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/cirrus_*.so
%{_mandir}/man4/cirrus.4*
%endif

%ifarch %{ix86} ia64 %{x8664}
%files driver-cyrix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/cyrix_drv.so
%{_mandir}/man4/cyrix.4*
%endif

%ifarch %{ix86} ia64 %{x8664} alpha sparc sparc64 sparcv9 mips ppc arm superh
%files driver-fbdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/fbdev_drv.so
%{_mandir}/man4/fbdev.4*
%endif

%ifarch %{ix86} ia64
%if %{with glide}
%files driver-glide
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/glide_drv.so
%{_mandir}/man4/glide.4*
%endif
%endif

%files driver-glint
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/glint_drv.so
%{_mandir}/man4/glint.4*

%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
#%files driver-glint-dri
#%attr(755,root,root) %{_libdir}/modules/dri/gamma_dri.so
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664}
%files driver-i128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i128_drv.so
%{_mandir}/man4/i128.4*
%endif

%files driver-i2c
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/multimedia/bt*.so
%attr(755,root,root) %{_libdir}/modules/multimedia/fi*.so
%attr(755,root,root) %{_libdir}/modules/multimedia/tda*.so
%attr(755,root,root) %{_libdir}/modules/multimedia/msp*.so
%attr(755,root,root) %{_libdir}/modules/multimedia/uda*.so

# Devel: sparc sparc64
%ifarch %{ix86} ia64
%files driver-i740
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i740_drv.so
%{_mandir}/man4/i740.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664}
%files driver-i810
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i810_drv.so
%{_mandir}/man4/i810.4*

%files driver-i810-dri
%ifarch %{ix86} ia64
%attr(755,root,root) %{_libdir}/modules/dri/i810_dri.so
%endif
%attr(755,root,root) %{_libdir}/modules/dri/i915_dri.so
%endif

# Devel: %{ix86} sparc sparc64 ppc %{x8664}
%if 0
%files driver-imstt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/imstt_drv.so
%{_mandir}/man4/imstt.4*
%endif

%ifarch %{ix86} ia64 %{x8664} sparc sparc64 sparcv9 mips alpha ppc arm
%files driver-mga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/mga_drv.so
%{_mandir}/man4/mga.4*

%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
%files driver-mga-dri
%attr(755,root,root) %{_libdir}/modules/dri/mga_dri.so
%endif
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664}
%files driver-neomagic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/neomagic_drv.so
%{_mandir}/man4/neomagic.4*
%endif

# Devel: %{ix86} sparc sparc64 %{x8664}
%ifarch mips
%files driver-newport
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/newport_drv.so
%{_mandir}/man4/newport.4*
%endif

%ifarch %{ix86}
%files driver-nsc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/nsc_drv.so
%{_mandir}/man4/nsc.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} mips alpha arm ppc
%files driver-nv
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/nv_drv.so
%attr(755,root,root) %{_libdir}/modules/drivers/riva128.so
%{_mandir}/man4/nv.4*
%endif

%files driver-ati
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/ati*_drv.so
%attr(755,root,root) %{_libdir}/modules/multimedia/theatre*_drv.so

%files driver-r128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/r128*_drv.so
%{_mandir}/man4/r128.4*

%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
%files driver-r128-dri
%attr(755,root,root) %{_libdir}/modules/dri/r128_dri.so
%endif

%files driver-radeon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/radeon*_drv.so
%{_mandir}/man4/radeon.4*

%ifarch %{ix86} ia64 %{x8664} alpha ppc arm
%files driver-radeon-dri
%attr(755,root,root) %{_libdir}/modules/dri/radeon_dri.so
%attr(755,root,root) %{_libdir}/modules/dri/r200_dri.so
%if %{with r300}
%attr(755,root,root) %{_libdir}/modules/dri/r300_dri.so
%endif
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} alpha
%files driver-rendition
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/rendition_drv.so
%{_libdir}/modules/*.uc
%{_mandir}/man4/rendition.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} mips alpha ppc arm
%files driver-s3virge
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/s3virge_drv.so
%{_mandir}/man4/s3virge.4*
%endif

%ifarch %{ix86} ia64 %{x8664} mips alpha ppc arm
%files driver-s3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/s3_drv.so
#%%{_mandir}/man4/s3.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} mips alpha ppc arm
%files driver-savage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/savage_drv.so
%{_mandir}/man4/savage.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} alpha
%files driver-siliconmotion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/siliconmotion_drv.so
%{_mandir}/man4/siliconmotion.4*
%endif

%ifarch %{ix86} ia64 %{x8664} mips ppc arm
%files driver-sis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sis_drv.so
%{_mandir}/man4/sis.4*

%ifarch %{ix86} ia64
%files driver-sis-dri
%attr(755,root,root) %{_libdir}/modules/dri/sis_dri.so
%endif
%endif

%files driver-sisusb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sisusb_drv.so
%{_mandir}/man4/sisusb.4*

%ifarch sparc sparc64 sparcv9
%files driver-sunbw2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunbw2_drv.so
%{_mandir}/man4/sunbw2.4*
%endif

%ifarch sparc sparc64 sparcv9
%files driver-suncg14
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg14_drv.so
%{_mandir}/man4/suncg14.4*
%endif

%ifarch sparc sparc64 sparcv9
%files driver-suncg3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg3_drv.so
%{_mandir}/man4/suncg3.4*
%endif

%ifarch sparc sparc64 sparcv9
%files driver-suncg6
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg6_drv.so
%{_mandir}/man4/suncg6.4*
%endif

%ifarch sparc sparc64 sparcv9
%files driver-sunffb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunffb_drv.so
# Devel: %{ix86} ia64 (for fun?)
%attr(755,root,root) %{_libdir}/modules/dri/ffb_dri.so
%{_mandir}/man4/sunffb.4*
%endif

%ifarch sparc sparc64 sparcv9
%files driver-sunleo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunleo_drv.so
%{_mandir}/man4/sunleo.4*
%endif

%ifarch sparc sparc64 sparcv9
%files driver-suntcx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suntcx_drv.so
%{_mandir}/man4/suntcx.4*
%endif

%ifarch %{ix86} ia64 %{x8664} sparc sparc64 sparcv9 mips alpha arm ppc
%files driver-tdfx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tdfx_drv.so
%{_mandir}/man4/tdfx.4*

%ifarch %{ix86} ia64 alpha arm
%files driver-tdfx-dri
%attr(755,root,root) %{_libdir}/modules/dri/tdfx_dri.so
%endif
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} alpha
%files driver-tga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tga_drv.so
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64 %{x8664} mips ppc arm
%files driver-trident
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/trident_drv.so
%{_mandir}/man4/trident.4*
%endif

%ifarch %{ix86} ia64 %{x8664}
%files driver-tseng
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tseng_drv.so
%{_mandir}/man4/tseng.4*
%endif

%ifarch %{ix86} ia64
%files driver-via
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/via_drv.so
%ifarch %{ix86}
%attr(755,root,root) %{_libdir}/modules/dri/unichrome_dri.so
%endif
%{_mandir}/man4/via.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} ia64
%files driver-vmware
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.4*
%endif

%files libs
%defattr(644,root,root,755)
/etc/ld.so.conf.d/*.conf
%dir %{_themesdir}/ThinIce
%dir %{_themesdir}/Metal
%dir %{_themesdir}/Industrial
%{_libx11dir}/XErrorDB
%{_libx11dir}/XKeysymDB
%dir %{_appdefsdir}
%lang(cs) %dir %{_appdefsdir}/cs
%lang(da) %dir %{_appdefsdir}/da
%lang(de) %dir %{_appdefsdir}/de
%lang(es) %dir %{_appdefsdir}/es
%lang(fr) %dir %{_appdefsdir}/fr
%lang(hu) %dir %{_appdefsdir}/hu
%lang(it) %dir %{_appdefsdir}/it
%lang(ja) %dir %{_appdefsdir}/ja
%lang(ko) %dir %{_appdefsdir}/ko
%lang(nl) %dir %{_appdefsdir}/nl
%lang(pl) %dir %{_appdefsdir}/pl
%lang(pt) %dir %{_appdefsdir}/pt
%lang(ru) %dir %{_appdefsdir}/ru
%lang(sk) %dir %{_appdefsdir}/sk
%lang(zh_CN) %dir %{_appdefsdir}/zh_CN.gb2312
%lang(zh_TW) %dir %{_appdefsdir}/zh_TW.big5
%dir %{_libx11dir}/locale
%{_libx11dir}/locale/[!l]*
%{_libx11dir}/locale/locale.*
%dir %{_libx11dir}/locale/%{_lib}
%dir %{_libx11dir}/locale/%{_lib}/common
%attr(755,root,root) %{_libx11dir}/locale/%{_lib}/common/*.so*
%dir %{_includedir}
%dir %{_includedir}/X11
/usr/include/X11
%dir %{_sbindir}
%dir %{_datadir}/misc
%dir %{_pixmapsdir}/mini
%attr(755,root,root) %{_libdir}/libFS.so.*.*
%attr(755,root,root) %{_libdir}/lib*XvMC*.so.*.*
%attr(755,root,root) %{_libdir}/libICE.so.*.*
%attr(755,root,root) %{_libdir}/libSM.so.*.*
%attr(755,root,root) %{_libdir}/libX11.so.*.*
%attr(755,root,root) %{_libdir}/libXRes.so.*.*
%attr(755,root,root) %{_libdir}/libXTrap.so.*.*
%attr(755,root,root) %{_libdir}/libXau.so.*.*
%attr(755,root,root) %{_libdir}/libXaw.so.6.*
%attr(755,root,root) %{_libdir}/libXaw.so.7.*
%attr(755,root,root) %{_libdir}/libXaw.so.8.*
%attr(755,root,root) %{_libdir}/libXcomposite.so.*.*
%attr(755,root,root) %{_libdir}/libXcursor.so.*.*.*
%attr(755,root,root) %{_libdir}/libXdamage.so.*.*
%attr(755,root,root) %{_libdir}/libXdmcp.so.*.*
%attr(755,root,root) %{_libdir}/libXevie.so.*.*
%attr(755,root,root) %{_libdir}/libXext.so.*.*
%attr(755,root,root) %{_libdir}/libXfixes.so.*.*
%attr(755,root,root) %{_libdir}/libXfont.so.*.*
%attr(755,root,root) %{_libdir}/libXft.so.1.*
%attr(755,root,root) %{_libdir}/libXft.so.2.*.*
%attr(755,root,root) %{_libdir}/libXi.so.*.*
%attr(755,root,root) %{_libdir}/libXinerama.so.*.*
%attr(755,root,root) %{_libdir}/libXmu.so.*.*
%attr(755,root,root) %{_libdir}/libXmuu.so.*.*
%attr(755,root,root) %{_libdir}/libXp.so.*.*
%attr(755,root,root) %{_libdir}/libXpm.so.*.*
%attr(755,root,root) %{_libdir}/libXrandr.so.*.*
%attr(755,root,root) %{_libdir}/libXrender.so.*.*.*
%attr(755,root,root) %{_libdir}/libXss.so.*.*
%attr(755,root,root) %{_libdir}/libXt.so.*.*
%attr(755,root,root) %{_libdir}/libXtst.so.*.*
%attr(755,root,root) %{_libdir}/libXv.so.*.*
%attr(755,root,root) %{_libdir}/libXxf86dga.so.*.*
%attr(755,root,root) %{_libdir}/libXxf86misc.so.*.*
%attr(755,root,root) %{_libdir}/libXxf86rush.so.*.*
%attr(755,root,root) %{_libdir}/libXxf86vm.so.*.*
%attr(755,root,root) %{_libdir}/libfontenc.so.*.*
%attr(755,root,root) %{_libdir}/libxkbfile.so.*.*
%attr(755,root,root) %{_libdir}/libxkbui.so.*.*
%attr(755,root,root) %{_libdir}/libxrx*.so.*.*

%files modules
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xkbcomp
%{_libx11dir}/xkb
%{_sysconfdir}/X11/xkb
/var/lib/xkb
%dir %{_libdir}/modules
%dir %{_libdir}/modules/dri
%dir %{_libdir}/modules/drivers
%attr(755,root,root) %{_libdir}/modules/*.so
%attr(755,root,root) %{_libdir}/modules/drivers/v4l_drv.so
%ifarch %{ix86} ia64 %{x8664} sparc sparc64 alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/drivers/vga_drv.so
%endif
%ifarch %{ix86} ia64 %{x8664} sparc sparc64
%attr(755,root,root) %{_libdir}/modules/drivers/vesa_drv.so
%endif
%dir %{_libdir}/modules/extensions
%dir %{_libdir}/modules/multimedia
%attr(755,root,root) %{_libdir}/modules/extensions/libdbe.so
%attr(755,root,root) %{_libdir}/modules/extensions/libdri.so
%attr(755,root,root) %{_libdir}/modules/extensions/libextmod.so
%attr(755,root,root) %{_libdir}/modules/extensions/librecord.so
%attr(755,root,root) %{_libdir}/modules/extensions/libxtrap.so
%attr(755,root,root) %{_libdir}/modules/fonts
%attr(755,root,root) %{_libdir}/modules/input
%attr(755,root,root) %{_libdir}/modules/linux
%attr(755,root,root) %{_libx11dir}/xserver
%dir /etc/X11/xserver
/etc/X11/xserver/SecurityPolicy
#%%{_mandir}/man1/xtr*
%{_mandir}/man1/xkbcomp.1*
%{_mandir}/man4/aiptek.4*
%{_mandir}/man4/citron.4*
%{_mandir}/man4/dmc.4*
%{_mandir}/man4/dynapro.4*
%{_mandir}/man4/elographics.4*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man4/fpit.4*
%{_mandir}/man4/js_x.4*
%{_mandir}/man4/kbd.4*
%{_mandir}/man4/keyboard.4*
%{_mandir}/man4/microtouch.4*
%{_mandir}/man4/mouse-x.4*
%{_mandir}/man4/mutouch.4*
%{_mandir}/man4/palmax.4*
%{_mandir}/man4/penmount.4*
%{_mandir}/man4/tek4957.4*
%{_mandir}/man4/ur98.4*
%{_mandir}/man4/v4l.4*
%ifarch %{ix86} ia64 %{x8664} sparc sparc64 sparcv9 alpha ppc arm
%{_mandir}/man4/vga.4*
%endif
%ifarch %{ix86} ia64 %{x8664} sparc sparc64 sparcv9
%{_mandir}/man4/vesa.4*
%endif
%{_mandir}/man4/void.4*
%{_mandir}/man4/wacom.4*

%files setup
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcitweak
%attr(755,root,root) %{_bindir}/scanpci
%attr(755,root,root) %{_bindir}/xorgcfg
%attr(755,root,root) %{_bindir}/xorgconfig
%{_appdefsdir}/XOrgCfg
%{_mandir}/man1/pcitweak.1*
%{_mandir}/man1/scanpci.1*
%{_mandir}/man1/xorgcfg.1*
%{_mandir}/man1/xorgconfig.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libFS.a
%{_libdir}/lib*XvMC*.a
%{_libdir}/libICE.a
%{_libdir}/libSM.a
%{_libdir}/libX11.a
%{_libdir}/libXRes.a
%{_libdir}/libXTrap.a
%{_libdir}/libXau.a
%{_libdir}/libXaw.a
%{_libdir}/libXcomposite.a
%{_libdir}/libXcursor.a
%{_libdir}/libXdamage.a
%{_libdir}/libXdmcp.a
%{_libdir}/libXevie.a
%{_libdir}/libXext.a
%{_libdir}/libXfixes.a
%{_libdir}/libXfont.a
%{_libdir}/libXft.a
%{_libdir}/libXi.a
%{_libdir}/libXinerama.a
%{_libdir}/libXmu.a
%{_libdir}/libXmuu.a
%{_libdir}/libXp.a
%{_libdir}/libXpm.a
%{_libdir}/libXrandr.a
%{_libdir}/libXrender.a
%{_libdir}/libXss.a
%{_libdir}/libXt.a
%{_libdir}/libXtst.a
%{_libdir}/libXv.a
%{_libdir}/libXxf86dga.a
%{_libdir}/libXxf86misc.a
%{_libdir}/libXxf86rush.a
%{_libdir}/libXxf86vm.a
%{_libdir}/libfontenc.a
%{_libdir}/libxkbfile.a
%{_libdir}/libxkbui.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/beforelight
%attr(755,root,root) %{_bindir}/ico
%attr(755,root,root) %{_bindir}/listres
%attr(755,root,root) %{_bindir}/oclock
%attr(755,root,root) %{_bindir}/rman
%attr(755,root,root) %{_bindir}/showfont
%attr(755,root,root) %{_bindir}/texteroids
%attr(755,root,root) %{_bindir}/viewres
%attr(755,root,root) %{_bindir}/x11perf
%attr(755,root,root) %{_bindir}/x11perfcomp
%attr(755,root,root) %{_bindir}/xbiff
%attr(755,root,root) %{_bindir}/xcalc
%attr(755,root,root) %{_bindir}/xclipboard
%attr(755,root,root) %{_bindir}/xclock
%attr(755,root,root) %{_bindir}/xditview
%attr(755,root,root) %{_bindir}/xdbedizzy
%attr(755,root,root) %{_bindir}/xdpr
%attr(755,root,root) %{_bindir}/xdriinfo
%attr(755,root,root) %{_bindir}/xedit
%attr(755,root,root) %{_bindir}/xev
%attr(755,root,root) %{_bindir}/xeyes
%attr(755,root,root) %{_bindir}/xfd
%attr(755,root,root) %{_bindir}/xfontsel
%attr(755,root,root) %{_bindir}/xgc
%attr(755,root,root) %{_bindir}/xkill
%attr(755,root,root) %{_bindir}/xload
%attr(755,root,root) %{_bindir}/xlogo
%attr(755,root,root) %{_bindir}/xmag
%attr(755,root,root) %{_bindir}/xman
%attr(755,root,root) %{_bindir}/xmessage
%attr(755,root,root) %{_bindir}/xmh
%attr(755,root,root) %{_bindir}/xmore
%attr(755,root,root) %{_bindir}/xphelloworld
%attr(755,root,root) %{_bindir}/xplsprinters
%attr(755,root,root) %{_bindir}/xpr
%attr(755,root,root) %{_bindir}/xprehashprinterlist
%attr(755,root,root) %{_bindir}/xpsimplehelloworld
%attr(755,root,root) %{_bindir}/xpxthelloworld
%attr(755,root,root) %{_bindir}/xtrap*
%attr(755,root,root) %{_bindir}/xwininfo
%{_libx11dir}/xedit
%{_libx11dir}/xman.help
%{_mandir}/man1/beforelight.1*
%{_mandir}/man1/ico.1*
%{_mandir}/man1/listres.1*
%{_mandir}/man1/oclock.1*
%{_mandir}/man1/rman.1*
%{_mandir}/man1/showfont.1*
%{_mandir}/man1/texteroids.1*
%{_mandir}/man1/viewres.1*
%{_mandir}/man1/x11perf.1*
%{_mandir}/man1/x11perfcomp.1*
%{_mandir}/man1/xbiff.1*
%{_mandir}/man1/xcalc.1*
%{_mandir}/man1/xclipboard.1*
%{_mandir}/man1/xclock.1*
%{_mandir}/man1/xditview.1*
%{_mandir}/man1/xdbedizzy.1*
%{_mandir}/man1/xdpr.1*
%{_mandir}/man1/xdriinfo.1*
%{_mandir}/man1/xmore.1*
%{_mandir}/man1/xedit.1*
%{_mandir}/man1/xev.1*
%{_mandir}/man1/xeyes.1*
%{_mandir}/man1/xfd.1*
%{_mandir}/man1/xfontsel.1*
%{_mandir}/man1/xgc.1*
%{_mandir}/man1/xkill.1*
%{_mandir}/man1/xload.1*
%{_mandir}/man1/xlogo.1*
%{_mandir}/man1/xmag.1*
%{_mandir}/man1/xman.1*
%{_mandir}/man1/xmessage.1*
%{_mandir}/man1/xmh.1*
%{_mandir}/man1/xphelloworld.1*
%{_mandir}/man1/xplsprinters.1*
%{_mandir}/man1/xpr.1*
%{_mandir}/man1/xprehashprinterlist.1*
%{_mandir}/man1/xpsimplehelloworld.1*
%{_mandir}/man1/xpxthelloworld.1*
%{_mandir}/man1/xtrap*
%{_mandir}/man1/xwininfo.1*

%lang(it) %{_mandir}/it/man1/xload.1*

%lang(pl) %{_mandir}/pl/man1/rman.1*

%{_appdefsdir}/Beforelight
%{_appdefsdir}/Bitmap
%{_appdefsdir}/Bitmap-color
%{_appdefsdir}/Clock-color
%{_appdefsdir}/Editres
%{_appdefsdir}/Editres-color
%{_appdefsdir}/Viewres
%{_appdefsdir}/XConsole
%{_appdefsdir}/XFontSel
%{_appdefsdir}/XMore
%{_appdefsdir}/Xditview
%{_appdefsdir}/Xditview-chrtr
%{_appdefsdir}/Xedit
%{_appdefsdir}/Xedit-color
%{_appdefsdir}/Xfd
%{_appdefsdir}/Xgc
%{_appdefsdir}/Xmag
%{_appdefsdir}/Xman
%{_appdefsdir}/Xmessage
%{_appdefsdir}/Xmessage-color
%{_appdefsdir}/Xmh

%{_desktopdir}/oclock.desktop
%{_desktopdir}/xcalc.desktop
%{_desktopdir}/xclipboard.desktop
%{_desktopdir}/xclock.desktop
%{_desktopdir}/xedit.desktop
%{_desktopdir}/xeyes.desktop
%{_desktopdir}/xload.desktop
%{_desktopdir}/xmag.desktop
%{_pixmapsdir}/oclock.png
%{_pixmapsdir}/xcalc.png
%{_pixmapsdir}/xclipboard.png
%{_pixmapsdir}/xclock.png
%{_pixmapsdir}/xedit.png
%{_pixmapsdir}/xeyes.png
%{_pixmapsdir}/xload.png
%{_pixmapsdir}/xmag.png

%files -n XcursorTheme-handhelds
%defattr(644,root,root,755)
%{_iconsdir}/handhelds

%files -n XcursorTheme-redglass
%defattr(644,root,root,755)
%{_iconsdir}/redglass

%files -n XcursorTheme-whiteglass
%defattr(644,root,root,755)
%{_iconsdir}/whiteglass

%files imake
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ccmakedep
%attr(755,root,root) %{_bindir}/cleanlinks
%attr(755,root,root) %{_bindir}/gccmakedep
%attr(755,root,root) %{_bindir}/imake
%attr(755,root,root) %{_bindir}/makedepend
%attr(755,root,root) %{_bindir}/xmkmf

%{_mandir}/man1/imake.1*
%{_mandir}/man1/ccmakedep.1*
%{_mandir}/man1/cleanlinks.1*
%{_mandir}/man1/gccmakedep.1*
%{_mandir}/man1/makedepend.1*
%{_mandir}/man1/xmkmf.1*

%files sessreg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sessreg
%{_mandir}/man1/sessreg.1*

%files twm
%defattr(644,root,root,755)
%{_wmpropsdir}/twm.desktop
%{_xsessdir}/twm.desktop
%attr(755,root,root) %{_bindir}/twm
%dir %{_sysconfdir}/X11/twm
%config %{_sysconfdir}/X11/twm/system.twmrc
%attr(755,root,root) %{_libx11dir}/twm
%{_mandir}/man1/twm.1*

%files xauth
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xauth*
%{_mandir}/man1/xauth.1*

%files xdm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xdm
%attr(754,root,root) /etc/rc.d/init.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/xdm
/var/lib/xdm

%{_appdefsdir}/Chooser

%attr(755,root,root) %{_libx11dir}/xdm
%attr(755,root,root) %{_bindir}/xdm
%attr(755,root,root) %{_bindir}/chooser
%{_mandir}/man1/xdm.1*

%dir %{_sysconfdir}/X11/xdm
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xdm/GiveConsole
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xdm/TakeConsole
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xdm/Xsession
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xdm/Xsetup_0
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xdm/Xwilling
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xdm/Xaccess
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xdm/Xresources
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xdm/Xservers
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xdm/xdm-config
%{_sysconfdir}/X11/xdm/pixmaps
%{_sysconfdir}/X11/xdm/authdir

%files xfs
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/xfs
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/xfs
%dir %{_sysconfdir}/X11/fs
%attr(755,root,root) %{_libx11dir}/fs
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/fs/config

%attr(755,root,root) %{_bindir}/xfs
%attr(755,root,root) %{_bindir}/fslsfonts
%attr(755,root,root) %{_bindir}/fstobdf
%attr(755,root,root) %{_bindir}/mkcfm
%attr(755,root,root) %{_bindir}/xfsinfo

%{_mandir}/man1/xfs.1*
%{_mandir}/man1/fslsfonts.1*
%{_mandir}/man1/fstobdf.1*
%{_mandir}/man1/mkcfm.1*
%{_mandir}/man1/xfsinfo.1*
