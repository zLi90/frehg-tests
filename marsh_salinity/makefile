HOME=laspack

CC = mpicc

all:
	$(CC) configuration.c groundwater.c initialize.c map.c mpifunctions.c \
		  scalar.c shallowwater.c solve.c utility.c \
		  $(HOME)/eigenval.c $(HOME)/errhandl.c $(HOME)/factor.c $(HOME)/itersolv.c \
		  $(HOME)/matrix.c $(HOME)/mlsolv.c $(HOME)/operats.c $(HOME)/precond.c \
		  $(HOME)/qmatrix.c $(HOME)/vector.c $(HOME)/rtc.c FREHG.c -lm -O3 -o frehg
