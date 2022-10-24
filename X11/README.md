# This file contains a simple configuration about the mouse sensitivity

- # To config in your setup must the next things:
    - The name of your peripherial
        - For this, I recommend to use xinput, in Arch Linux you can install it with.
            ```bash
            sudo pacman -S xorg-xinput
            ```
            ### To use it just call the utility in your terminal with:
            ```bash
            xinput list
            ```

            ### In my case looks something like this:

            > Use the device that you want to use that appear in the 'Virtual core pointer' section first.
            >
            > If it dont works, use the device that appear 'Virtual core keyboard'

            ```bash
            ⎡ Virtual core pointer                    	    id=2	[master pointer  (3)]
            ⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
            ⎜   ↳ SONiX USB DEVICE Keyboard               	id=9	[slave  pointer  (2)]
            ⎜   ↳ Logitech USB Receiver                   	id=11	[slave  pointer  (2)]
            ⎜   ↳ Logitech USB Receiver Keyboard          	id=12	[slave  pointer  (2)]
            ⎣ Virtual core keyboard                   	    id=3	[master keyboard (2)]
                ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
                ↳ Power Button                            	id=6	[slave  keyboard (3)]
                ↳ Power Button                            	id=7	[slave  keyboard (3)]
                ↳ SONiX USB DEVICE                        	id=8	[slave  keyboard (3)]
                ↳ SONiX USB DEVICE Wireless Radio Control 	id=10	[slave  keyboard (3)]
                ↳ C-Media Electronics Inc. USB Advanced Audio Device Consumer Control	id=13	[slave  keyboard (3)]
                ↳ SONiX USB DEVICE Keyboard               	id=14	[slave  keyboard (3)]
                ↳ Logitech USB Receiver Keyboard          	id=15	[slave  keyboard (3)]
            ```
    - Then, replace the value of 'Identifier' key in the '50-mouse-deceleration.conf' file by the name of your peripherial

    - Then in the key **'Option "AccelSpeed"'** replace the number inside of double quotes, by the sensitivity that you want to use, in this case is -0.6.