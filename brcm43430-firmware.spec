#debug packages make no sense!
%global debug_package %{nil}
#no stripping required either
%global __os_install_post %{nil}

%global snap_date	20160310
%global commit_long	54bab3d6a6d43239c71d26464e6e10e5067ffea7
%global commit_short	%(c=%{commit_long}; echo ${c:0:7})

Name:          brcm43430-firmware
Version:       %{snap_date}
Release:       1.%{commit_short}%{?dist}
Summary:       Binary firmware for Broadcom BCM43430 802.11n SDIO chipset
Group:         System Environment/Kernel
License:       Redistributable, no modification permitted
URL:           https://github.com/RPi-Distro/firmware-nonfree
Source0:       https://github.com/RPi-Distro/firmware-nonfree/raw/%{commit_long}/brcm80211/brcm/brcmfmac43430-sdio.bin
Source1:       https://github.com/RPi-Distro/firmware-nonfree/raw/%{commit_long}/brcm80211/brcm/brcmfmac43430-sdio.txt
Source2:       https://github.com/RPi-Distro/firmware-nonfree/raw/%{commit_long}/brcm80211/LICENSE
BuildArch:     noarch

%description
This package contains the binary firmware for Broadcom BCM43430 802.11n SDIO chipset,
which is supported by the brcmfmac driver. This wifi chipset is used in the Raspberry
Pi 3 Model B.

%prep
%setup -c -T %{name}-%{commit_short}

cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%build


%install
%{__install} -d %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 brcmfmac43430-sdio.bin %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 brcmfmac43430-sdio.txt %{buildroot}/%{_libdir}/firmware/brcm/

%files
%license LICENSE
%{_libdir}/firmware/brcm/*


%changelog
* Thu Mar 10 2016 Vaughan <devel at agrez dot net> - 20160310-1.54bab3d
- Initial package
