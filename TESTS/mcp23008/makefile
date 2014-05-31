#
# Makefile for gertboard test programs
#
#
# Copyright (C) Gert Jan van Loo & Myra VanInwegen 2012
# No rights reserved
# You may treat this program as if it was in the public domain
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Keep things simple for novice users
# so do not use any implicit rules!
#
all : mcp23008_demo 

clean :
	rm *.o mcp23008_demo

mcp23008_demo : mcp23008.o pi_i2c.o mcp23008_demo.o
	gcc -o mcp23008_demo pi_i2c.o mcp23008.o mcp23008_demo.o


# The next lines generate the various object files

pi_i2c.o : pi_i2c.c pi_i2c.h
	gcc -c pi_i2c.c

mcp23008.o : mcp23008.c mcp23008.h
		gcc -c mcp23008.c

mcp23008_demo.o : mcp23008_demo.c pi_i2c.h mcp23008.h
	gcc -c mcp23008_demo.c
