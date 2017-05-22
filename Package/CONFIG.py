import ops
import iopc

def MAIN_ENV(args):
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    return False

def MAIN_EXTRACT(args):
    pkg_dir = args["pkg_path"]
    output_dir = args["output_path"]

    ops.copyto(iopc.getBaseRootFile("/lib/systemd/systemd"), output_dir)
    ops.ln(output_dir, "/lib/systemd/systemd", "init")

    ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libselinux.so.1"), output_dir)

    ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libpam.so.0.83.1"), output_dir)
    ops.ln(output_dir, "libpam.so.0.83.1", "libpam.so.0")

    ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libaudit.so.1.0.0"), output_dir)
    ops.ln(output_dir, "libaudit.so.1.0.0", "libaudit.so.1")

    ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libcap.so.2.24"), output_dir)
    ops.ln(output_dir, "libcap.so.2.24", "libcap.so.2")

    ops.copyto(iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libkmod.so.2.2.8"), output_dir)
    ops.ln(output_dir, "libkmod.so.2.2.8", "libkmod.so.2")

    return False

def MAIN_CONFIGURE(args):
    output_dir = args["output_path"]
    return False

def MAIN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN_INSTALL(args):
    output_dir = args["output_path"]

    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "systemd"), "lib/systemd/") 
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "init"), "")

    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "libselinux.so.1"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "libpam.so.0.83.1"), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "libpam.so.0"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "libaudit.so.1.0.0"), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "libaudit.so.1"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "libcap.so.2.24"), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "libcap.so.2"), "lib")

    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "libkmod.so.2.2.8"), "lib")
    iopc.installBin(args["pkg_name"], ops.path_join(output_dir, "libkmod.so.2"), "lib")

    return False

def MAIN_CLEAN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN(args):
    output_dir = args["output_path"]

