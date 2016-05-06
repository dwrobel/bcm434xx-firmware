#debug packages make no sense!
%global debug_package %{nil}
#no stripping required either
%global __os_install_post %{nil}

%global snap_date	20160506
%global commit_long	54bab3d6a6d43239c71d26464e6e10e5067ffea7
%global commit_short	%(c=%{commit_long}; echo ${c:0:7})

Name:       bcm43438-firmware
Version:    %{snap_date}
Release:    1.%{commit_short}%{?dist}
Summary:    Binary firmware for Broadcom BCM43438 SDIO module
Group:      System Environment/Kernel
License:    Redistributable, no modification permitted
URL:        https://github.com/RPi-Distro/firmware-nonfree
Source0:    https://github.com/RPi-Distro/firmware-nonfree/raw/%{commit_long}/brcm80211/brcm/brcmfmac43430-sdio.bin
Source1:    https://github.com/RPi-Distro/firmware-nonfree/raw/%{commit_long}/brcm80211/brcm/brcmfmac43430-sdio.txt
Source2:    https://github.com/RPi-Distro/firmware-nonfree/raw/%{commit_long}/brcm80211/LICENSE
Source3:    https://github.com/OpenELEC/misc-firmware/raw/master/firmware/brcm/BCM43430A1.hcd

BuildArch:  noarch
Obsoletes:  brcm43430-firmware
Conflicts:  brcm43430-firmware


%description
This package contains the binary firmware for Broadcom BCM43438 wifi/bluetooth module.
Wifi is supported by the brcmfmac driver. The BCM43438 wifi/bluetooth module is used
in the Raspberry Pi 3 Model B.

%prep
%setup -c -T %{name}-%{commit_short}

cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build


%install
%{__install} -d %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 brcmfmac43430-sdio.bin %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 brcmfmac43430-sdio.txt %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 BCM43430A1.hcd %{buildroot}/%{_libdir}/firmware/brcm/

%files
%license LICENSE
%{_libdir}/firmware/brcm/*


%changelog
* Fri May 06 2016 Vaughan <devel at agrez dot net> - 20160506-1.54bab3d
- Rename package (whilst the chipset identifies itself as bcm43430
  its actually the bcm43438 module that is used in the RPi3.)
- Add bluetooth firmware (sourced from openelec repo as RPi foundation
  don't seem to want to make this easily available anywhere.... why??)
- Add Obsoletes / Conflicts: brcm43430-firmware
  
* Thu Mar 10 2016 Vaughan <devel at agrez dot net> - 20160310-1.54bab3d
- Initial package
