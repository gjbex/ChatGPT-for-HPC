CXX = nvc++
CXXFLAGS = -mp=gpu
LDFLAGS = -mp=gpu

all: devices.exe hello_world.exe

%.exe: %.o
	$(CXX) $(LDFLAGS) -o $@ $<

%.o: %.c
	$(CXX) -c $(CXXFLAGS) $<

clean:
	$(RM) $(wildcard *.o) $(wildcard *.exe)
