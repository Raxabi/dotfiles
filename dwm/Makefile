# dwm - dynamic window manager
# See LICENSE file for copyright and license details.

include config.mk

SOURCE_DIR   = ./src
OUT_DIR      = ./out
BUILD_DIR    = ./build
INCL_DIR     = ./includes
LOCAL_INCL   = -I${INCL_DIR}

SRC = ${SOURCE_DIR}/drw.c ${SOURCE_DIR}/dwm.c ${SOURCE_DIR}/util.c
OBJ = ${subst ./src,./out,${SRC:.c=.o}}

# modify, all requirements over 'config.h' has been replaced by this var
CFG = ${INCL_DIR}/config.h

all: dwm

# modify, all object files will be compiled into ./out directory
# modify, "Old-Fashioned Suffix Rules" to "pattern rule"
# reference for this last change: https://stackoverflow.com/a/9233484/18592727
${OUT_DIR}/%.o: ${SOURCE_DIR}/%.c
	${CC} -c ${CFLAGS} ${LOCAL_INCL} $< -o $@

# add, same as above rule but for source files on the project root
${OUT_DIR}/%.o: %.c
	${CC} -c ${CFLAGS} ${LOCAL_INCL} $< -o $@

${OBJ}: ${CFG} config.mk

# modify, changed rule target
${CFG}:
	cp config.def.h $@

# modify, -o parameter no points to ./build/dwm
dwm: ${OBJ}
	${CC} -o ${BUILD_DIR}/$@ ${OBJ} ${LDFLAGS} ${LOCAL_INCL}

# modify, dwm binary is now removed form ./build/dwm
clean:
	rm -f ${BUILD_DIR}/dwm ${OBJ} dwm-${VERSION}.tar.gz

# modify, replaced header files location with 'includes' direectory
dist: clean
	mkdir -p dwm-${VERSION}
	cp -R LICENSE Makefile README config.def.h config.mk\
		dwm.1 ${INCL_DIR}/drw.h ${INCL_DIR}/util.h ${SRC} dwm.png transient.c dwm-${VERSION}
	tar -cf dwm-${VERSION}.tar dwm-${VERSION}
	gzip dwm-${VERSION}.tar
	rm -rf dwm-${VERSION}

# modify, dwm binary is now copied form ./build/dwm
install: all
	mkdir -p ${DESTDIR}${PREFIX}/bin
	cp -f ${BUILD_DIR}/dwm ${DESTDIR}${PREFIX}/bin
	chmod 755 ${DESTDIR}${PREFIX}/bin/dwm
	mkdir -p ${DESTDIR}${MANPREFIX}/man1
	sed "s/VERSION/${VERSION}/g" < dwm.1 > ${DESTDIR}${MANPREFIX}/man1/dwm.1
	chmod 644 ${DESTDIR}${MANPREFIX}/man1/dwm.1

# modify, added '-v' option parameter in rm
uninstall:
	rm -fv ${DESTDIR}${PREFIX}/bin/dwm\
		${DESTDIR}${MANPREFIX}/man1/dwm.1

.PHONY: all clean dist install uninstall
