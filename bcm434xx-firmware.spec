#debug packages make no sense!
%global debug_package %{nil}
%global _build_id_links none
%global __debug_package %{nil}
#no stripping required either
%global __os_install_post %{nil}

%global snap_date   20240810
%global commit_fw   4b356e134e8333d073bd3802d767a825adec3807
%global commit_bt   78d6a07730e2d20c035899521ab67726dc028e1c
%global commit_short	%(c=%{commit_fw}; echo ${c:0:7})
%global fetch_url	https://raw.githubusercontent.com/RPi-Distro

Name:       bcm434xx-firmware
Version:    %{snap_date}
Release:    1.%{commit_short}%{?dist}
Summary:    Binary firmwares for Broadcom BCM434xx modules
Group:      System Environment/Kernel
License:    Redistributable, no modification permitted
URL:        https://github.com/RPi-Distro/
Source0:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/copyright

Source1:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/defines
Source2:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/cypress/README.txt
# RPi3B wifi firmware
Source3:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/cypress/cyfmac43430-sdio.bin
Source4:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/cypress/cyfmac43430-sdio.clm_blob
Source5:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/brcm/brcmfmac43430-sdio.txt
# RPi3B bluetooth firmware
Source6:    %{fetch_url}/bluez-firmware/%{commit_bt}/debian/firmware/broadcom/BCM43430A1.hcd
# RPi3B+ wifi firmware
Source7:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/cypress/cyfmac43455-sdio-standard.bin
Source77:   %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/cypress/cyfmac43455-sdio-minimal.bin
Source8:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/cypress/cyfmac43455-sdio.clm_blob
Source9:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/brcm/brcmfmac43455-sdio.txt
# RPi3B+ bluetooth firmware
Source10:    %{fetch_url}/bluez-firmware/%{commit_bt}/debian/firmware/broadcom/BCM4345C0.hcd
# RPi400 wifi firmware
Source11:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/brcm/brcmfmac43456-sdio.bin
Source12:    %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/brcm/brcmfmac43456-sdio.clm_blob
Source13:   %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/brcm/brcmfmac43456-sdio.txt
# RPiZero 2 W
Source14:   %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/brcm/brcmfmac43436-sdio.bin
Source15:   %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/brcm/brcmfmac43436-sdio.clm_blob
Source16:   %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/brcm/brcmfmac43436-sdio.txt
Source17:   %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/brcm/brcmfmac43436s-sdio.bin
Source18:   %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/brcm/brcmfmac43436s-sdio.txt
# RpiPico W
Source19:   %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/cypress/cyfmac43439-sdio.bin
Source20:   %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/cypress/cyfmac43439-sdio.clm_blob
Source21:   %{fetch_url}/firmware-nonfree/%{commit_fw}/debian/config/brcm80211/cypress/cyfmac43439-sdio.txt

BuildArch:  noarch
Conflicts:  linux-firmware < 20171215-83.git2451bb22
Conflicts:  bcm43438-firmware
Obsoletes:  bcm43438-firmware <= 20180306-1.927fa8e
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
%{__install} -d %{buildroot}%{_prefix}/lib/firmware/
for i in %{SOURCE1}; do
    %{__install} -p -m0644 $i %{buildroot}%{_prefix}/lib/firmware/
done

%{__install} -d %{buildroot}%{_prefix}/lib/firmware/cypress/
for i in %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE7} %{SOURCE77} %{SOURCE8}; do
    %{__install} -p -m0644 $i %{buildroot}%{_prefix}/lib/firmware/cypress/
done

%{__install} -d %{buildroot}%{_prefix}/lib/firmware/brcm/
for i in %{SOURCE5} %{SOURCE6} \
  %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
  %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18}; do
    %{__install} -p -m0644 $i %{buildroot}%{_prefix}/lib/firmware/brcm/
done

pushd %{buildroot}%{_prefix}/lib/firmware/cypress/
  # Use standard version by default
  ln -s cyfmac43455-sdio-standard.bin cyfmac43455-sdio.bin
popd

pushd %{buildroot}%{_prefix}/lib/firmware/brcm/
  # Generated from firmware-nonfree/debian/config/brcm80211/brcm directory using:
  # $ ls -ls | grep -- '->' | awk '{print "  ln -s "$12 "\t" $10}'
  ln -s brcmfmac43436-sdio.bin	brcmfmac43430b0-sdio.raspberrypi,model-zero-2-w.bin
  ln -s brcmfmac43436-sdio.clm_blob	brcmfmac43430b0-sdio.raspberrypi,model-zero-2-w.clm_blob
  ln -s brcmfmac43436-sdio.txt	brcmfmac43430b0-sdio.raspberrypi,model-zero-2-w.txt
  ln -s ../cypress/cyfmac43430-sdio.bin	brcmfmac43430-sdio.bin
  ln -s ../cypress/cyfmac43430-sdio.clm_blob	brcmfmac43430-sdio.clm_blob
  ln -s ../cypress/cyfmac43430-sdio.bin	brcmfmac43430-sdio.raspberrypi,3-model-b.bin
  ln -s ../cypress/cyfmac43430-sdio.clm_blob	brcmfmac43430-sdio.raspberrypi,3-model-b.clm_blob
  ln -s brcmfmac43430-sdio.txt	brcmfmac43430-sdio.raspberrypi,3-model-b.txt
  ln -s brcmfmac43436s-sdio.bin	brcmfmac43430-sdio.raspberrypi,model-zero-2-w.bin
  ln -s brcmfmac43436s-sdio.txt	brcmfmac43430-sdio.raspberrypi,model-zero-2-w.txt
  ln -s ../cypress/cyfmac43430-sdio.bin	brcmfmac43430-sdio.raspberrypi,model-zero-w.bin
  ln -s ../cypress/cyfmac43430-sdio.clm_blob	brcmfmac43430-sdio.raspberrypi,model-zero-w.clm_blob
  ln -s brcmfmac43430-sdio.txt	brcmfmac43430-sdio.raspberrypi,model-zero-w.txt
  ln -s brcmfmac43436-sdio.bin	brcmfmac43436-sdio.raspberrypi,model-zero-2-w.bin
  ln -s brcmfmac43436-sdio.clm_blob	brcmfmac43436-sdio.raspberrypi,model-zero-2-w.clm_blob
  ln -s brcmfmac43436-sdio.txt	brcmfmac43436-sdio.raspberrypi,model-zero-2-w.txt
  ln -s brcmfmac43436s-sdio.bin	brcmfmac43436s-sdio.raspberrypi,model-zero-2-w.bin
  ln -s brcmfmac43436s-sdio.txt	brcmfmac43436s-sdio.raspberrypi,model-zero-2-w.txt
  ln -s ../cypress/cyfmac43439-sdio.bin	brcmfmac43439-sdio.bin
  ln -s ../cypress/cyfmac43439-sdio.clm_blob	brcmfmac43439-sdio.clm_blob
  ln -s ../cypress/cyfmac43439-sdio.txt	brcmfmac43439-sdio.txt
  ln -s ../cypress/cyfmac43455-sdio.bin	brcmfmac43455-sdio.bin
  ln -s ../cypress/cyfmac43455-sdio.clm_blob	brcmfmac43455-sdio.clm_blob
  ln -s ../cypress/cyfmac43455-sdio.bin	brcmfmac43455-sdio.raspberrypi,3-model-a-plus.bin
  ln -s ../cypress/cyfmac43455-sdio.clm_blob	brcmfmac43455-sdio.raspberrypi,3-model-a-plus.clm_blob
  ln -s brcmfmac43455-sdio.txt	brcmfmac43455-sdio.raspberrypi,3-model-a-plus.txt
  ln -s ../cypress/cyfmac43455-sdio.bin	brcmfmac43455-sdio.raspberrypi,3-model-b-plus.bin
  ln -s ../cypress/cyfmac43455-sdio.clm_blob	brcmfmac43455-sdio.raspberrypi,3-model-b-plus.clm_blob
  ln -s brcmfmac43455-sdio.txt	brcmfmac43455-sdio.raspberrypi,3-model-b-plus.txt
  ln -s ../cypress/cyfmac43455-sdio.bin	brcmfmac43455-sdio.raspberrypi,4-compute-module.bin
  ln -s ../cypress/cyfmac43455-sdio.clm_blob	brcmfmac43455-sdio.raspberrypi,4-compute-module.clm_blob
  ln -s brcmfmac43455-sdio.txt	brcmfmac43455-sdio.raspberrypi,4-compute-module.txt
  ln -s ../cypress/cyfmac43455-sdio.bin	brcmfmac43455-sdio.raspberrypi,4-model-b.bin
  ln -s ../cypress/cyfmac43455-sdio.clm_blob	brcmfmac43455-sdio.raspberrypi,4-model-b.clm_blob
  ln -s brcmfmac43455-sdio.txt	brcmfmac43455-sdio.raspberrypi,4-model-b.txt
  ln -s ../cypress/cyfmac43455-sdio.bin	brcmfmac43455-sdio.raspberrypi,5-model-b.bin
  ln -s ../cypress/cyfmac43455-sdio.clm_blob	brcmfmac43455-sdio.raspberrypi,5-model-b.clm_blob
  ln -s brcmfmac43455-sdio.txt	brcmfmac43455-sdio.raspberrypi,5-model-b.txt
  ln -s brcmfmac43456-sdio.bin	brcmfmac43456-sdio.raspberrypi,400.bin
  ln -s brcmfmac43456-sdio.clm_blob	brcmfmac43456-sdio.raspberrypi,400.clm_blob
  ln -s brcmfmac43456-sdio.txt	brcmfmac43456-sdio.raspberrypi,400.txt
  ln -s brcmfmac43456-sdio.bin	brcmfmac43456-sdio.raspberrypi,4-compute-module.bin
  ln -s brcmfmac43456-sdio.clm_blob	brcmfmac43456-sdio.raspberrypi,4-compute-module.clm_blob
  ln -s brcmfmac43456-sdio.txt	brcmfmac43456-sdio.raspberrypi,4-compute-module.txt
popd

%files
%license copyright
%{_prefix}/lib/firmware/defines
%dir %{_prefix}/lib/firmware/cypress
%{_prefix}/lib/firmware/cypress/*
%dir %{_prefix}/lib/firmware/brcm
%{_prefix}/lib/firmware/brcm/*


%changelog
* Wed Oct 23 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2020810-1.4b356e1
- Sync firmware-nonfree to commit: 20240810git4b356e1
- Sync bluez-firmware to commit:   20240226git78d6a07
- Update symlinks

* Thu Jan 11 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20231115-1.88aa085
- Sync firmware-nonfree to commit: 20231115git88aa085
- Sync bluez-firmware to commit:   20231024gitd9d4741
- Update symlinks

* Thu Oct 19 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20231006-1.d763667
- Sync firmware-nonfree to commit: 20231006gitd763667

* Thu Jul 06 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20230619-1.b5df30d
- Sync firmware-nonfree to commit: 20230619gitb5df30d

* Wed Jan 25 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20230125-1.7f29411
- Sync firmware-nonfree to commit: 20230125git7f29411
- Sync bluez-firmware to commit:   20230105git9556b08

* Tue Sep 13 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20220714-1.d9c8834
- Sync firmware-nonfree to commit: 20220714gitd9c8834
- Sync bluez-firmware to commit:   20220505git31ad688

* Thu Mar 31 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20211206-1.99d5c58
- Sync firmware-nonfree to commit: 20211206git99d5c58

* Mon Jan 31 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20211028-2.bda9207
- Sync firmware-nonfree to commit: 20211028gitbda9207

* Wed Sep 22 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20210922-1.d27b9f1
- Sync firmware-nonfree to commit: 20210922gitd27b9f1

* Thu Jun 24 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20210623-1.00de319
- Sync firmware-nonfree to commit: 20210623git00de319
- Add RPi400 firmware

* Fri Mar 12 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20210125-1.83938f7
- Sync firmware-nonfree to commit: 20210125git83938f7
- Sync bluez-firmware to commit:   20210128gite7fd166

* Wed Dec 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20201201-1.b66ab26
- Sync firmware-nonfree to commit: 20201201gitb66ab26
- Sync bluez-firmware to commit:   20201126git1e4ee0c

* Fri Sep 11 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20200902-2.98e8157
- Fix install dir on aarch64

* Wed Sep 02 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20200902-1.98e8157
- Sync firmware-nonfree to commit: 20200729git98e8157
- Sync bluez-firmware to commit:   20200805gitafe608e

* Fri May 29 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20200529-1.616fc2d
- Sync firmware-nonfree to commit: 20200417git616fc2d
- Sync bluez-firmware to commit:   20200518git98cbd44

* Mon Mar 09 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20200306-1.ce751a8
- Sync firmware-nonfree to commit: 20200306gitce751a8
- Sync bluez-firmware to commit:   20191202gitfff76cb
- Fix rpm warning: "It's not recommended to have unversioned Obsoletes"

* Tue Oct 01 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20190530-1.130cb86
- Update to the latest available release (fixes lack of wlan on RPi4B)

* Sat Apr 20 2019 Vaughan <devel at agrez dot net> - 20190420-1.b518de4
- Update RPi3B+ bluetooth firmware (BCM4345C0.hcd v003.001.025.0156.0280)

* Wed Oct 10 2018 Vaughan <devel at agrez dot net> - 20181010-1.b518de4
- Refactor sources (all firmware now sourced from https://github.com/RPi-Distro)
- Sync firmware-nonfree to commit b518de45ced519e8f7a499f4778100173402ae43
- Sync bluez-firmware to commit ade2bae1aaaebede09abb8fb546f767a0e4c7804
- Add RPi3B+ bluetooth firmware (BCM4345C0.hcd)

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
