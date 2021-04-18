import subprocess




def load_module():
    """This function loads the module and returns any errors that occur in the process."""
    proc = subprocess.Popen(["pactl", "set-default-sink", "alsa_output.usb-3DSA_USB_SOUND_3DSA_USB_SOUND_23456789-00.analog-stereo"], stderr=subprocess.PIPE)
    stderr = proc.communicate()[1].decode("UTF-8")
    return stderr


def main():
    """Main function"""
    err = load_module()
    if len(err) > 0:
        Exception("[ALSA&PULSEAUDIO FIX][ERROR] Error settingdefault card`!"
                  "Output pactl: {}".format(err))
    else:
        print("[ALSA&PULSEAUDIO FIX][INFO] Default card set!")


if __name__ == '__main__':
    main()
