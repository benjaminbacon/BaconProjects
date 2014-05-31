#include <linux/i2c-dev.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdint.h>
#include <errno.h>
#include <string.h>
#include "pi_i2c.h"
#include "mcp23008.h"

// Registers
#define	IODIRA	0x00
#define	GPIOA	0x09


// I2C Addres (A2,A1,A0 tied to ground)
#define ADDR	0x20
int fd;	

int mcp23008_init(unsigned char dir)
{
	fd = i2c_init("/dev/i2c-1");
	if ( fd < 0 ){
		return 1;
	}


	// Set pin directions
	i2c_write(fd, ADDR, a({IODIRA,dir}), 2);

	return 0;
}

int mcp23008_write(unsigned char data)
{
	// Set pin values
	i2c_write(fd, ADDR, a({GPIOA,data}), 2);
	
	
	
}


