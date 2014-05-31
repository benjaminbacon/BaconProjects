#include <linux/i2c-dev.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdint.h>
#include <errno.h>
#include <string.h>

#include "mcp23008.h"


int main()
{

	printf("start\n");
	int i;
	
	mcp23008_init(0x00);	// Set all pins to output

	while(1)
	{
		for(i=0;i<8;i++)	// Move left
		{
			mcp23008_write(1<<i);	// Write to port
			delay(200);				// Small delay
		}
		delay(200);
		
		for(i=7;i>=0;i--)	// Move right
		{
			mcp23008_write(1<<i);	// Write to port
			delay(200);				// Small delay
		}
		delay(200);	
		
	}

	return 0;
}

