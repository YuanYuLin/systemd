import ops
import iopc

def MAIN_ENV(args):
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    return False

def MAIN_EXTRACT(args):
    pkg_dir = args["pkg_path"]
    output_bin_dir = ops.path_join(args["output_path"], "bin")
    output_lib_dir = ops.path_join(args["output_path"], "lib")
    output_etc_dir = ops.path_join(args["output_path"], "etc")
    output_usr_lib_dir = ops.path_join(args["output_path"], "usr/lib")
    output_usr_bin_dir = ops.path_join(args["output_path"], "usr/bin")
    output_root_dir = args["output_path"]
    arch = ops.getEnv("ARCH_ALT")

    ops.mkdir(output_lib_dir)
    ops.copyto(iopc.getBaseRootFile("/lib/systemd"), output_lib_dir)
    ops.ln(output_root_dir, "/lib/systemd/systemd", "init")

    ops.mkdir(output_etc_dir)
    ops.copyto(iopc.getBaseRootFile("/etc/systemd"), output_etc_dir)

    ops.mkdir(output_usr_lib_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/lib/systemd"), output_usr_lib_dir)

    ops.mkdir(output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/systemd-analyze"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/deb-systemd-invoke"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/systemd-detect-virt"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/systemd-run"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/systemd-cgtop"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/systemd-nspawn"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/systemd-cat"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/systemd-path"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/systemd-cgls"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/systemd-stdio-bridge"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/deb-systemd-helper"), output_usr_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/usr/bin/systemd-delta"), output_usr_bin_dir)

    ops.mkdir(output_bin_dir)
    ops.ln(output_bin_dir, "/lib/systemd/systemd", "systemd")
    ops.copyto(iopc.getBaseRootFile("/bin/systemctl"), output_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/bin/systemd-ask-password"), output_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/bin/systemd-inhibit"), output_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/bin/systemd-notify"), output_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/bin/systemd-tty-ask-password-agent"), output_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/bin/systemd-escape"), output_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/bin/systemd-machine-id-setup"), output_bin_dir)
    ops.copyto(iopc.getBaseRootFile("/bin/systemd-tmpfiles"), output_bin_dir)
    ops.ln(output_bin_dir, "/lib/systemd/systemd", "systemd")

    if arch == "armhf":
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libselinux.so.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libpam.so.0.83.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libaudit.so.1.0.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libcap.so.2.24"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libkmod.so.2.2.8"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libsystemd.so.0.3.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/liblzma.so.5.0.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libgcrypt.so.20.0.3"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libresolv-2.19.so"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libgpg-error.so.0.13.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libpcre.so.3.13.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libattr.so.1.1.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libblkid.so.1.1.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libacl.so.1.1.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libuuid.so.1.3.0"), output_lib_dir)

        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabihf/libicudata.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabihf/libicui18n.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabihf/libicuio.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabihf/libicule.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabihf/libiculx.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabihf/libicutest.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabihf/libicutu.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabihf/libicuuc.so.52.1"), output_lib_dir)

    elif arch == "armel":
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libselinux.so.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libpam.so.0.83.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libaudit.so.1.0.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libcap.so.2.24"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libkmod.so.2.2.8"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libsystemd.so.0.3.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/liblzma.so.5.0.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libgcrypt.so.20.0.3"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libresolv-2.19.so"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libgpg-error.so.0.13.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libpcre.so.3.13.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libattr.so.1.1.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libblkid.so.1.1.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libacl.so.1.1.0"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabi/libuuid.so.1.3.0"), output_lib_dir)

        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabi/libicudata.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabi/libicui18n.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabi/libicuio.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabi/libicule.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabi/libiculx.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabi/libicutest.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabi/libicutu.so.52.1"), output_lib_dir)
        ops.copyto(iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabi/libicuuc.so.52.1"), output_lib_dir)

    else:
        sys.exit(1)

    ops.ln(output_lib_dir, "libpam.so.0.83.1", "libpam.so.0")
    ops.ln(output_lib_dir, "libaudit.so.1.0.0", "libaudit.so.1")
    ops.ln(output_lib_dir, "libcap.so.2.24", "libcap.so.2")
    ops.ln(output_lib_dir, "libkmod.so.2.2.8", "libkmod.so.2")
    ops.ln(output_lib_dir, "libsystemd.so.0.3.1", "libsystemd.so.0")
    ops.ln(output_lib_dir, "liblzma.so.5.0.0", "liblzma.so.5")
    ops.ln(output_lib_dir, "libgcrypt.so.20.0.3", "libgcrypt.so.20")
    ops.ln(output_lib_dir, "libresolv-2.19.so", "libresolv.so.2")
    ops.ln(output_lib_dir, "libgpg-error.so.0.13.0", "libgpg-error.so.0")
    ops.ln(output_lib_dir, "libpcre.so.3.13.1", "libpcre.so.3")
    ops.ln(output_lib_dir, "libattr.so.1.1.0", "libattr.so.1")
    ops.ln(output_lib_dir, "libblkid.so.1.1.0", "libblkid.so.1")
    ops.ln(output_lib_dir, "libacl.so.1.1.0", "libacl.so.1")
    ops.ln(output_lib_dir, "libuuid.so.1.3.0", "libuuid.so.1")

    ops.ln(output_lib_dir, "libicudata.so.52.1", "libicudata.so.52")
    ops.ln(output_lib_dir, "libicui18n.so.52.1", "libicui18n.so.52")
    ops.ln(output_lib_dir, "libicuio.so.52.1", "libicuio.so.52")
    ops.ln(output_lib_dir, "libicule.so.52.1", "libicule.so.52")
    ops.ln(output_lib_dir, "libiculx.so.52.1", "libiculx.so.52")
    ops.ln(output_lib_dir, "libicutest.so.52.1", "libicutest.so.52")
    ops.ln(output_lib_dir, "libicutu.so.52.1", "libicutu.so.52")
    ops.ln(output_lib_dir, "libicuuc.so.52.1", "libicuuc.so.52")

    return False

def MAIN_CONFIGURE(args):
    output_dir = args["output_path"]
    return False

def MAIN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN_INSTALL(args):
    output_dir = args["output_path"]

    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "bin/."), "bin") 
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "lib/."), "lib") 
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "etc/."), "etc") 
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "usr/."), "usr") 
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "init"), "")

    return False

def MAIN_CLEAN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN(args):
    output_dir = args["output_path"]

