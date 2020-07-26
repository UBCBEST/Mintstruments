# MOCK INSTRUMENTS (=MINTSTRUMENT)

Due to the difficulties of trasportation which the COVID-19 pandemic presents, we are developing a set of mock
instruments to model the physical instruments with which we would interface. This will initially be restricted
to the instruments which will be used with the MAML project. There is no reason why other projects can't use
this, or make their own mock instruments.

## Goal

Classes or packages which will mock the interface with an instrument, which will act (mostly) in the same way
that the real instrument will act. This will allow us to develop the code which processes the instrument data
while working remotely.

## Specific Instruments

### smbus (I2C) 

Here, we are mocking an I2C device, where we will use the `smbus2` package to do the hard work.
The `smbus2` package has these functions below which we need to mock.

function              |           description           |         parameters         | return value |
|:-----------------------------------:|:-------------------------------:|:--------------------------:|:------------:|
|             SMBus Access            |                                 |                            |              |
| write_quick(addr)                   | Quick transaction.              | int addr                   | long         |
| read_byte(addr)                     | Read Byte transaction.          | int addr                   | long         |
| write_byte(addr,val)                | Write Byte transaction.         | int addr,char val          | long         |
| read_byte_data(addr,cmd)            | Read Byte Data transaction.     | int addr,char cmd          | long         |
| write_byte_data(addr,cmd,val)       | Write Byte Data transaction.    | int addr,char cmd,char val | long         |
| read_word_data(addr,cmd)            | Read Word Data transaction.     | int addr,char cmd          | long         |
| write_word_data(addr,cmd,val)       | Write Word Data transaction.    | int addr,char cmd,int val  | long         |
| process_call(addr,cmd,val)          | Process Call transaction.       | int addr,char cmd,int val  | long         |
| read_block_data(addr,cmd)           | Read Block Data transaction.    | int addr,char cmd          | long[]       |
| write_block_data(addr,cmd,vals)     | Write Block Data transaction.   | int addr,char cmd,long[]   | None         |
| block_process_call(addr,cmd,vals)   | Block Process Call transaction. | int addr,char cmd,long[]   | long[]       |
|              I2C Access             |                                 |                            |              |
| read_i2c_block_data(addr,cmd)       | Block Read transaction.         | int addr,char cmd          | long[]       |
| write_i2c_block_data(addr,cmd,vals) | Block Write transaction.        | int addr,char cmd,long[]   | None         |



###### why is it called mintstruments?
###### i was eating altoids while writing it
