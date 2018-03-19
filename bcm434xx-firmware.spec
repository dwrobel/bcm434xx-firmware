#debug packages make no sense!
%global debug_package %{nil}
#no stripping required either
%global __os_install_post %{nil}

%global snap_date	20180319
%global commit_long	86e88fbf0345da49555d0ec34c80b4fbae7d0cd3
%global commit_short	%(c=%{commit_long}; echo ${c:0:7})

Name:       bcm434xx-firmware
Version:    %{snap_date}
Release:    1.%{commit_short}%{?dist}
Summary:    Binary firmwares for Broadcom BCM434xx modules
Group:      System Environment/Kernel
License:    Redistributable, no modification permitted
URL:        https://github.com/RPi-Distro/firmware-nonfree
Source0:    %{url}/raw/%{commit_long}/brcm/brcmfmac43430-sdio.bin
Source1:    %{url}/raw/%{commit_long}/brcm/brcmfmac43430-sdio.txt
Source2:    %{url}/raw/%{commit_long}/LICENCE.broadcom_bcm43xx
Source3:    https://github.com/OpenELEC/misc-firmware/raw/master/firmware/brcm/BCM43430A1.hcd
Source4:    %{url}/raw/%{commit_long}/brcm/brcmfmac43455-sdio.bin
Source5:    %{url}/raw/%{commit_long}/brcm/brcmfmac43455-sdio.clm_blob
Source6:    %{url}/raw/%{commit_long}/brcm/brcmfmac43455-sdio.txt

BuildArch:  noarch
Conflicts:  linux-firmware < 20171215-83.git2451bb22
Conflicts:  bcm43438-firmware
Obsoletes:  bcm43438-firmware
Provides:   bcm43438-firmware


%description
This package contains binary firmwares for Broadcom BCM434xx wifi/bluetooth modules.
Wifi is supported by the brcmfmac driver. The BCM43xx wifi/bluetooth modules are used
in the Raspberry Pi 3 Model B (plus).

%prep
%setup -c -T %{name}-%{commit_short}

cp -a %{sources} .


%build


%install
%{__install} -d %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 %{SOURCE0} %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 %{SOURCE1} %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 %{SOURCE3} %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 %{SOURCE4} %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 %{SOURCE5} %{buildroot}/%{_libdir}/firmware/brcm/
%{__install} -p -m0644 %{SOURCE6} %{buildroot}/%{_libdir}/firmware/brcm/


%files
%license LICENCE.broadcom_bcm43xx
%{_libdir}/firmware/brcm/*


%changelog
* Mon Mar 19 2018 Vaughan <devel at agrez dot net> - 20180319-1.86e88fbf
- Rename package (it now contains multiple firmwares)
- Add brcmfmac43455 firmware files (for RPi3B+) (v7.45.154)
- Sync to commit 86e88fbf0345da49555d0ec34c80b4fbae7d0cd3
  (really brcmfmac43430-sdio.bin v7.45.98.38 this time!)

* Thu Mar 08 2018 Vaughan <devel at agrez dot net> - 20180306-1.927fa8e
- Re-add wifi firmware brcmfmac43430-sdio.bin
- Sync to commit 927fa8ebdf5bcfb90944465b40ec4981e01d6015
  (brcmfmac43430-sdio.bin version 7.45.98.38)
- Update spec

* Sat Oct 01 2016 Vaughan <devel at agrez dot net> - 20160627-2.a7491de
- Drop SOURCE0 (brcmfmac43430-sdio.bin) as its now inlcuded upstream
  (linux-firmware >= 20160923-68.git42ad5367.fc24)

* Mon Jun 27 2016 Vaughan <devel at agrez dot net> - 20160627-1.a7491de
- Sync to commit a7491de4c4b2f1ceb5d0dfa5350b95e5c6fb9bd4 (this updates 
  brcmfmac43430-sdio.bin to version 7.45.41.26)

* Fri May 06 2016 Vaughan <devel at agrez dot net> - 20160506-1.54bab3d
- Rename package (whilst the chipset identifies itself as bcm43430
  its actually the bcm43438 module that is used in the RPi3.)
- Add bluetooth firmware (sourced from openelec repo as RPi foundation
  don't seem to want to make this easily available anywhere.... why??)
- Add Obsoletes / Conflicts: brcm43430-firmware
  
* Thu Mar 10 2016 Vaughan <devel at agrez dot net> - 20160310-1.54bab3d
- Initial package
