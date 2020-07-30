from typing import Dict


I2C_SMBUS_READ = 0  # placeholder
I2C_SMBUS_BLOCK_MAX = 32


class mock_smbus2:
    def __init__(self, bus: None = Dict, force: False = bool):
        """Initialize and (optionally) open an i2c bus connection

        :param bus: this is really an "address to device" map that we will use here
            to get a device object (e.g. MPR_device()) from an address (e.g. 0x18)
        :param force: in the real SMBus, the documentation says "force using the slave
            address even when driver is already using it.
        """
        self.addr = None
        self.bus = None
        if bus is not None:
            self.bus = self.open(bus)

    def __enter__(self):
        """Enter handler."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit handler."""
        self.close()

    def open(self, bus):
        """
        Takes "bus", which is a map from an address of an i2c device (e.g. 0x18) to
        the device class; this method instantiates each of the devices.

        This may be silly and needless, but I think it adds a bit more realism (i.e. you
        need to "initialize" something, whether it be the bus or the objects). I may take
        this out later if it ends up being silly.
        """
        return {addr: device() for addr, device in bus.items()}

    def close(self):
        """
        Close the i2c connection - in our case, just make self.bus None
        """
        self.bus = None

    def _set_address(self, addr, force=None):
        """
        Set i2c slave address to use for subsequent calls

        As it sits, this is a kinda pointless method; however, after looking
        into this entire thing, it is clear that we can get pretty darn accurate
        with the simulation. So I am leaving this here just so we keep it in mind,
        in case we end up diving more into all this. Again, I may remove it if
        it ends up being dumb.
        """
        self.addr = addr

    def _get_funcs(self):
        """
        This is just something that I am not going to do right now - I am not exactly sure
        what was the use case for this is. Don't you usually have the datasheet?
        """
        return 0

    def write_quick(self, i2c_addr, force=None):
        """
        This sends a single bit to the device, at the place of the Rd/Wr bit.
        i.e. it sends a 0 or 1, to be used as start, stop, ack, e.t.c.
        """
        # TODO: Come back to this
        self._set_address(i2c_addr, force=force)
        self.bus[self.addr]._read(0)

    def read_byte(self, i2c_addr, force=None):
        """
        Read a single byte from a device.
        According to the SMBus Protocol Summary,

            This reads a single byte from a device, without specifying a device
            register. Some devices are so simple that this interface is enough; for
            others, it is a shorthand if you want to read the same register as in
            the previous SMBus command.

        So I don't think MAML will have much use for this.
        The way we do this is a little weird, because we aren't reading
        registers from an I2C bus. But c'est la vie, if there is a better
        way to do this, we should change it
        """
        self._set_address(i2c_addr, force=force)
        return self.bus[self.addr]._read(self)

    def write_byte(self, i2c_addr, value, force=None):
        """
        Write a single byte to a device. According to the SMBus Protocol Summary,

            This operation is the reverse of Receive Byte: it sends a single byte
            to a device.  See Receive Byte for more information.

        """
        self._set_address(i2c_addr, force=force)
        self.bus[addr]._write(val)

    def read_byte_data(self, i2c_addr, register, force=None):
        """
        Read a single byte from a designated register. From the SMBus Protocol Summary,

            This reads a single byte from a device, from a designated register.
            The register is specified through the Comm byte.

        I believe that this is the register on the device. TODO: Confirm this
        """
        self._set_address(i2c_addr, force=force)
        return self.bus[self.addr]._read(self, register=register)

    def write_byte_data(self, i2c_addr, register, value, force=None):
        """
        Write a byte to a given register.

            This reads a single byte from a device, from a designated register.
            The register is specified through the Comm byte.
        """
        self._set_address(i2c_addr, force=force)
        self.bus[self.addr]._write(value, register=register)

    def read_word_data(self, i2c_addr, register, force=None):
        """
        Read a single word (2 bytes) from a given register.

            This operation is very like Read Byte; again, data is read from a
            device, from a designated register that is specified through the Comm
            byte. But this time, the data is a complete word (16 bits)
        """
        self._set_address(i2c_addr, force=force)
        self.bus[self.addr]._read(self, register=register, size=2)
        return  # TODO fixme

    def write_word_data(self, i2c_addr, register, value, force=None):
        """
        Write a byte to a given register.


            This writes a single byte to a device, to a designated register. The
            register is specified through the Comm byte. This is the opposite of
            the Read Byte operation.
        """
        self._set_address(i2c_addr, force=force)
        self.bus[self.addr]._write(value, self, register=register, size=2)

    def process_call(self, i2c_addr, register, value, force=None):
        """
        From the SMBus Protocol,

            This command selects a device register (through the Comm byte), sends
            16 bits of data to it, and reads 16 bits of data in return.

        So it is just a "write word data" then a "read word data". This could be
        for scenarios where you want to tell the device to do something, and then
        return the result immediately.
        """
        self.write_word_data(i2c_addr, register, value, force=force)
        return self.read_word_data(i2c_addr, register, value, force=force)

    def read_block_data(self, i2c_addr, register, force=None):
        """
        Read a block of up to 32-bytes from a given register.
        """
        self._set_address(i2c_addr, force=force)
        self.bus[self.addr]._read(self, register=register, size=I2C_SMBUS_BLOCK_MAX)
        return  # TODO fixme

    def write_block_data(self, i2c_addr, register, data, force=None):
        """
        Write a block of byte data to a given register.

            The opposite of the Block Read command, this writes up to 32 bytes to
            a device, to a designated register that is specified through the
            Comm byte. The amount of data is specified in the Count byte.
        """
        self._set_address(i2c_addr, force=force)
        self.bus[self.addr]._write(value, self, register=register)

    def block_process_call(self, i2c_addr, register, data, force=None):
        """
        Executes a SMBus Block Process Call, sending a variable-size data
        block and receiving another variable-size response
        """
        self.write_i2c_block_data(i2c_addr, register, data, force=force)
        return self.read_i2c_block_data(i2c_addr, register, size, force=force)

    def read_i2c_block_data(self, i2c_addr, register, size, force=None):
        """
        Read a block of byte data from a given register.
        """
        if size > I2C_SMBUS_BLOCK_MAX:
            err_str = f"Desired block size over {I2C_SMBUS_BLOCK_MAX} bytes"
            raise ValueError(err_str)
        self._set_address(i2c_addr, force=force)
        r = self.bus[self.addr]._read(self, register=register, size=size)
        return r

    def write_i2c_block_data(self, i2c_addr, register, data, force=None):
        """
        Write a block of byte data to a given register.
        """
        size = len(data)
        if size > I2C_SMBUS_BLOCK_MAX:
            err_str = "Data size cannot exceed {I2C_SMBUS_BLOCK_MAX} bytes"
            raise ValueError(err_str)
        self._set_address(i2c_addr, force=force)
        self.bus[self.addr]._write(data, register=register, size=len(data))

    def i2c_rdwr(self, *i2c_msgs):
        """
        Combine a series of i2c read and write operations in a single
        transaction (with repeated start bits but no stop bits in between).
        This method takes i2c_msg instances as input, which must be created
        first with :py:meth:`i2c_msg.read` or :py:meth:`i2c_msg.write`.
        :param i2c_msgs: One or more i2c_msg class instances.
        :type i2c_msgs: i2c_msg
        :rtype: None


        I will look at this later, but not for now
        """
        ioctl_data = i2c_rdwr_ioctl_data.create(*i2c_msgs)
        ioctl(self.fd, I2C_RDWR, ioctl_data)
